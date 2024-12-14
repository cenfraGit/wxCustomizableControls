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

        # ------------------- control attributes ------------------- #

        kwargs["label"] = label

        # ------------------- initialize window ------------------- #

        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # ------------------------- events ------------------------- #

        self.Bind(wx.EVT_PAINT, self.__on_paint)
        self.Bind(wx.EVT_LEFT_DCLICK, self.__on_left_down)
        self.Bind(wx.EVT_LEFT_DOWN, self.__on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.__on_left_up)
        
    def __on_paint(self, event: wx.Event) -> None:
        """Handles the drawing of the control.
        """

        if self._UseDefaults:
            state = "default"
        else:
            state = self._get_state_as_string()
        
        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        # drawing area
        drawing_area: wx.Rect = self.GetClientRect()
        gcdc.SetPen(self._get_pen_element("drawingarea", state))
        gc.SetBrush(self._get_brush_element("drawingarea", state, gc))
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

    def __on_left_down(self, event) -> None:
        if not self._Pressed:
            self.CaptureMouse()
            self._Pressed = True
            self.Refresh()
            if self._ActOnPress:
                self.__post_event()
        event.Skip()

    def __on_left_up(self, event) -> None:
        if self._Pressed:
            self.ReleaseMouse()
            self._Pressed = False
            self.Refresh()
            if not self._ActOnPress:
                self.__post_event()
        event.Skip()

    def __post_event(self):
        if self._Hover:
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
        return wx.Size(300, 300)
