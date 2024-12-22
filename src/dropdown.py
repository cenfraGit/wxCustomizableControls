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
                 config_scrolledpanel={}, **kwargs):

        wx.PopupTransientWindow.__init__(self, parent, flags)
        Window.__init__(self, parent, config=config, **kwargs)
        
        self._opening = False

        self._main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._main_sizer)

        scrolledpanel = ScrolledPanel(self, config=config_scrolledpanel)
        self._panel = scrolledpanel.GetPanel()
        self._sizer = wx.GridBagSizer()
        self._panel.SetSizer(self._sizer)
        # for i in range(10):
        #     self._sizer.Add(wx.Button(self._panel, label="test"), pos=(i, 0))
        self._sizer.Layout()
        
        self._main_sizer.Add(scrolledpanel, 1, wx.EXPAND)
        self._main_sizer.Layout()

        # -------------- initialize animation values -------------- #

        self._current_values["height"] = {"current": 0, "target": 0, "start": 0}

    def GetPanelAndSizer(self):
        return self._panel, self._sizer

    def _get_children_heights(self) -> int:
        height = 0
        for child in self._sizer.GetChildren():
            height += child.GetSize()[1]
        return height

    def setup_dropdown(self, position):
        children_heights = self._get_children_heights()
        if children_heights > 200:
            children_heights = 200
        self._current_values["height"]["target"] = children_heights + 10
        self._current_values["height"]["start"] = self._current_values["height"]["current"]
        self.Position(position, wx.Size(0, 0))
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
        """This method is called from within _window inside the
        animation timer event handler.
        """
        height = int(self._current_values["height"]["current"])
        self.SetSize(wx.Size(-1, height))
        if not self._opening and height == 0:
            self.Dismiss()
        
    def DoGetBestClientSize(self):
        return wx.Size(self.GetParent().GetSize()[0], 0)

    
