"""_window.py

The base class for all customizable windows.

This class will be inherited from all of the customizable objects in
the library (both controls and other windows which are not controls,
like panels). This class will keep track of the object's configuration
data and also include methods used during the drawing process.

wxCustomizableControls
16/dec/2024
cenfra
"""


from copy import copy
import math
import os
from typing import Tuple, Literal
import wx

from ._utils import VectorRGB


class Window(wx.Window):    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name=wx.PanelNameStr,
                 config={}, **kwargs):

        super().__init__(parent, id, pos, size, style|wx.NO_BORDER, name)

        # --------------------- window states --------------------- #

        # these states are used to keep track of user input and window
        # behavior.

        self._Enabled = True
        self._Pressed = False
        self._Hover = False

        # ------------------- control attributes ------------------- #

        # these attributes are used when creating controls. you must
        # pass them to this class via the kwargs dictionary before
        # initializing this class.

        self._Label = kwargs.get("label", None)
        self._Value = kwargs.get("value", None)
        self._Choices = kwargs.get("choices", None)
        self._Range = kwargs.get("range", None)

        self._ActOnPress = kwargs.get("act_on_press", False)
        self._UseDefaults = kwargs.get("use_defaults", False)
        self._UseSmoothTransitions = kwargs.get("use_smooth_transitions", True)

        # ------------------- configuration data ------------------- #

        # the _config attribute holds the configuration data in
        # dictionary format for convenient key manipulation.

        self._config = copy(config)

        # ---------------------- window setup ---------------------- #

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.SetInitialSize(size)

        # -------------- timers and colour transitions -------------- #

        self._timer_ms = 15
        self._timer_paint_steps_counter = 0

        self._timer_smoothing = wx.Timer(self)

        # these attributes will store the element (key), and a new
        # dict containing its current rgb colour and its target rgb
        # colour. used for colour smoothing for all elements which need
        # them        
        # {"button": {"current": VectorRGB(0, 0, 0), "target": VectorRGB(0, 0, 0)}}
        self._colour_smoothing_brushes = {} # using backgroundcolour attributes
        self._colour_smoothing_pens    = {} # using bordercolour attributes

        # save initial colour data
        for key in self._config.keys():
            if "backgroundcolour_default" in key:
                attribute_parts = key.split('_')
                backgroundtype = self._get_background_type(attribute_parts[0])
                current = VectorRGB(*self._config[key]) if (backgroundtype == "solid") else VectorRGB(127, 127, 127)
                self._colour_smoothing_brushes[attribute_parts[0]] = {"current": current,
                                                                     "target": VectorRGB(0, 0, 0)}
            elif "bordercolour_default" in key:
                attribute_parts = key.split('_')
                self._colour_smoothing_pens[attribute_parts[0]] = {"current": VectorRGB(*self._config[key]),
                                                                  "target": VectorRGB(0, 0, 0)}

        # ------------------------- events ------------------------- #

        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda _: None)
        
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_enter_window)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave_window)

        self.Bind(wx.EVT_LEFT_DCLICK, self._on_left_down)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_left_up)

        self.Bind(wx.EVT_TIMER, self._on_timer_smoothing)

    # ------------------------- public ------------------------- #

    def SetConfig(self, config: dict) -> None:
        self._config = config
        self.Refresh()

    def GetConfig(self) -> dict:
        return self._config

    def SetLabel(self, label: str) -> None:
        self._Label = label
        self.Refresh()

    def GetLabel(self) -> str:
        return self._Label

    def SetValue(self, value) -> None:
        self._Value = value
        self.Refresh()

    def GetValue(self):
        return self._Value

    def SetRange(self, value: int) -> None:
        self._Range = value
        self.Refresh()

    def GetRange(self):
        return self._Range

    def GetBackgroundColour(self) -> wx.Colour:
        """Returns the current background colour of the customizable
        window.
        """
        window_type = self.__class__.__name__
        colour_attribute = f"{window_type.lower()}_backgroundcolour_default"
        if colour_attribute in self._config:
            colour = self._config[colour_attribute]
            if len(colour) == 3:
                return wx.Colour(*colour)
            else:
                return wx.BLACK
        else:
            return self.GetParent().GetBackgroundColour()

    def Enable(self, enable:bool=True) -> None:
        self._Enabled = enable
        super().Enable(enable)
        self.Refresh()

    def Disable(self) -> None:
        self.Enable(False)

    # ------------------------- events ------------------------- #

    def _on_enter_window(self, event: wx.Event) -> None:
        if self._UseDefaults:
            event.Skip()
            return None

        self._Hover = True
        self._handle_colour_transition()
            
        self.Refresh()
        event.Skip()

    def _on_leave_window(self, event: wx.Event) -> None:
        if self._UseDefaults:
            event.Skip()
            return None

        self._Hover = False
        self._handle_colour_transition()
            
        self.Refresh()
        event.Skip()

    def _on_left_down(self, event: wx.Event) -> None:
        if not self._Pressed:

            self._Pressed = True
            self._handle_colour_transition()
                
            self.CaptureMouse()
            if self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _on_left_up(self, event: wx.Event) -> None:
        if self._Pressed:

            self._Pressed = False
            self._handle_colour_transition()
                
            self.ReleaseMouse()
            if not self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _on_timer_smoothing(self, event: wx.TimerEvent) -> None:
        """Uses easing functions so smooth out the colour transition
        between states. Updates the current colour for all pens and
        brushes.
        """
        # get last valid state
        state = self._get_state()
        if state in ["hover", "pressed"]:
            self._last_state = state
        else:
            self._last_state = "hover"
        timer_paint_steps = int(self._config[f"colourtransition_ms_{self._last_state}"] / self._timer_ms)
        if self._timer_paint_steps_counter < timer_paint_steps:
            
            t = self._timer_paint_steps_counter / timer_paint_steps
            easing_t = self._get_easing_t(t)

            for colour_values in self._colour_smoothing_brushes.values():
                if isinstance(colour_values["current"], VectorRGB) and isinstance(colour_values["target"], VectorRGB):
                    colour_values["current"] = colour_values["current"] + (colour_values["target"] - colour_values["current"]) * easing_t
                else:
                    colour_values["current"] = colour_values["target"]
            for colour_values in self._colour_smoothing_pens.values():
                colour_values["current"] = colour_values["current"] + (colour_values["target"] - colour_values["current"]) * easing_t

            self._timer_paint_steps_counter += 1
        else:
            self._timer_paint_steps_counter = 0
            self._timer_smoothing.Stop()
        self.Refresh()
        event.Skip()

    def _on_paint(self, event: wx.Event) -> None:
        raise NotImplementedError("_on_paint")
    
    def _handle_event(self) -> None:
        raise NotImplementedError("_handle_event")
    
    # -------------------- colour smoothing -------------------- #

    def _handle_colour_transition(self) -> None:
        if self._UseSmoothTransitions:
            self._update_colour_targets()
            self._timer_paint_steps_counter = 0
            if not self._timer_smoothing.IsRunning():
                self._timer_smoothing.Start(self._timer_ms)
        else:
            self._update_colour_currents()

    def _update_colour_targets(self) -> None:
        """Updates the colour targets for all brushes and pens
        depending on the state of the window.
        """
        for element, colour_values in self._colour_smoothing_brushes.items():
            if self._get_background_type(element) == "solid":
                colour_values["target"] = VectorRGB(*self._config[f"{element}_backgroundcolour_{self._get_state()}"])
            else: # if gradient
                colour_values["target"] = VectorRGB(0, 0, 0)
        for element, colour_values in self._colour_smoothing_pens.items():
            colour_values["target"] = VectorRGB(*self._config[f"{element}_bordercolour_{self._get_state()}"])

    def _update_colour_currents(self) -> None:
        """Updates the colour currents for all brushes and pens
        depending on the state of the window. Used for non-smooth
        colour transitioning.
        """
        for element, colour_values in self._colour_smoothing_brushes.items():
            colour_values["current"] = VectorRGB(*self._config[f"{element}_backgroundcolour_{self._get_state()}"])
        for element, colour_values in self._colour_smoothing_pens.items():
            colour_values["current"] = VectorRGB(*self._config[f"{element}_bordercolour_{self._get_state()}"])

    def _cubic_bezier(self, t, p0, p1, p2, p3) -> float:
        return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

    def _get_easing_t(self, t: float) -> float:
        p0, p3 = 0, 1
        p1, p2 = 0.42, 0.58
        return self._cubic_bezier(t, p0, p1, p2, p3)
    
    # ---------------------- get methods ---------------------- #

    def _get_state(self) -> str:
        """Returns the state of the window. Will return "default" if
        self._UseDefaults is True.
        """
        if self._UseDefaults:
            return "default"
        
        if not self._Enabled:
            return "disabled"
        elif self._Pressed:
            return "pressed"
        elif self._Hover:
            return "hover"
        else:
            return "default"

    def _get_drawing_contexts(self, window) -> Tuple[wx.GCDC, wx.GraphicsContext]:
        """Creates the BufferedPaintDC and returns the GCDC with its
        GraphicsContext reference.
        """
        dc = wx.BufferedPaintDC(window)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        return gcdc, gc

    def _get_pen_current(self, element: str) -> wx.Pen:
        state = self._get_state()
        penwidth = self._config[f"{element}_borderwidth_{state}"]
        penstyle = self._config[f"{element}_borderstyle_{state}"]
        if (penwidth == 0):
            return wx.TRANSPARENT_PEN
        return wx.Pen(self._colour_smoothing_pens[element]["current"].GetValue(),
                      penwidth,
                      self._get_tool_style("pen", penstyle))

    def _get_brush_current(self, element: str, gc: wx.GraphicsContext) -> wx.Brush:
        state = self._get_state()
        backgroundcolour = self._config[f"{element}_backgroundcolour_{state}"]
        backgroundstyle = self._config[f"{element}_backgroundstyle_{state}"]
        if len(backgroundcolour) == 3:
            return wx.Brush(self._colour_smoothing_brushes[element]["current"].GetValue(),
                            self._get_tool_style("brush", backgroundstyle))
        else:
            return gc.CreateLinearGradientBrush(*backgroundcolour)

    def _get_pen_element(self, element: str) -> wx.Pen:
        state = self._get_state()
        pen_width = self._config[f"{element}_borderwidth_{state}"]
        if (pen_width == 0):
            return wx.TRANSPARENT_PEN
        return wx.Pen(wx.Colour(self._config[f"{element}_bordercolour_{state}"]),
                      self._config[f"{element}_borderwidth_{state}"],
                      self._get_tool_style("pen", self._config[f"{element}_borderstyle_{state}"]))

    def _get_brush_element(self, element: str, gc: wx.GraphicsContext) -> wx.Brush:
        # the backgroundcolour can either be an rgb tuple or a linear
        # gradient tuple. if the length of the list is 3, use normal
        # brush. else, try to create a linear gradient brush
        state = self._get_state()
        backgroundcolour = self._config[f"{element}_backgroundcolour_{state}"]
        backgroundstyle = self._config[f"{element}_backgroundstyle_{state}"]
        if len(backgroundcolour) == 3:
            return wx.Brush(wx.Colour(backgroundcolour),
                            self._get_tool_style("brush", backgroundstyle))
        else:
            return gc.CreateLinearGradientBrush(*backgroundcolour)

    def _get_brush_parent_background(self) -> wx.Brush:
        return wx.Brush(self.GetParent().GetBackgroundColour())

    def _get_font(self) -> wx.Font:
        state = self._get_state()
        fontfacename = self._config[f"fontfacename_{state}"]
        fontsize = self._config[f"fontsize_{state}"]
        fontstyle = self._config[f"fontstyle_{state}"]
        fontweight = self._config[f"fontweight_{state}"]
        
        if fontstyle == "normal":
            fontstyle = wx.FONTSTYLE_NORMAL
        elif fontstyle == "italic":
            fontstyle = wx.FONTSTYLE_ITALIC

        if fontweight == "normal":
            fontweight = wx.FONTWEIGHT_NORMAL
        elif fontweight == "bold":
            fontweight = wx.FONTWEIGHT_BOLD

        return wx.Font(fontsize, wx.FONTFAMILY_DEFAULT, fontstyle, fontweight, faceName=fontfacename)

    def _get_cursor(self, cursor: str) -> wx.Cursor:
        cursor_styles = {
            "none": wx.CURSOR_NONE,
            "arrow": wx.CURSOR_ARROW,
            "right_arrow": wx.CURSOR_RIGHT_ARROW,
            "bullseye": wx.CURSOR_BULLSEYE,
            "char": wx.CURSOR_CHAR,
            "cross": wx.CURSOR_CROSS,
            "hand": wx.CURSOR_HAND,
            "ibeam": wx.CURSOR_IBEAM,
            "left_button": wx.CURSOR_LEFT_BUTTON,
            "magnifier": wx.CURSOR_MAGNIFIER,
            "middle_button": wx.CURSOR_MIDDLE_BUTTON,
            "no_entry": wx.CURSOR_NO_ENTRY,
            "paint_brush": wx.CURSOR_PAINT_BRUSH,
            "pencil": wx.CURSOR_PENCIL,
            "point_left": wx.CURSOR_POINT_LEFT,
            "point_right": wx.CURSOR_POINT_RIGHT,
            "question_arrow": wx.CURSOR_QUESTION_ARROW,
            "right_button": wx.CURSOR_RIGHT_BUTTON,
            "sizenesw": wx.CURSOR_SIZENESW,
            "sizens": wx.CURSOR_SIZENS,
            "sizenwse": wx.CURSOR_SIZENWSE,
            "sizewe": wx.CURSOR_SIZEWE,
            "sizing": wx.CURSOR_SIZING,
            "spraycan": wx.CURSOR_SPRAYCAN,
            "wait": wx.CURSOR_WAIT,
            "watch": wx.CURSOR_WATCH,
            "blank": wx.CURSOR_BLANK,
            "default": wx.CURSOR_DEFAULT,
            "copy_arrow": wx.CURSOR_COPY_ARROW,
            "arrowwait": wx.CURSOR_ARROWWAIT,
            "max": wx.CURSOR_MAX
        }
        return wx.Cursor(cursor_styles[cursor])

    def _get_tool_style(self, tool: Literal["pen", "brush"], style: str):
        pen_styles = {
            "solid": wx.PENSTYLE_SOLID,
            "dot": wx.PENSTYLE_DOT,
            "long_dash": wx.PENSTYLE_LONG_DASH,
            "short_dash": wx.PENSTYLE_SHORT_DASH,
            "dot_dash": wx.PENSTYLE_DOT_DASH,
            "transparent": wx.PENSTYLE_TRANSPARENT,
            "stipple": wx.PENSTYLE_STIPPLE,
            "bdiagonal_hatch": wx.PENSTYLE_BDIAGONAL_HATCH,
            "crossdiag_hatch": wx.PENSTYLE_CROSSDIAG_HATCH,
            "fdiagonal_hatch": wx.PENSTYLE_FDIAGONAL_HATCH,
            "cross_hatch": wx.PENSTYLE_CROSS_HATCH,
            "horizontal_hatch": wx.PENSTYLE_HORIZONTAL_HATCH,
            "vertical_hatch": wx.PENSTYLE_VERTICAL_HATCH,
            "first_hatch": wx.PENSTYLE_FIRST_HATCH,
            "last_hatch": wx.PENSTYLE_LAST_HATCH,
            }
        brush_styles = {
            "solid": wx.BRUSHSTYLE_SOLID,
            "transparent": wx.BRUSHSTYLE_TRANSPARENT,
            "stipple": wx.BRUSHSTYLE_STIPPLE,
            "bdiagonal_hatch": wx.BRUSHSTYLE_BDIAGONAL_HATCH,
            "crossdiag_hatch": wx.BRUSHSTYLE_CROSSDIAG_HATCH,
            "fdiagonal_hatch": wx.BRUSHSTYLE_FDIAGONAL_HATCH,
            "cross_hatch": wx.BRUSHSTYLE_CROSS_HATCH,
            "horizontal_hatch": wx.BRUSHSTYLE_HORIZONTAL_HATCH,
            "vertical_hatch": wx.BRUSHSTYLE_VERTICAL_HATCH,
            "first_hatch": wx.BRUSHSTYLE_FIRST_HATCH,
            "last_hatch": wx.BRUSHSTYLE_LAST_HATCH,
            }
        if tool == "pen" and style in pen_styles.keys():
            return pen_styles[style]
        elif tool == "brush" and style in brush_styles.keys():
            return brush_styles[style]
        else:
            raise ValueError("Incorrect tool or style.")
    
    def _get_text_dimensions(self, text: str, gc: wx.GraphicsContext) -> Tuple[int, int]:
        text_width, text_height = 0, 0
        if (text.strip() != ""):
            gc.SetFont(self._get_font(), wx.WHITE)
            text_width, text_height, _, _ = gc.GetFullTextExtent(text)
        return text_width, text_height

    def _get_bitmap_and_dimensions(self) -> Tuple[wx.Bitmap, int, int]:
        state = state = self._get_state()
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        bitmap = wx.Bitmap(1, 1)

        image_path = self._config[f"image_path_{state}"]
        image_path = os.path.normpath(image_path)
        image_path = os.path.abspath(image_path)
        _, image_extension = os.path.splitext(image_path)
        # if the file indicated by the path exists
        if os.path.isfile(image_path) and image_extension in [".png", ".jpg", ".jpeg"]:
            image_width = self._config[f"image_width_{state}"]
            image_height = self._config[f"image_height_{state}"]
            image: wx.Image = wx.Image(image_path).AdjustChannels(*self._config[f"image_channels_{state}"])
            image = image.Scale(image_width, image_height, wx.IMAGE_QUALITY_HIGH)
            bitmap: wx.Bitmap = image.ConvertToBitmap()
            #bitmap.SetSize(wx.Size(image_width, image_height))
        return bitmap, image_width, image_height            

    def _get_max_value(self, prop: str, element: str) -> int:
        """Returns the maximum value of an element's property for all
        its states. The property must be numeric.
        """
        values = []
        for state in ["default", "hover", "pressed", "disabled"]:
            values.append(self._config[f"{element}_{prop}_{state}"])
        return max(*values)

    def _get_coords_object_sides(self, drawing_rectangle: wx.Rect,
                                 object1_width: int, object1_height: int,
                                 object2_width: int, object2_height: int,
                                 separation: int,
                                 object2_side: Literal["left", "right", "top", "bottom"]) -> Tuple[int, int, int, int]:
        """Returns the coordinates for two objects that are side by
        side, depending on their separation and the side of object2.
        """
        # initialize coordinates
        object1_X, object1_Y = 0, 0
        object2_X, object2_Y = 0, 0
        r = drawing_rectangle # alias
        
        object1_exists:bool = (object1_width != 0 and object1_height != 0)
        object2_exists:bool = (object2_width != 0 and object2_height != 0)

        if not object2_exists:
            # object1 in center of rectangle
            object1_X = r.GetX() + (r.GetWidth() // 2) - (object1_width // 2)
            object1_Y = r.GetY() + (r.GetHeight() // 2) - (object1_height // 2)
        elif not object1_exists:
            # object2 in center of rectangle
            object2_X = r.GetX() + (r.GetWidth() // 2) - (object2_width // 2)
            object2_Y = r.GetY() + (r.GetHeight() // 2) - (object2_height // 2)
        else: # drawing both objects
            if (object2_side == "right"):
                object1_X = r.GetX() + (r.GetWidth() // 2) - ((object1_width + separation + object2_width) // 2)
                object1_Y = r.GetY() + (r.GetHeight() // 2) - (object1_height // 2)
                object2_X = object1_X + object1_width + separation
                object2_Y = r.GetY() + (r.GetHeight() // 2) - (object2_height // 2)
            elif (object2_side == "left"):
                object2_X = r.GetX() + (r.GetWidth() // 2) - ((object1_width + separation + object2_width) // 2)
                object2_Y = r.GetY() + (r.GetHeight() // 2) - (object2_height // 2)
                object1_X = object2_X + object2_width + separation
                object1_Y = r.GetY() + (r.GetHeight() // 2) - (object1_height // 2)
            elif (object2_side == "top"):
                object2_X = r.GetX() + (r.GetWidth() // 2) - (object2_width // 2)
                object2_Y = r.GetY() + (r.GetHeight() // 2) - ((object1_height + separation + object2_height) // 2)
                object1_X = r.GetX() + (r.GetWidth() // 2) - (object1_width // 2)
                object1_Y = object2_Y + object2_height + separation
            elif (object2_side == "bottom"):
                object1_X = r.GetX() + (r.GetWidth() // 2) - (object1_width // 2)
                object1_Y = r.GetY() + (r.GetHeight() // 2) - ((object1_height + separation + object2_height) // 2)
                object2_X = r.GetX() + (r.GetWidth() // 2) - (object2_width // 2)
                object2_Y = object1_Y + object1_height + separation
        return int(object1_X), int(object1_Y), int(object2_X), int(object2_Y)

    def _get_object_sides_dimensions(self, object1_width: int, object1_height: int,
                                     object2_width: int, object2_height: int,
                                     separation: int,
                                     object2_side: Literal["left", "right", "top", "bottom"]) -> Tuple[int, int]:
        """Returns the dimensions of an imaginary rectangle containing
        object1 and object2 depending on their arrangement. Used in
        images, checkboxes, radiobuttons.
        """
        rectangle_width, rectangle_height = 0, 0
        if (object2_side == "right" or object2_side == "left"):
            rectangle_width = object1_width + separation + object2_width
            rectangle_height = max(object1_height, object2_height)
        elif (object2_side == "top" or object2_side == "bottom"):
            rectangle_width = max(object1_width, object2_width)
            rectangle_height = object1_height + separation + object2_height
        return int(rectangle_width), int(rectangle_height)

    def _get_background_type(self, element: str) -> str:
        """Returns a string ("solid" or "gradient") indicating the
        type of background of the element.
        """
        state = self._get_state()
        backgroundcolour = self._config[f"{element}_backgroundcolour_{state}"]
        if len(backgroundcolour) == 3:
            return "solid"
        else:
            return "gradient"

    # --------------------- useful methods --------------------- #

    def _configure_cursor(self) -> None:
        state = self._get_state()
        if state != "default":
            self.SetCursor(self._get_cursor(self._config[f"mousecursor_{state}"]))

    def _draw_text_and_bitmap(self, text: str, text_width: int, text_height: int,
                              bitmap: wx.Bitmap, image_width: int, image_height: int,
                              rectangle: wx.Rect, gcdc: wx.GCDC) -> None:
        """Draws text and a bitmap in the specified rectangle, taking
        into account the text side and the separation between the
        bitmap and the text.
        """
        text_x, text_y, image_x, image_y = self._get_coords_object_sides(rectangle,
                                                                         text_width, text_height,
                                                                         image_width, image_height,
                                                                         self._config[f"image_separation"],
                                                                         self._config[f"image_side"])
        if text.strip() != "":
            gcdc.DrawText(text, text_x, text_y)
        if (image_width != 0) and (image_height != 0):
            gcdc.DrawBitmap(bitmap, image_x, image_y)
    
