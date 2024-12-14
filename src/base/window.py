"""window.py
"""


from .object import CustomizableObject
import wx


class CustomizableWindow(wx.Window, CustomizableObject):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name=wx.PanelNameStr, config={}):

        super().__init__(parent, id, pos, size, style|wx.NO_BORDER, name)
        CustomizableObject.__init__(self, config)

        # --------------------- window states --------------------- #

        self._Enabled = True
        self._Pressed = False
        self._Hover = False

        # ---------------------- window setup ---------------------- #

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.SetInitialSize(size)

        # ------------------------- events ------------------------- #

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.__on_erase_background)
        self.Bind(wx.EVT_ENTER_WINDOW, self.__on_enter_window)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.__on_leave_window)

    def _get_state_as_string(self) -> str:
        if not self._Enabled:
            return "disabled"
        elif self._Pressed:
            return "pressed"
        elif self._Hover:
            return "hover"
        else:
            return "default"

    def __on_erase_background(self, event) -> None:
        pass

    def __on_enter_window(self, event) -> None:
        self._Hover = True
        self.Refresh()
        event.Skip()

    def __on_leave_window(self, event) -> None:
        self._Hover = False
        self.Refresh()
        event.Skip()

    def Enable(self, enable:bool=True) -> None:
        self._Enabled = enable
        super().Enable(enable)
        self.Refresh()

    def Disable(self) -> None:
        self.Enable(False)
    
