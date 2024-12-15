"""button.py

A customizable button.

wxCustomizableControls
13/dec/2024
cenfra
"""


from .base.window import CustomizableWindow
import wx


class Button(CustomizableWindow):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator, name=wx.ButtonNameStr,
                 config={}, **kwargs):

        # control attributes
        kwargs["label"] = label

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

        # button
        button_rectangle = drawing_area.Deflate(1, 1)
        gcdc.SetPen(self._get_pen_element("button", state))
        gc.SetBrush(self._get_brush_element("button", state, gc))
        gcdc.DrawRoundedRectangle(button_rectangle, self._config[f"cornerradius_button_{state}"])

        # text
        text_width, text_height = self._get_text_dimensions(self._Label, state, gc)

        # image
        bitmap, image_width, image_height = self._get_bitmap_and_dimensions(state)

        # draw
        self._draw_text_and_bitmap(self._Label, text_width, text_height,
                                   bitmap, image_width, image_height,
                                   button_rectangle, state, gcdc)

        # set mouse cursor
        self._configure_cursor()
        
    def _handle_event(self):
        if self._Hover:
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        state = "default" if self._UseDefaults else self._get_state_as_string()
        # state = "default"
        text_width, text_height = self._get_text_dimensions(self._Label, state, gc)
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        text_image_separation = self._config[f"separation_image_{state}"]
        width, height = self._get_object_sides_dimensions(text_width, text_height,
                                                          image_width, image_height,
                                                          text_image_separation,
                                                          self._config[f"side_image_{state}"])
        # padding
        width += 2 * 10
        height += 2 * 5
        return wx.Size(int(width), int(height))
    
