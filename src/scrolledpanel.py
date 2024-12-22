"""scrolledpanel.py

wxCustomizableControls
19/dec/2024
cenfra
"""


from ._window import Window
from wx.lib.scrolledpanel import ScrolledPanel as wxScrolledPanel
import wx


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

        self._scroll_x = self._config["scroll_x"]
        self._scroll_y = self._config["scroll_y"]
        self._rate_x = self._config["rate_x"]
        self._rate_y = self._config["rate_y"]

        # create the scrolled panel and set up its scrolling values
        self._scrolled_panel = wxScrolledPanel(self)
        self._scrolled_panel.SetupScrolling(self._scroll_x,
                                             self._scroll_y,
                                             self._rate_x,
                                             self._rate_y)
        # now we hide its scrollbars
        self._scrolled_panel.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_NEVER)
        self._scrolled_panel.SetBackgroundColour(wx.YELLOW)

        # ------------------- set up scrollbars ------------------- #

        self._scrollbar_window_vertical_is_shown = True
        self._scrollbar_window_horizontal_is_shown = True

        scrollbar_width = self._config["thumb_width"]
        self._scrollbar_window_vertical = ScrollBar(self, "vertical", self._scrolled_panel,
                                                    size=wx.Size(scrollbar_width, -1), config=config)
        self._scrollbar_window_horizontal = ScrollBar(self, "horizontal", self._scrolled_panel,
                                                      size=wx.Size(-1, scrollbar_width), config=config)

        self._scrollbar_window_vertical.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self._scrollbar_window_horizontal.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        # ---------------------- add to sizer ---------------------- #

        self._sizer = wx.GridBagSizer()
        self.SetSizer(self._sizer)
        self._sizer.Add(self._scrolled_panel, pos=(0, 0), flag=wx.EXPAND)
        self._sizer.Add(self._scrollbar_window_vertical, pos=(0, 1), flag=wx.EXPAND)
        self._sizer.Add(self._scrollbar_window_horizontal, pos=(1, 0), flag=wx.EXPAND)

        self._sizer.AddGrowableCol(0, 1)
        self._sizer.AddGrowableRow(0, 1)

        self.UpdateScrollbars()
        
        self._sizer.Layout()

        # ------------------------- events ------------------------- #

        self._scrolled_panel.Bind(wx.EVT_MOUSEWHEEL, self._on_mousewheel)

    def GetPanel(self):
        return self._scrolled_panel

    def UpdateScrollbars(self):
        """Should be called when scroll_x or scroll_y was changed.
        """
        if self._config["scroll_y"] and not self._scrollbar_window_vertical_is_shown:
            self._show_scrollbar("vertical", True)
        elif not self._config["scroll_y"] and self._scrollbar_window_vertical_is_shown:
            self._show_scrollbar("vertical", False)

        if self._config["scroll_x"] and not self._scrollbar_window_horizontal_is_shown:
            self._show_scrollbar("horizontal", True)
        elif not self._config["scroll_x"] and self._scrollbar_window_horizontal_is_shown:
            self._show_scrollbar("horizontal", False)

    def _show_scrollbar(self, scrollbar: str, show: bool) -> None:
        if show:
            if scrollbar == "vertical" and not self._scrollbar_window_vertical_is_shown:
                self._sizer.Add(self._scrollbar_window_vertical, pos=(0, 1), flag=wx.EXPAND)
                self._scrollbar_window_vertical.Show()
                self._scrollbar_window_vertical_is_shown = True
            elif scrollbar == "horizontal" and not self._scrollbar_window_horizontal_is_shown:
                self._sizer.Add(self._scrollbar_window_horizontal, pos=(1, 0), flag=wx.EXPAND)
                self._scrollbar_window_horizontal.Show()
                self._scrollbar_window_horizontal_is_shown = True
        else:
            if scrollbar == "vertical" and self._scrollbar_window_vertical_is_shown:
                self._sizer.Detach(self._scrollbar_window_vertical)
                self._scrollbar_window_vertical.Hide()
                self._scrollbar_window_vertical_is_shown = False
            elif scrollbar == "horizontal" and self._scrollbar_window_horizontal_is_shown:
                self._sizer.Detach(self._scrollbar_window_horizontal)
                self._scrollbar_window_horizontal.Hide()
                self._scrollbar_window_horizontal_is_shown = False

    def _on_mousewheel(self, event: wx.MouseEvent) -> None:

        current_view = self._scrolled_panel.GetViewStart()
        wheel_axis = event.GetWheelAxis()
        wheel_rotation = event.GetWheelRotation()

        if wheel_axis == wx.MOUSE_WHEEL_VERTICAL:
            if not self._config[f"scroll_y"]:
                return
            x = current_view[0]
            y = current_view[1] - (wheel_rotation / 8)
            self._scrollbar_window_vertical.Refresh()
        else:
            if not self._config[f"scroll_x"]:
                return
            x = current_view[0] + (wheel_rotation / 8)
            y = current_view[1]
            self._scrollbar_window_horizontal.Refresh()
        self._scrolled_panel.Scroll(int(x), int(y))

    def _on_size(self, event: wx.Event):
        """Determines if scrollbars need to be drawn or not.
        """

        client_size = self._scrolled_panel.GetClientSize()
        virtual_size = self._scrolled_panel.GetVirtualSize()

        real_vertical, visible_vertical = virtual_size[1], client_size[1]
        real_horizontal, visible_horizontal = virtual_size[0], client_size[0]

        vertical_proportion = visible_vertical / real_vertical
        horizontal_proportion = visible_horizontal / real_horizontal

        if (vertical_proportion >= 1.0) and self._scrollbar_window_vertical_is_shown:
            self._show_scrollbar("vertical", False)
        elif (vertical_proportion < 1.0) and not self._scrollbar_window_vertical_is_shown:
            self._show_scrollbar("vertical", True)

        if (horizontal_proportion >= 1.0) and self._scrollbar_window_horizontal_is_shown:
            self._show_scrollbar("horizontal", False)
        elif (horizontal_proportion < 1.0) and not self._scrollbar_window_horizontal_is_shown:
            self._show_scrollbar("horizontal", True)

        self._sizer.Layout()

        event.Skip()
        
    
