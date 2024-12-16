"""panel.py

A customizable panel.

wxCustomizableControls
15/dec/2024
cenfra
"""


from .base.window import CustomizableWindow
import wx


class Panel(CustomizableWindow):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name=wx.PanelNameStr, config={},
                 **kwargs):

        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        # initialize window
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _handle_event(self) -> None:
        return None

    def _on_paint(self, event: wx.Event) -> None:
        state = "default" if self._UseDefaults else self._get_state_as_string()

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        # drawing area
        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gcdc.SetBrush(wx.Brush(self.GetParent().GetBackgroundColour()))
        gcdc.DrawRectangle(drawing_rect)

        panel_rectangle = drawing_rect.Deflate(1, 1)
        gcdc.SetPen(self._get_pen_element("panel", state))
        gc.SetBrush(self._get_brush_element("panel", state, gc))
        gcdc.DrawRoundedRectangle(panel_rectangle, self._config[f"panel_cornerradius_{state}"])

        # set mouse cursor
        self._configure_cursor()

