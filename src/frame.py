"""frame.py

wxCustomizableControls
18/dec/2024
cenfra
"""


import wx


class Frame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, name=wx.FrameNameStr, **kwargs):
        
        super().__init__(parent, id, pos=pos, size=size, style=wx.NO_BORDER, name=name)

        self._resizing = False

        self.Bind(wx.EVT_MOTION, self._on_motion)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_left_up)

        self.SetSize((400, 400))

    def _on_motion(self, event: wx.MouseEvent) -> None:
        if self._resizing and event.Dragging():
            _current_pos = event.GetPosition()
            _current_size = self.GetSize()

            difference = _current_pos[0] - self._starting_pos[0]

            #print( * 100 / _current_size[0])

            # convert difference
            # 400 - 100%
            # difference - x%
            
            #print(resize_amount)
            _current_size[0] = _current_pos[0]
            #_current_size[1] = _current_size[1]
            self.SetSize(_current_size)
            

    def _on_left_down(self, event):
        mouse_position = event.GetPosition()
        frame_size = self.GetSize()
        tolerance = 0.03
        horizontal_in_range = True if ((1 - tolerance) * frame_size[0] < mouse_position[0] < (1 + tolerance) * frame_size[0]) else False

        if horizontal_in_range:
            self._resizing = True
            self._starting_pos = mouse_position
        else:
            self._resizing = False

    def _on_left_up(self, event):
        self._resizing = False
        if self.HasCapture():
            self.ReleaseMouse()

if __name__ == "__main__":
    app = wx.App()
    f = Frame(None)
    f.Show()
    app.MainLoop()
        
