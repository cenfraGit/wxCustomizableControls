"""checkbox.py

wxCustomizableControls
14/dec/2024
cenfra
"""


from copy import copy
from ._window import Window
import wx


class CheckBox(Window):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator,
                 name=wx.CheckBoxNameStr, config=None, **kwargs):

        # ------------------- control attributes ------------------- #
        
        kwargs["label"] = label
        kwargs["value"] = False

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # --------- text, image and checkbox calculations --------- #
        
        text_width, text_height = self._get_text_dimensions(self._Label, gc)

        bitmap, image_width, image_height = self._get_bitmap_and_dimensions()

        # first we calculate the text label and image area dimensions
        text_image_rectangle_width, text_image_rectangle_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config["image_separation"],
            self._config["image_side"])

        # now we calculate the coordinates for the previous rectangle
        # and the checkbox itself. we will take into consideration the
        # width of the checkbox border.
        text_image_rectangle_x, text_image_rectangle_y, checkbox_x, checkbox_y = self._get_coords_object_sides(
            drawing_rect,
            text_image_rectangle_width, text_image_rectangle_height,
            self._config["checkbox_width"] + self._get_max_value("borderwidth", "checkbox"),
            self._config["checkbox_height"] + self._get_max_value("borderwidth", "checkbox"),
            self._config["checkbox_separation"],
            self._config["checkbox_side"])

        # ----------------------- rectangles ----------------------- #

        checkbox_rectangle = wx.Rect(checkbox_x,
                                     checkbox_y,
                                     self._config["checkbox_width"] + self._get_max_value("borderwidth", "checkbox"),
                                     self._config["checkbox_height"] + self._get_max_value("borderwidth", "checkbox"))
        # we use deflate to automatically calculate the new top left
        # rectangle coordinates instead of doing it manually. this new
        # rectangle is the actual checkbox, without border width
        # consideration.
        checkbox_rectangle = checkbox_rectangle.Deflate(self._get_max_value("borderwidth", "checkbox") // 2 + 1,
                                                        self._get_max_value("borderwidth", "checkbox") // 2 + 1)
        text_image_rectangle = wx.Rect(
            text_image_rectangle_x,
            text_image_rectangle_y,
            text_image_rectangle_width,
            text_image_rectangle_height)

        # ------------------- drawing rectangles ------------------- #

        # draw text label and image
        self._draw_text_and_bitmap(self._Label, text_width, text_height,
                                   bitmap, image_width, image_height,
                                   text_image_rectangle, gcdc)
        # draw checkbox rectangle
        gcdc.SetPen(self._get_pen_current("checkbox"))
        gc.SetBrush(self._get_brush_current("checkbox", gc))
        gcdc.DrawRoundedRectangle(checkbox_rectangle,
                                  self._config[f"checkbox_cornerradius_{self._get_state()}"])

        # -------------------- selection marker -------------------- #

        if self._Value:
            # create smaller rectangle to represent checkmark area
            selection_rectangle: wx.Rect = copy(checkbox_rectangle).Deflate(int(self._config["checkbox_width"] * 0.3),
                                                                            int(self._config["checkbox_height"] * 0.3))
            # draw the selection marker
            gcdc.SetPen(self._get_pen_current("selectionmarker"))
            gc.SetBrush(wx.TRANSPARENT_BRUSH)
            path: wx.GraphicsPath = gc.CreatePath()
            path.MoveToPoint(selection_rectangle.GetX(),
                             selection_rectangle.GetY() + (selection_rectangle.GetHeight() // 1.5))
            path.AddLineToPoint(selection_rectangle.GetX() + (selection_rectangle.GetWidth() // 2.5),
                                selection_rectangle.GetY() + selection_rectangle.GetHeight())
            path.AddLineToPoint(*selection_rectangle.GetTopRight())
            gc.StrokePath(path)

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()
                          
    def _handle_event(self) -> None:
        if self._Hover:
            self._Value = not self._Value
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_CHECKBOX.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        text_width, text_height = self._get_text_dimensions(self._Label, gc)
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        text_image_width, text_image_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config[f"image_separation"],
            self._config[f"image_side"])
        width, height = self._get_object_sides_dimensions(
            text_image_width, text_image_height,
            self._config["checkbox_width"] + self._get_max_value("borderwidth", "checkbox"),
            self._config["checkbox_height"] + self._get_max_value("borderwidth", "checkbox"),
            self._config["checkbox_separation"],
            self._config["checkbox_side"])
        # padding
        width += 5
        height += 5
        return wx.Size(int(width), int(height))
    
