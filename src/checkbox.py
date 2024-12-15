"""checkbox.py

A customizable checkbox.

wxCustomizableControls
14/dec/2024
cenfra
"""


from .base.window import CustomizableWindow
import wx


class CheckBox(CustomizableWindow):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator, name=wx.CheckBoxNameStr, config={},
                 **kwargs):

        # control attributes
        kwargs["label"] = label
        kwargs["value"] = False

        # initialize window
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _on_paint(self, event: wx.Event) -> None:
        state = "default" if self._UseDefaults else self._get_state_as_string()

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        # drawing area
        drawing_area: wx.Rect = self.GetClientRect()
        gcdc.SetPen(self._get_pen_element("drawingarea", state))
        gc.SetBrush(self._get_brush_element("drawingarea", state, gc))
        gcdc.DrawRectangle(drawing_area)

        

    def _handle_event(self):
        if self._Hover:
            self._Value = not self._Value
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_CHECKBOX.typeId, self.GetId()))
        
