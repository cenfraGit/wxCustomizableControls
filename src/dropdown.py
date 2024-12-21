"""dropdown.py

A dropdown scrolled panel used for comboboxes and menubars.

wxCustomizableControls
20/dec/2024
cenfra
"""


from ._window import Window
from .scrolledpanel import ScrolledPanel
import wx


class DropDown(wx.PopupTransientWindow, Window):
    def __init__(self, parent, flags=wx.BORDER_NONE, config={},
                 **kwargs):

        wx.PopupTransientWindow.__init__(self, parent, flags)
        Window.__init__(self, parent, config=config, **kwargs)

        self._main_panel = wx.Panel(self)
        self._main_panel.SetBackgroundColour(wx.GREEN)
        self._main_sizer = wx.BoxSizer(wx.VERTICAL)
        self._main_panel.SetSizer(self._main_sizer)

        self._pos = wx.Point(0, 0)

        # self._scrolled_panel = ScrolledPanel(self._main_panel)

        # self.Bind(wx.EVT_PAINT, self._on_paint)

        # -------------- initialize animation values -------------- #

        self._current_values["height"] = {"current": 0, "target": 0, "start": 0}

    def SetupAnimation(self, pos):
        self._current_values["height"]["target"] = 300
        self._current_values["height"]["start"] = self._current_values["height"]["current"]

        self.Position(pos, wx.Size(0, 0))
        self.Popup()
        self._start_timer_animation()

    def _on_paint(self, event: wx.Event) -> None:
        self.UpdateDropdown()

    def UpdateDropdown(self):
        self.SetSize(wx.Size(-1, int(self._current_values["height"]["current"])))
        
    def DoGetBestClientSize(self):
        return wx.Size(300, 300)
        

        
