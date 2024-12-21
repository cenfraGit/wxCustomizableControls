"""combobox.py

wxCustomizableControls
21/dec/2024
cenfra
"""


from ._window import Window
from .dropdown import DropDown
import wx


class ComboBox(Window):
    def __init__(self, parent, id=wx.ID_ANY, value="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 choices=[], style=0, validator=wx.DefaultValidator,
                 name=wx.ComboBoxNameStr, config={}, **kwargs):

        # ------------------- control attributes ------------------- #

        kwargs["value"] = value

        # this attribute will help us keep track of the state of the
        # dropdown so that we can send the correct events.
        self._dropdown_active = False

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
                
    def _display_dropdown(self):
        dropdown_style = {
            "colourtransition_ms_default": 0,
            "colourtransition_ms_hover": 0,
            "colourtransition_ms_pressed": 0,
            "animation_ms": self._config["animation_ms"],
        }

        dropdown = DropDown(self, config=dropdown_style)
        position = self.ClientToScreen(wx.Point(0, 0))
        size = self.GetSize()
        position[1] += size[1]
        dropdown.setup_dropdown(position)

    def DoGetBestClientSize(self):
        return wx.Size(150, 50)
                

        
