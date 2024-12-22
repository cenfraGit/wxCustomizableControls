"""staticbox.py

A customizable staticbox.

wxCustomizableControls
15/dec/2024
cenfra
"""


from ._window import Window
import wx


class StaticBox(Window):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 name=wx.StaticBoxNameStr, config={}, **kwargs):

        # ----------------------- attributes ----------------------- #
        
        kwargs["label"] = label
        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # --------------------- content panel --------------------- #

        # to facilitate the use of the staticbox, we will create a
        # panel inside ourselves in which the actual staticbox content
        # will be in. the staticbox label and border lines will not
        # overlap with the content panel, so we must add some sort of
        # padding between the staticbox drawing panel and the content
        # panel.

        # first we get the text label height to offset the content
        # panel from the top
        dc = wx.ScreenDC()
        font, _ = self._get_font()
        dc.SetFont(font)
        _, self._text_height = dc.GetTextExtent(self._Label)

        # create content panel
        self.__Panel = wx.Panel(self)
        # self.__Panel.SetBackgroundColour(self.GetParent().GetBackgroundColour())
        self.__Panel.SetBackgroundColour(wx.YELLOW)
        # redirect panel events to ourselves
        self.__Panel.Bind(wx.EVT_ENTER_WINDOW, self._on_enter_window)
        self.__Panel.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave_window)
        self.__Panel.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)
        self.__Panel.Bind(wx.EVT_LEFT_UP, self._on_left_up)

        # create a sizer to outselves and then add the content panel
        # with paddings
        self.__Sizer = wx.BoxSizer(wx.VERTICAL)
        self.__Sizer.AddSpacer(self._text_height)
        self.__Sizer.Add(self.__Panel, proportion=1,
                         flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,
                         border=self._get_max_value("borderwidth", "staticbox") * 2)
        self.SetSizer(self.__Sizer)

    def GetPanel(self) -> wx.Panel:
        """Returns the reference to the staticbox's content panel.
        """
        return self.__Panel

    def _handle_event(self) -> None:
        return None

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # ------------------ staticbox rectangle ------------------ #

        gcdc.SetPen(self._get_pen_current("staticbox"))
        gc.SetBrush(wx.TRANSPARENT_BRUSH)
        
        padding_sides = self._config[f"staticbox_borderwidth_{self._get_state()}"]
        padding_top = self._text_height // 2

        gcdc.DrawRoundedRectangle(drawing_rect.GetX() + padding_sides,
                                  drawing_rect.GetY() + padding_top,
                                  drawing_rect.GetWidth() - 2 * padding_sides,
                                  drawing_rect.GetHeight() - padding_top - padding_sides,
                                  self._config[f"staticbox_cornerradius_{self._get_state()}"])

        # ----------------------- text label ----------------------- #
        
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gc.SetFont(*self._get_font())

        text_width, text_height = gcdc.GetTextExtent(self._Label)

        text_center_x = drawing_rect.GetWidth() // 2 - (text_width // 2)
        text_center_y = padding_top - text_height // 2

        # draw label background (rectangle)
        text_lateral_offset = 7
        gcdc.DrawRectangle(text_center_x - text_lateral_offset,
                           text_center_y,
                           text_width + 2 * text_lateral_offset,
                           text_height)
        # draw text label
        gcdc.DrawText(self._Label, text_center_x, text_center_y)

        # ------------- make content panel update size ------------- #

        self.Layout()
