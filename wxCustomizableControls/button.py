"""button.py

wxCustomizableControls
13/dec/2024
cenfra
"""


from ._window import Window
import wx


class Button(Window):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator, name=wx.ButtonNameStr,
                 config=None, **kwargs):

        # ------------------- control attributes ------------------- #
        
        kwargs["label"] = label

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

        # ------------------------- button ------------------------- #

        button_rectangle = drawing_rect.Deflate(self._get_pen_current("button").GetWidth() // 2 + 1,
                                                self._get_pen_current("button").GetWidth() // 2 + 1)
        gcdc.SetPen(self._get_pen_current("button"))
        gc.SetBrush(self._get_brush_current("button", gc))
        gcdc.DrawRoundedRectangle(button_rectangle, self._config[f"button_cornerradius_{self._get_state()}"])

        # --------------------- text and image --------------------- #

        text_width, text_height = self._get_text_dimensions(self._Label, gc)

        bitmap, image_width, image_height = self._get_bitmap_and_dimensions()

        self._draw_text_and_bitmap(self._Label, text_width,
                                   text_height, bitmap, image_width,
                                   image_height, button_rectangle,
                                   gcdc)

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()
        
    def _handle_event(self) -> None:
        if self._Hover:
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        text_width, text_height = self._get_text_dimensions(self._Label, gc)
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        width, height = self._get_object_sides_dimensions(text_width, text_height,
                                                          image_width, image_height,
                                                          self._config[f"image_separation"],
                                                          self._config[f"image_side"])
        # add border widths
        width += 2 * self._get_max_value("borderwidth", "button")
        height += 2 * self._get_max_value("borderwidth", "button")
        # padding
        width += 2 * 10
        height += 2 * 5
        return wx.Size(int(width), int(height))
    
