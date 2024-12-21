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
        
        self._opening = False
        
        self._main_panel = wx.Panel(self)
        self._main_panel.SetSize(wx.Size(300, 300))
        self._main_panel.SetBackgroundColour(wx.GREEN)
        self._main_sizer = wx.BoxSizer(wx.VERTICAL)
        self._main_panel.SetSizer(self._main_sizer)

        self._pos = wx.Point(0, 0)

        # self._scrolled_panel = ScrolledPanel(self._main_panel)


        # -------------- initialize animation values -------------- #

        self._current_values["height"] = {"current": 0, "target": 0, "start": 0}

    def SetupAnimation(self, pos):
        self._current_values["height"]["target"] = 300
        self._current_values["height"]["start"] = self._current_values["height"]["current"]

        self.Position(pos, wx.Size(0, 0))
        self.Popup()
        self._start_timer_animation()
        self._opening = True

    def OnDismiss(self):
        self._current_values["height"]["target"] = 0
        self._current_values["height"]["start"] = self._current_values["height"]["current"]
        self.Popup()
        self._start_timer_animation()
        self._opening = False

    def _update_dropdown(self):
        height = int(self._current_values["height"]["current"])
        self.SetSize(wx.Size(-1, height))
        if not self._opening and height == 0:
            self.Dismiss()
        
    def DoGetBestClientSize(self):
        return wx.Size(300, 0)

    
