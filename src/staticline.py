"""staticline.py

wxCustomizableControls
16/dec/2024
cenfra
"""


from ._window import Window
import wx


class StaticLine(Window):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LI_HORIZONTAL,
                 name=wx.StaticLineNameStr, config={}, **kwargs):

        # ----------------------- attributes ----------------------- #

        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        self.style = style

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

        # ----------------------- staticline ----------------------- #

        gcdc.SetPen(self._get_pen_current("staticline"))

        vertical_midpoint = drawing_rect.GetX() + drawing_rect.GetHeight() // 2
        horizontal_midpoint = drawing_rect.GetX() + drawing_rect.GetWidth() // 2

        if self.style == wx.LI_HORIZONTAL:
            gcdc.DrawLine(0, vertical_midpoint, drawing_rect.GetWidth(), vertical_midpoint)
        elif self.style == wx.LI_VERTICAL:
            gcdc.DrawLine(horizontal_midpoint, 0, horizontal_midpoint, drawing_rect.GetHeight())

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()