class ScrollBar(Window):
    def __init__(self, parent, scrollbar_type, scrolled_panel,
                 id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, name=wx.ScrollBarNameStr,
                 config={}, **kwargs):

        # ----------------------- attributes ----------------------- #

        self._scrollbar_type = scrollbar_type # vertical or horizontal
        self._scrolled_panel = scrolled_panel
        self._scrollbar_thumb_rectangle = wx.Rect(0, 0, 0, 0)
        self._scrollbar_thumb_length = 0
        self._scrollbar_thumb_start = 0
        self._scrollbar_click_offset = 0

        # ------------------- initialize window ------------------- #

        super().__init__(parent, id, pos, size, 0, name, config, **kwargs)

        # ------------------------- events ------------------------- #
        
        self.Unbind(wx.EVT_ENTER_WINDOW, handler=self._on_enter_window)
        self.Bind(wx.EVT_MOTION, self._on_motion)

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

        # and now we use this value to scale the dimension
        # corresponding to the orientation of the scrollbar window (if
        # its a vertical scrollbar, we will scale the height of its
        # window. if its a horizontal scrollbar, we will scale its
        # width)
        scrollbar_window_client_size = self.GetClientSize()
        scrollbar_window_length = scrollbar_window_client_size[1] if scrollbar_window_is_vertical else scrollbar_window_client_size[0]
        
        bar_length *= scrollbar_window_length

        self._scrollbar_thumb_length = bar_length

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

        self._scrollbar_thumb_start = start_of_bar

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
            scrollbar_thumb_width = self._config[f"thumb_width"]
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
            scrollbar_thumb_height = self._config[f"thumb_width"]
            # drawn rectangle
            scrollbar_thumb_drawn_x = scrollbar_thumb_x
            scrollbar_thumb_drawn_y = scrollbar_thumb_y + padding
            scrollbar_thumb_drawn_width = scrollbar_thumb_width
            scrollbar_thumb_drawn_height = scrollbar_thumb_height - 2 * padding

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
        self._scrollbar_thumb_rectangle = scrollbar_thumb_rectangle

        gcdc.DrawRoundedRectangle(
            scrollbar_thumb_drawn_rectangle,
            self._config[f"thumb_cornerradius_{self._get_state()}"])

    def _on_left_down(self, event: wx.MouseEvent) -> None:
        """Checks if the user clicked on the scrollbar and captures
        mouse.
        """        
        x, y = event.GetPosition()

        clicked_on_scrollbar = self._scrollbar_thumb_rectangle.Contains(x, y)

        if not clicked_on_scrollbar:
            event.Skip()
            return

        variable = y if (self._scrollbar_type == "vertical") else x
        self._scrollbar_click_offset = self._scrollbar_thumb_start - variable

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

    def _on_motion(self, event: wx.MouseEvent) -> None:

        # --------------------- get event data --------------------- #

        x, y = event.GetPosition()
        scrollbar_window_is_vertical = self._scrollbar_type == "vertical"

        if self.HasCapture():

            units_x, units_y = self._scrolled_panel.GetScrollPixelsPerUnit()

            virtual_size_scrolled_panel = self._scrolled_panel.GetVirtualSize()
            client_size_scrollbar_window = self.GetClientSize()
            
            if scrollbar_window_is_vertical:
                if not self._config["scroll_y"]:
                    event.Skip()
                    return
                virtual_scrolled_panel = virtual_size_scrolled_panel[1]
                client_scrollbar_window = client_size_scrollbar_window[1]
                scrollbar_click = y + self._scrollbar_click_offset
                focus = units_y
            else:
                virtual_scrolled_panel = virtual_size_scrolled_panel[0]
                client_scrollbar_window = client_size_scrollbar_window[0]
                scrollbar_click = x + self._scrollbar_click_offset
                focus = units_x

            transform = (self._scrollbar_thumb_length * virtual_scrolled_panel / client_scrollbar_window)

            # the very bottom cannot be scrolled down to

            scroll_range = virtual_scrolled_panel - transform

            click_range = int(client_scrollbar_window - self._scrollbar_thumb_length)

            click_range = 0.01 if click_range == 0 else click_range

            percentage = scrollbar_click / click_range

            value = percentage * scroll_range / focus

            if scrollbar_window_is_vertical:
                self._scrolled_panel.Scroll(-1, int(value))
            else:
                self._scrolled_panel.Scroll(int(value), -1)

            self.Refresh()

        else:
            if self._scrollbar_thumb_rectangle.Contains(x, y):
                self._Hover = True
            else:
                self._Hover = False
            self._handle_colour_transition()
            
        event.Skip()
        
