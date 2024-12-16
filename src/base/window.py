"""window.py

The base class for all customizable windows.

wxCustomizableControls
13/dec/2024
cenfra
"""


from .object import CustomizableObject
import wx


class CustomizableWindow(wx.Window, CustomizableObject):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name=wx.PanelNameStr,
                 config={}, **kwargs):

        super().__init__(parent, id, pos, size, style|wx.NO_BORDER, name)
        CustomizableObject.__init__(self, config)

        # --------------------- window states --------------------- #

        # these states are used to draw the window/control appearance
        # accordingly.

        self._Enabled = True
        self._Pressed = False
        self._Hover = False

        # ------------------- control attributes ------------------- #

        # these attributes are not always present. if we intend to use
        # them we must first assign them a value inside kwargs before
        # initializing CustomizableWindow.

        self._Label = kwargs.get("label", None)
        self._Value = kwargs.get("value", None)
        self._Choices = kwargs.get("choices", None)

        self._ActOnPress = kwargs.get("act_on_press", False)
        self._UseDefaults = kwargs.get("use_defaults", False)

        # ---------------------- window setup ---------------------- #

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.SetInitialSize(size)

        # ------------------------- events ------------------------- #

        self.Bind(wx.EVT_PAINT, self._on_paint)

        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda _: None)
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_enter_window)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave_window)

        self.Bind(wx.EVT_LEFT_DCLICK, self._on_left_down)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_left_up)

    def SetLabel(self, label: str) -> None:
        self._Label = label
        self.Refresh()

    def GetLabel(self) -> str:
        return self._Label

    def SetValue(self, state: bool) -> None:
        self._Value = state
        self.Refresh()

    def GetValue(self):
        return self._Value

    def _get_state_as_string(self) -> str:
        if not self._Enabled:
            return "disabled"
        elif self._Pressed:
            return "pressed"
        elif self._Hover:
            return "hover"
        else:
            return "default"

    def _configure_cursor(self):
        state = self._get_state_as_string()
        if state != "default":
            self.SetCursor(self._get_cursor(self._config[f"mousecursor_{state}"]))

    def _on_paint(self, event: wx.Event) -> None:
        raise NotImplementedError("_on_paint")

    def _on_enter_window(self, event: wx.Event) -> None:
        self._Hover = True
        self.Refresh()
        event.Skip()

    def _on_leave_window(self, event: wx.Event) -> None:
        self._Hover = False
        self.Refresh()
        event.Skip()

    def _on_left_down(self, event: wx.Event) -> None:
        if not self._Pressed:
            self.CaptureMouse()
            self._Pressed = True
            if self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _on_left_up(self, event: wx.Event) -> None:
        if self._Pressed:
            self.ReleaseMouse()
            self._Pressed = False
            if not self._ActOnPress:
                self._handle_event()
            self.Refresh()
        event.Skip()

    def _handle_event(self) -> None:
        raise NotImplementedError("_handle_event")

    def Enable(self, enable:bool=True) -> None:
        self._Enabled = enable
        super().Enable(enable)
        self.Refresh()

    def Disable(self) -> None:
        self.Enable(False)
    
