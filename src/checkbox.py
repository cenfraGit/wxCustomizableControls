"""checkbox.py

A customizable checkbox.

wxCustomizableControls
14/dec/2024
cenfra
"""


from .base.window import CustomizableWindow
import wx


class CheckBox(CustomizableWindow):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator, name=wx.CheckBoxNameStr, config={},
                 **kwargs):

        # control attributes
        kwargs["label"] = label
        kwargs["value"] = False

        # initialize window
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _on_paint(self, event: wx.Event) -> None:
        state = "default" if self._UseDefaults else self._get_state_as_string()

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        # drawing area
        drawing_area: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gcdc.SetBrush(wx.Brush(self.GetParent().GetBackgroundColour()))
        gcdc.DrawRectangle(drawing_area)

        # text
        text_width, text_height = self._get_text_dimensions(self._Label, state, gc)

        # image
        bitmap, image_width, image_height = self._get_bitmap_and_dimensions(state)

        # we need to calculate the dimensions of an imaginary
        # rectangle containing both the text label and the image
        text_image_rectangle_width, text_image_rectangle_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config["separation_image"],
            self._config["side_image"])

        # now we calculate the coordinates for the previous rectangle
        # and the checkbox itself
        checkbox_x, checkbox_y, text_image_rectangle_x, text_image_rectangle_y = self._get_coords_object_sides(
            drawing_area,
            self._config["width_checkbox"], self._config["height_checkbox"],
            text_image_rectangle_width, text_image_rectangle_height,
            self._config["separation_checkbox"],
            self._config["side_checkbox"])

        # create rectangles
        checkbox_rectangle = wx.Rect(checkbox_x, checkbox_y,
                                     self._config["width_checkbox"],
                                     self._config["height_checkbox"])
        text_image_rectangle = wx.Rect(text_image_rectangle_x,
                                       text_image_rectangle_y,
                                       text_image_rectangle_width,
                                       text_image_rectangle_height)

        # draw rectangles
        self._draw_text_and_bitmap(self._Label, text_width, text_height,
                                   bitmap, image_width, image_height,
                                   drawing_area, state, gcdc)

        gcdc.SetPen(self._get_pen_element("checkbox", state))
        gc.SetBrush(self._get_brush_element("checkbox", state, gc))
        gcdc.DrawRoundedRectangle(checkbox_rectangle,
                                  self._config[f"cornerradius_checkbox_{state}"])
        
        # add support for custom check images
        # if no image specified, use drawn checkmark
        

                          
    def _handle_event(self):
        if self._Hover:
            self._Value = not self._Value
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_CHECKBOX.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
       return wx.Size(300, 60)
                                          
                                          
