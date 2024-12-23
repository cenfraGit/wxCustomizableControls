"""combobox.py

wxCustomizableControls
21/dec/2024
cenfra
"""


from ._window import Window
from .dropdown import DropDown
from .button import Button
import wx


class ComboBox(Window):
    def __init__(self, parent, id=wx.ID_ANY, value="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 choices=[], style=0, validator=wx.DefaultValidator,
                 name=wx.ComboBoxNameStr, config=None,
                 config_dropdown=None, config_button=None,
                 config_scrolledpanel=None, **kwargs):

        # ------------------- control attributes ------------------- #

        kwargs["value"] = value
        kwargs["choices"] = choices

        # this attribute will help us keep track of the state of the
        # dropdown so that we can send the correct events.
        self._dropdown_active = False

        self._config_dropdown = config_dropdown
        self._config_button = config_button
        self._config_scrolledpanel = config_scrolledpanel

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #
        
        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # ------------------------ combobox ------------------------ #

        combobox_rectangle = drawing_rect.Deflate(self._get_pen_current("combobox").GetWidth() // 2 + 1,
                                                self._get_pen_current("combobox").GetWidth() // 2 + 1)
        gcdc.SetPen(self._get_pen_current("combobox"))
        gc.SetBrush(self._get_brush_current("combobox", gc))
        gcdc.DrawRoundedRectangle(combobox_rectangle, self._config[f"combobox_cornerradius_{self._get_state()}"])

        # ----------------- text and arrow coords ----------------- #

        text_width, text_height = self._get_text_dimensions(self._Value, gc)

        text_x, text_y, arrow_x, arrow_y = self._get_coords_object_sides(
            drawing_rect,
            text_width, text_height,
            self._config["arrow_width"],
            self._config["arrow_height"],
            self._config["arrow_separation"],
            self._config["arrow_side"])

        # ----------------------- draw text ----------------------- #

        gcdc.DrawText(self._Value, text_x, text_y)

        # ----------------------- draw arrow ----------------------- #

        arrow_rectangle = wx.Rect(arrow_x, arrow_y, self._config["arrow_width"], self._config["arrow_height"])

        gcdc.SetPen(self._get_pen_current("arrow"))
        gc.SetBrush(wx.TRANSPARENT_BRUSH)
        
        path: wx.GraphicsPath = gc.CreatePath()
        path.MoveToPoint(arrow_rectangle.GetX(), arrow_rectangle.GetY())
        path.AddLineToPoint(arrow_rectangle.GetX() + arrow_rectangle.GetWidth() // 2,
                            arrow_rectangle.GetY() + arrow_rectangle.GetHeight())
        path.AddLineToPoint(arrow_rectangle.GetX() + arrow_rectangle.GetWidth(), arrow_rectangle.GetY())
        gc.StrokePath(path)

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()

    def _handle_event(self) -> None:
        if self._Hover:
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_COMBOBOX.typeId, self.GetId()))
            if not self._dropdown_active:
                wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_COMBOBOX_DROPDOWN.typeId, self.GetId()))
                self._dropdown_active = True
            elif self._dropdown_active:
                wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_COMBOBOX_CLOSEUP.typeId, self.GetId()))
                self._dropdown_active = False

            self._display_dropdown()
                
    def _display_dropdown(self) -> None:
        dropdown = DropDown(self, config=self._config_dropdown,
                            config_scrolledpanel=self._config_scrolledpanel)
        self._display_choices_in_dropdown(dropdown)
        position = self.ClientToScreen(wx.Point(0, 0))
        size = self.GetSize()
        position[1] += size[1]
        dropdown.setup_dropdown(position)

    def _display_choices_in_dropdown(self, dropdown: DropDown) -> None:
        panel, sizer = dropdown.GetPanelAndSizer()
        self._button_choices = []
        if self._Choices:
            for index, choice in enumerate(self._Choices):
                button_choice = Button(panel, label=choice, config=self._config_button)
                self._button_choices.append(button_choice)
                
                sizer.Add(button_choice, pos=(index, 0), flag=wx.EXPAND)
            sizer.AddGrowableCol(0, 1)

        for button in self._button_choices:
            button.Bind(wx.EVT_BUTTON, lambda event: self._set_value_click(event, dropdown))

    def _set_value_click(self, event: wx.Event, dropdown: DropDown):
        # button event configured incorrectly?
        # button = event.GetEventObject()
        button = wx.Window.FindWindowById(event.GetId())
        self.SetValue(button.GetLabel())
        dropdown.close()
        self._Hover = False
        self._Pressed = False
        self._handle_colour_transition()

    def DoGetBestClientSize(self):
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        choices_lengths = [len(choice) for choice in self._Choices]
        longest_choice_string = self._Choices[choices_lengths.index(max(choices_lengths))]
        text_width, text_height = self._get_text_dimensions(longest_choice_string, gc)
        arrow_width, arrow_height = self._config["arrow_width"], self._config["arrow_height"]
        width, height = self._get_object_sides_dimensions(text_width, text_height,
                                                          arrow_width, arrow_height,
                                                          self._config[f"arrow_separation"],
                                                          self._config[f"arrow_side"])
        # add border widths
        width += 2 * self._get_max_value("borderwidth", "combobox")
        height += 2 * self._get_max_value("borderwidth", "combobox")
        # padding
        width += 2 * 10
        height += 2 * 5
        return wx.Size(int(width), int(height))

