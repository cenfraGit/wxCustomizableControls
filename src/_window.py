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
import os
from typing import Tuple, Literal
import wx


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

        self._ActOnPress = kwargs.get("act_on_press", False)
        self._UseDefaults = kwargs.get("use_defaults", False)

        # ------------------- configuration data ------------------- #

        # the _config attribute holds the configuration data in
        # dictionary format for convenient key manipulation.

        self._config = copy(config)

        # ---------------------- window setup ---------------------- #

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.SetInitialSize(size)

        # -------------- timers and color transitions -------------- #

        self._timer_ms = 50
        
        self._timer_paint_steps = 10
        self._timer_paint_steps_counter = 0

        self._timer_hover = wx.Timer(self)
        self._timer_pressed = wx.Timer(self)

        self.Bind(wx.EVT_TIMER, self._on_timer_hover, self._timer_hover)
        self.Bind(wx.EVT_TIMER, self._on_timer_pressed, self._timer_pressed)

        self._color_current = ()
        self._color_target = ()

        # ------------------------- events ------------------------- #

        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda _: None)
        
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_enter_window)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave_window)

        self.Bind(wx.EVT_LEFT_DCLICK, self._on_left_down)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_left_up)

    def _calculate_rgb_steps(self, rgb_start, rgb_end) -> list:
        """Returns the increments per rgb channel in order to get a
        color transition for all three channels in the same steps.
        """
        def get_increment(start: int, end: int, steps: int):
            range = end - start
            return range / steps
        return [
            get_increment(rgb_end[0], rgb_start[0], self._timer_paint_steps),
            get_increment(rgb_end[1], rgb_start[1], self._timer_paint_steps),
            get_increment(rgb_end[2], rgb_start[2], self._timer_paint_steps)
        ]

    def _on_timer_hover(self, event):
        if self._timer_paint_steps_counter <= self._timer_paint_steps:
            print("test")
            self._timer_paint_steps_counter += 1
        else:
            self._timer_paint_steps_counter = 0
            self._timer_hover.Stop()
    
    def _on_timer_pressed(self, event):
        pass

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

    def SetValue(self, state: bool) -> None:
        self._Value = state
        self.Refresh()

    def GetValue(self):
        return self._Value

    def GetBackgroundColour(self) -> wx.Colour:
        """Returns the current background color of the customizable
        window.
        """
        window_type = self.__class__.__name__
        color = self._config[f"{window_type.lower()}_backgroundcolor_{self._get_state()}"]
        if len(color) == 3:
            return wx.Colour(*color)
        else:
            return wx.BLACK # a gradient

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
        if not self._timer_hover.IsRunning():
            self._timer_hover.Start(self._timer_ms)
            self._color_target = self._config[f"{self.__class__.__name__.lower()}_backgroundcolor_hover"]
        self._Hover = True
        self.Refresh()
        event.Skip()

    def _on_leave_window(self, event: wx.Event) -> None:
        if self._UseDefaults:
            event.Skip()
            return None
        if not self._timer_hover.IsRunning():
            self._timer_hover.Start(self._timer_ms)
            self._color_target = self._config[f"{self.__class__.__name__.lower()}_backgroundcolor_default"]
        self._Hover = False
        self.Refresh()
        event.Skip()

    def _on_left_down(self, event: wx.Event) -> None:
        if not self._Pressed:
            self.CaptureMouse()
            self._Pressed = True
            if self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _on_left_up(self, event: wx.Event) -> None:
        if self._Pressed:
            self.ReleaseMouse()
            self._Pressed = False
            if not self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _handle_event(self) -> None:
        raise NotImplementedError("_handle_event")
    
    def _on_paint(self, event: wx.Event) -> None:
        raise NotImplementedError("_on_paint")

    # --------------------- useful methods --------------------- #

    def _configure_cursor(self) -> None:
        state = self._get_state()
        if state != "default":
            self.SetCursor(self._get_cursor(self._config[f"mousecursor_{state}"]))

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

    def _get_pen_element(self, element: str) -> wx.Pen:
        state = self._get_state()
        return wx.Pen(wx.Colour(self._config[f"{element}_bordercolor_{state}"]),
                      self._config[f"{element}_borderwidth_{state}"],
                      self._get_tool_style("pen", self._config[f"{element}_borderstyle_{state}"]))

    def _get_brush_element(self, element: str, gc: wx.GraphicsContext) -> wx.Brush:
        # the backgroundcolor can either be an rgb tuple or a linear
        # gradient tuple. if the length of the list is 3, use normal
        # brush. else, try to create a linear gradient brush
        state = self._get_state()
        backgroundcolor = self._config[f"{element}_backgroundcolor_{state}"]
        backgroundstyle = self._config[f"{element}_backgroundstyle_{state}"]
        if len(backgroundcolor) == 3:
            return wx.Brush(wx.Colour(backgroundcolor),
                            self._get_tool_style("brush", backgroundstyle))
        else:
            return gc.CreateLinearGradientBrush(*backgroundcolor)

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

    # -------------------- drawing methods -------------------- #

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
    
