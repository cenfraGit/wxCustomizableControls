"""gauge.py

wxCustomizableControls
18/dec/2024
cenfra
"""


from ._window import Window
import wx


class Gauge(Window):
    def __init__(self, parent, id=wx.ID_ANY, range=100,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.GA_HORIZONTAL, validator=wx.DefaultValidator,
                 name=wx.GaugeNameStr, config={}, **kwargs):

        # ----------------------- attributes ----------------------- #

        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        kwargs["value"] = 0
        kwargs["range"] = range
        self._Style = style

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # -------------- initialize animation values -------------- #

        self._current_values["progress"] = {"current": 0, "target": 0, "start": 0}

    def SetValue(self, value:int) -> None:
        """Sets the value of the gauge's progress.
        """
        if (value < 0) or (value > self._Range):
            raise ValueError("SetValue out of range.")
        else:
            self._Value = value
            self._handle_animation()

    def IsVertical(self) -> bool:
        return (self._Style == wx.GA_VERTICAL)

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #
        
        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # ------------------ gauge outer 'frame' ------------------ #

        gauge_rectangle = drawing_rect.Deflate(self._get_pen_current("gauge").GetWidth() // 2 + 1,
                                                self._get_pen_current("gauge").GetWidth() // 2 + 1)
        gcdc.SetPen(self._get_pen_current("gauge"))
        gc.SetBrush(self._get_brush_current("gauge", gc))
        gcdc.DrawRoundedRectangle(gauge_rectangle, self._config[f"gauge_cornerradius_{self._get_state()}"])

        # ------------------- gauge progress bar ------------------- #

        # the _get_progressbar_rectangle takes into account the range,
        # value, orientation, progressbar_startfrom value, and
        # borderwidths of both the outer frame and progressbar to
        # calculate the dimensions of the rectangle.
        progress_rectangle = self._get_progressbar_rectangle()
        
        gcdc.SetPen(self._get_pen_current("progress"))
        gc.SetBrush(self._get_brush_current("progress", gc))
        gcdc.DrawRoundedRectangle(progress_rectangle, self._config[f"progress_cornerradius_{self._get_state()}"])

        # ---------------------- mouse cursor ---------------------- #

        self._configure_cursor()
        
    def _get_progressbar_rectangle(self) -> wx.Rect:
        """Returns the rectangle representing the progressbar.
        """
        # get both gauge and progressbar info
        gauge_range = self.GetRange()
        gauge_value = self._current_values["progress"]["current"]
        gauge_size = self.GetSize()
        gauge_vertical = self.IsVertical()
        padding = (self._config[f"progress_padding_{self._get_state()}"] +
                   self._get_pen_current("progress").GetWidth() // 2 +
                   self._get_pen_current("gauge").GetWidth())

        # if the gauge style is vertical, we will use its height to
        # perform the value calculations. if its horizontal, use the
        # width.
        if gauge_vertical:
            gauge_length = gauge_size[1]
            gauge_width_sides = gauge_size[0]
        else:
            gauge_length = gauge_size[0]
            gauge_width_sides = gauge_size[1]

        # the progressbar_length is the value transformation
        progressbar_length = gauge_value * (gauge_length - 2 * padding) / gauge_range
        # the progressbar_width_sides is the width of the side of the
        # progressbar, regardless of its orientation.
        progressbar_width_sides = gauge_width_sides - 2 * padding

        # now we determine the orientation for the previous calculations
        progressbar_width = progressbar_width_sides if gauge_vertical else progressbar_length
        progressbar_height = progressbar_length if gauge_vertical else progressbar_width_sides

        # addionally, the user can specify if the progressbar starts
        # from the top or bottom (if the gauge is vertical) or left or
        # right (if the gauge is horizontal)

        if gauge_vertical:
            if self._config["progress_startfrom"] == "top":
                progressbar_x = padding
                progressbar_y = padding
            elif self._config["progress_startfrom"] == "bottom":
                progressbar_x = padding
                progressbar_y = gauge_length - progressbar_length - padding
            else:
                raise ValueError("progress_startfrom: invalid value for vertical orientation.")
        else:
            if self._config["progress_startfrom"] == "left":
                progressbar_x = padding
                progressbar_y = padding
            elif self._config["progress_startfrom"] == "right":
                progressbar_x = gauge_length - progressbar_width - padding
                progressbar_y = padding
            else:
                raise ValueError("progress_startfrom: invalid value for horizontal orientation")

        return wx.Rect(int(progressbar_x), int(progressbar_y),
                       int(progressbar_width), int(progressbar_height))

