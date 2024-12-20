"""scrolledpanel.py

wxCustomizableControls
19/dec/2024
cenfra
"""


from ._window import Window
from wx.lib.scrolledpanel import ScrolledPanel as wxScrolledPanel
import wx


class ScrolledPanel(Window):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, name=wx.PanelNameStr, config={},
                 **kwargs):

        # the idea is to have a wx scrolled panel inside this window,
        # hide its native scrollbars, and then draw our own scrollbars
        # to the sides.

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, 0, name, config, **kwargs)

        # ----------------- set up scrolled panel ----------------- #

        self._scroll_x = True
        self._scroll_y = True
        self._rate_x = 20
        self._rate_y = 20

        # create the scrolled panel and set up its scrolling values
        self.__scrolled_panel = wxScrolledPanel(self)
        self.__scrolled_panel.SetupScrolling(self._scroll_x, self._scroll_y,
                                             self._rate_x, self._rate_y)
        # now we hide its scrollbars
        # self.__scrolled_panel.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_NEVER)
        self.__scrolled_panel.SetBackgroundColour(wx.YELLOW)

        # ------------------- set up scrollbars ------------------- #

        self._scrollbar_width = 30

        self.__scrollbar_window_vertical = wx.Window(self, size=wx.Size(self._scrollbar_width, -1))
        self.__scrollbar_window_horizontal = wx.Window(self, size=wx.Size(-1, self._scrollbar_width))

        self.__scrollbar_window_vertical.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.__scrollbar_window_horizontal.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        # ---------------------- add to sizer ---------------------- #

        self.__sizer = wx.GridBagSizer()
        self.SetSizer(self.__sizer)
        self.__sizer.Add(self.__scrolled_panel, pos=(0, 0), flag=wx.EXPAND)
        self.__sizer.Add(self.__scrollbar_window_vertical, pos=(0, 1), flag=wx.EXPAND)
        self.__sizer.Add(self.__scrollbar_window_horizontal, pos=(1, 0), flag=wx.EXPAND)

        self.__sizer.AddGrowableCol(0, 1)
        self.__sizer.AddGrowableRow(0, 1)

        self.__sizer.Layout()
        
        

        

    def _on_paint(self, event: wx.Event) -> None:
        pass

    def _handle_event(self) -> None:
        pass
        
        
