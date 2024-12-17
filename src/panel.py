"""panel.py

A customizable panel.

wxCustomizableControls
15/dec/2024
cenfra
"""


from ._window import Window
import wx


class Panel(Window):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name=wx.PanelNameStr, config={},
                 **kwargs):

        # ----------------------- attributes ----------------------- #

        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _handle_event(self) -> None:
        return None

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # ------------------------- panel ------------------------- #

        panel_rectangle = drawing_rect.Deflate(1, 1)
        gcdc.SetPen(self._get_pen_current("panel"))
        gc.SetBrush(self._get_brush_current("panel", gc))
        gcdc.DrawRoundedRectangle(panel_rectangle, self._config[f"panel_cornerradius_{self._get_state()}"])

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()

