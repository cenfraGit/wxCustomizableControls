"""object.py

The CustomizableObject class will be inherited from all of the
customizable objects in the library (both controls and other windows
which are not controls, like panels). This class will keep track of
the object's configuration data and also include methods to modify
this data.

The CustomizableObject class will also include useful methods used
during the drawing process.

wxCustomizableControls
13/dec/2024
cenfra
"""


from copy import copy
from typing import Tuple, Literal
import os
import wx


class CustomizableObject:
    def __init__(self, config: dict):
        self._config = copy(config)

    def SetConfig(self, config: dict):
        self._config = config

    def GetConfig(self):
        return self._config

    def _get_drawing_contexts(self, window) -> Tuple[wx.GCDC, wx.GraphicsContext]:
        """Creates the BufferedPaintDC and returns the GCDC with its
        GraphicsContext reference.
        """
        dc = wx.BufferedPaintDC(window)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        return gcdc, gc

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

    def _get_element_properties(self, element: str, state: str, gc) -> dict:
        """Returns a dictionary containing all properties belonging to
        the element, in the current window state.
        """
        # initial properties dictionary
        properties = {}
        # iterate over config to find element properties with state
        for attribute, value in self._config.items():
            parts = attribute.split('_')
            # up to this point, we have divided the attribute:
            # background_colour, drawingarea, default
            if (parts[1] == element) and (parts[2] == state):
                properties[parts[0]] = value
        # we can also add the pen and the brush to the dictionary
        properties["pen"] = self._get_pen(properties["bordercolor"],
                                          properties["borderwidth"],
                                          properties["borderstyle"])
        properties["brush"] = self._get_brush(properties["backgroundcolor"],
                                              properties["backgroundstyle"],
                                              gc)
        return properties

    def _get_pen(self, bordercolor: list, borderwidth: int,
                 borderstyle: str) -> wx.Pen:
        return wx.Pen(wx.Colour(bordercolor),
                     borderwidth,
                     self._get_tool_style("pen", borderstyle))

    def _get_brush(self, backgroundcolor: list, backgroundstyle: str, gc:
                   wx.GraphicsContext) -> wx.Brush:
        # the backgroundcolor can either be an rgb tuple or a linear
        # gradient tuple. if the length of the list is 3, use normal
        # brush. else, try to create a linear gradient brush
        if len(backgroundcolor) == 3:
            return wx.Brush(wx.Colour(backgroundcolor),
                            self._get_tool_style("brush", backgroundstyle))
        else:
            return gc.CreateLinearGradientBrush(*backgroundcolor)

    def _get_font(self, state) -> wx.Font:
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

        return wx.Font(fontsize, wx.FONTFAMILY_DEFAULT, fontstyle,
                       fontweight, faceName=fontfacename)

    def _get_text_dimensions(self, text: str, state: str, gc: wx.GraphicsContext) -> Tuple[int, int]:
        text_width, text_height = 0, 0
        if (text.strip() != ""):
            gc.SetFont(self._get_font(state), wx.WHITE)
            text_width, text_height, _, _ = gc.GetFullTextExtent(text)
        return text_width, text_height

    def _get_bitmap_and_dimensions(self, state) -> Tuple[wx.Bitmap, int, int]:
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        bitmap = wx.Bitmap(1, 1)

        image_path = self._config[f"path_image_{state}"]
        image_path = os.path.normpath(image_path)
        image_path = os.path.abspath(image_path)
        _, image_extension = os.path.splitext(image_path)
        # if the file indicated by the path exists
        if os.path.isfile(image_path) and image_extension in [".png", ".jpg", ".jpeg"]:
            image_width = self._config[f"width_image_{state}"]
            image_height = self._config[f"height_image_{state}"]
            image: wx.Image = wx.Image(image_path).AdjustChannels(*self._config[f"channels_image_{state}"])
            image = image.Scale(image_width, image_height, wx.IMAGE_QUALITY_HIGH)
            bitmap: wx.Bitmap = image.ConvertToBitmap()
            #bitmap.SetSize(wx.Size(image_width, image_height))
        return bitmap, image_width, image_height            

    def _get_max_value(self, property: str, element: str) -> int:
        """Returns the maximum value of an element's property for all
        its states. The property must be numeric.
        """
        values = []
        for state in ["default", "hover", "pressed", "disabled"]:
            values.append(self._config[f"{property}_{element}_{state}"])
        return max(*values)

    def _get_coords_object_sides(self, drawing_rectangle: wx.Rect,
                                 object1_width: int, object1_height: int,
                                 object2_width: int, object2_height: int,
                                 separation: int,
                                 object2_side: Literal["left", "right", "up", "down"]) -> Tuple[int, int, int, int]:
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
            elif (object2_side == "up"):
                object2_X = r.GetX() + (r.GetWidth() // 2) - (object2_width // 2)
                object2_Y = r.GetY() + (r.GetHeight() // 2) - ((object1_height + separation + object2_height) // 2)
                object1_X = r.GetX() + (r.GetWidth() // 2) - (object1_width // 2)
                object1_Y = object2_Y + object2_height + separation
            elif (object2_side == "down"):
                object1_X = r.GetX() + (r.GetWidth() // 2) - (object1_width // 2)
                object1_Y = r.GetY() + (r.GetHeight() // 2) - ((object1_height + separation + object2_height) // 2)
                object2_X = r.GetX() + (r.GetWidth() // 2) - (object2_width // 2)
                object2_Y = object1_Y + object1_height + separation
        return int(object1_X), int(object1_Y), int(object2_X), int(object2_Y)

    def _draw_text_and_bitmap(self, text: str, text_width: int, text_height: int,
                              bitmap: wx.Bitmap, image_width: int, image_height: int,
                              rectangle: wx.Rect, gcdc: wx.GCDC, state: str) -> None:
        """Draws text and a bitmap in the specified rectangle, taking
        into account the text side and the separation between the
        bitmap and the text.
        """
        image_x, image_y, text_x, text_y = self._get_coords_object_sides(rectangle,
                                                                         image_width, image_height,
                                                                         text_width, text_height,
                                                                         self._config[f"separation_image_{state}"],
                                                                         self._config[f"side_image_{state}"])
        if text.strip() != "":
            gcdc.DrawText(text, text_x, text_y)
        if (image_width != 0) and (image_height != 0):
            gcdc.DrawBitmap(bitmap, image_x, image_y)

