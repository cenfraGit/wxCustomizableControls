"""scrolledpanel.py

wxCustomizableControls
19/dec/2024
cenfra
"""


from ._window import Window
from wx.lib.scrolledpanel import ScrolledPanel as wxScrolledPanel
import wx


class ScrollBar(Window):
    def __init__(self, parent, scrollbar_type, scrolled_panel,
                 id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, name=wx.ScrollBarNameStr,
                 config={}, **kwargs):

        # ----------------------- attributes ----------------------- #

        self._scrollbar_type = scrollbar_type # vertical or horizontal
        self._scrolled_panel = scrolled_panel
        self._scrollbar_rectangle = wx.Rect(0, 0, 0, 0)

        # ------------------- initialize window ------------------- #

        super().__init__(parent, id, pos, size, 0, name, config, **kwargs)

        # ------------------------- events ------------------------- #
        
        self.Unbind(wx.EVT_ENTER_WINDOW, handler=self._on_enter_window)


    def _on_paint(self, event: wx.Event) -> None:

        scrollbar_window_is_vertical = self._scrollbar_type == "vertical"

        # ------- get scrolledpanel client and virtual size ------- #

        # the client size is the size of the panel we see, the virtual
        # size is the size of the "complete" panel. we need this data
        # to calculate the size of the scrollbars
        client_size = self._scrolled_panel.GetClientSize()
        virtual_size = self._scrolled_panel.GetVirtualSize()

        # using the event object data, we determine the real and
        # visible sizes depending on the scrollbar orientation
        real = virtual_size[1] if scrollbar_window_is_vertical else virtual_size[0]
        visible = client_size[1] if scrollbar_window_is_vertical else client_size[0]

        # now we calculate the proportion of the corresponding
        # scrollbar
        bar_length = visible / real

        # we will use this value to check if there is need to scroll.
        # if (bar_length >= 1.0):
        #     scrollbar_window.SetSize(wx.Size(0, 0))
        # wxPizza??????????????????????????????        

        # and now we use this value to scale the dimension
        # corresponding to the orientation of the scrollbar window (if
        # its a vertical scrollbar, we will scale the height of its
        # window. if its a horizontal scrollbar, we will scale its
        # width)
        scrollbar_window_client_size = self.GetClientSize()
        scrollbar_window_length = scrollbar_window_client_size[1] if scrollbar_window_is_vertical else scrollbar_window_client_size[0]
        
        bar_length *= scrollbar_window_length

        # now that we have the scrollbar thumb dimensions, we need to
        # determine its starting x and y coordinate. to do this, we
        # need to know up to which point the user has scrolled.

        # we need to translate the scrolled logical coordinates to
        # device ones, then scale these to match our view of the
        # scrollbar. CalcScrolledPosition translates logical
        # coordinates to device ones.
        view_from_start = self._scrolled_panel.CalcScrolledPosition(0, 0)
        distance_from_start = view_from_start[1] if scrollbar_window_is_vertical else view_from_start[0]

        # now we scale this distance to our view, the same thing we
        # did to get the original bar length.
        start_of_bar = -distance_from_start * visible / real

        # now that we have the length value and start coordinates of
        # the scrollbar, we can draw it.

        # ------------ drawing contexts and background ------------ #
        
        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()

        # -------------------- scrollbar track -------------------- #
        
        gcdc.SetPen(self._get_pen_current("track"))
        gc.SetBrush(self._get_brush_current("track", gc))
        gcdc.DrawRectangle(drawing_rect)

        # -------------------- scrollbar thumb -------------------- #

        # we determine on which dimensions the previous calculations
        # will apply to
        padding = (self._config[f"thumb_padding_{self._get_state()}"] +
                   self._get_pen_current("thumb").GetWidth() // 2)
        if scrollbar_window_is_vertical:
            # real rectangle
            scrollbar_thumb_x = 0
            scrollbar_thumb_y = int(start_of_bar)
            scrollbar_thumb_width = self._config[f"thumb_width_{self._get_state()}"]
            scrollbar_thumb_height = int(bar_length)
            # drawn rectangle
            scrollbar_thumb_drawn_x = scrollbar_thumb_x + padding
            scrollbar_thumb_drawn_y = scrollbar_thumb_y
            scrollbar_thumb_drawn_width = scrollbar_thumb_width - 2 * padding
            scrollbar_thumb_drawn_height = scrollbar_thumb_height
        else:
            # real rectangle
            scrollbar_thumb_x = int(start_of_bar)
            scrollbar_thumb_y = 0
            scrollbar_thumb_width = int(bar_length)
            scrollbar_thumb_height = self._config[f"thumb_width_{self._get_state()}"]
            # drawn rectangle
            scrollbar_thumb_drawn_x = scrollbar_thumb_x + padding
            scrollbar_thumb_drawn_y = scrollbar_thumb_y
            scrollbar_thumb_drawn_width = scrollbar_thumb_width - 2 * padding
            scrollbar_thumb_drawn_height = scrollbar_thumb_height

        # we created two rectangles because one is used to check if
        # the user clicked on the sidebar thumb and the other one is
        # used to draw the sidebar. they are basically the same,
        # except the drawn one has paddings. this is done because, if
        # by chance the user clicked on the padding space between the
        # track and the thumb and start dragging, they might expect
        # the sidebar to move. (is this actually useful?)
        scrollbar_thumb_rectangle = wx.Rect(
            scrollbar_thumb_x, scrollbar_thumb_y,
            scrollbar_thumb_width, scrollbar_thumb_height)
        scrollbar_thumb_drawn_rectangle = wx.Rect(
            scrollbar_thumb_drawn_x, scrollbar_thumb_drawn_y,
            scrollbar_thumb_drawn_width, scrollbar_thumb_drawn_height)

        # save the real rectangle data
        self._scrollbar_rectangle = scrollbar_thumb_rectangle

        gcdc.DrawRoundedRectangle(
            scrollbar_thumb_drawn_rectangle,
            self._config[f"thumb_cornerradius_{self._get_state()}"])

    def _on_left_down(self, event: wx.MouseEvent) -> None:
        """Checks if the user clicked on the scrollbar and captures
        mouse.
        """        
        x, y = event.GetPosition()

        clicked_on_scrollbar = self._scrollbar_rectangle.Contains(x, y)

        if not clicked_on_scrollbar:
            event.Skip()
            return

        self._Pressed = True
        self._handle_colour_transition()
        self.CaptureMouse()
        event.Skip()
        
    def _on_left_up(self, event: wx.MouseEvent) -> None:
        """Releases mouse capture.
        """        
        if not self.HasCapture():
            event.Skip()
            return

        self._Pressed = False
        self._Hover = False
        self._handle_colour_transition()
        self.ReleaseMouse()
        event.Skip()

    def _on_leave_window(self, event: wx.MouseEvent) -> None:
        """If mouse leaves window but has capture, does nothing. If it
        has no capture, resets state values.
        """
        
        if self.HasCapture():
            event.Skip()
            return

        self._Pressed = False
        self._Hover = False
        self._handle_colour_transition()
        event.Skip()

        


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
        self._scrollbar_padding = 5

        # initialize rectangles to check clicks
        self._scrollbar_vertical_rectangle = wx.Rect(0, 0, 0, 0)
        self._scrollbar_horizontal_rectangle = wx.Rect(0, 0, 0, 0)

        self.__scrollbar_window_vertical = ScrollBar(self, "vertical", self.__scrolled_panel,
                                                     size=wx.Size(self._scrollbar_width, -1), config=config)
        self.__scrollbar_window_horizontal = ScrollBar(self, "horizontal", self.__scrolled_panel,
                                                       size=wx.Size(-1, self._scrollbar_width), config=config)

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

        # ------------------------- events ------------------------- #

        self.__scrolled_panel.Bind(wx.EVT_MOUSEWHEEL, self._on_mousewheel)

    def GetPanel(self):
        return self.__scrolled_panel

    def _on_motion(self, event: wx.MouseEvent) -> None:
        
        # --------------------- get event data --------------------- #
        
        scrollbar_window = event.GetEventObject()
        scrollbar_window_is_vertical = scrollbar_window == self.__scrollbar_window_vertical

    def _on_mousewheel(self, event: wx.Event) -> None:
        pass

    def _handle_event(self) -> None:
        pass
        
        
