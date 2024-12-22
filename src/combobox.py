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
                 name=wx.ComboBoxNameStr, config={},
                 config_dropdown={}, config_button={},
                 config_scrolledpanel={}, **kwargs):

        # ------------------- control attributes ------------------- #

        kwargs["value"] = value
        kwargs["choices"] = choices

        # self._ControlChoices = []

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

        # --------------------- text and image --------------------- #

        text_width, text_height = self._get_text_dimensions(self._Value, gc)

        bitmap, image_width, image_height = self._get_bitmap_and_dimensions()

        self._draw_text_and_bitmap(self._Value, text_width,
                                   text_height, bitmap, image_width,
                                   image_height, combobox_rectangle,
                                   gcdc)

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
        dropdown.Dismiss()

    def DoGetBestClientSize(self):
        return wx.Size(150, 50)

