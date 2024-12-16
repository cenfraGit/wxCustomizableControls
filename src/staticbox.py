"""staticbox.py

A customizable staticbox.

wxCustomizableControls
15/dec/2024
cenfra
"""


from .panel import Panel
from .base.window import CustomizableWindow
import wx


class StaticBox(CustomizableWindow):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 name=wx.StaticBoxNameStr, config={}, **kwargs):

        # attributes
        kwargs["label"] = label
        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        # initialize window
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # to facilitate the use of the staticbox, we will create a
        # panel inside ourselves in which the actual staticbox content
        # will be in. the staticbox label and border lines will not
        # overlap with the content panel, so we must add some sort of
        # padding between the staticbox drawing panel and the content
        # panel.

        # first we get the text label height to offset the content
        # panel from the top
        dc = wx.ScreenDC()
        dc.SetFont(self._get_font("default"))
        _, self._text_height = dc.GetTextExtent(self._Label)

        # create content panel
        self.__Panel = Panel(self)
        self.__Panel.SetBackgroundColour(self.GetParent().GetBackgroundColour())
        self.__Panel.SetBackgroundColour(wx.YELLOW)

        # create a sizer to outselves and then add the content panel
        # with paddings
        self.__Sizer = wx.BoxSizer(wx.VERTICAL)
        self.__Sizer.AddSpacer(self._text_height)
        self.__Sizer.Add(self.__Panel, proportion=1,
                         flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,
                         border=self._get_pen_element("staticbox", "default").GetWidth() * 2)
        self.SetSizer(self.__Sizer)
        
