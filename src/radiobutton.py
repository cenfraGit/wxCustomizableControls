"""radiobutton.py

A customizable radiobutton.

wxCustomizableControls
15/dec/2024
cenfra
"""



import builtins
from .base.window import CustomizableWindow
import wx


class RadioButton(CustomizableWindow):

    groups = {} # used to keep track of radiobutton grups
    
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator,
                 name=wx.RadioButtonNameStr, config={}, **kwargs):

        # control attributes
        kwargs["label"] = label
        kwargs["value"] = False

        # initialize window
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # check if starts a new group
        if style & wx.RB_GROUP or not RadioButton.groups:
            # start new group
            self.group_id = builtins.id(self)
            RadioButton.groups[self.group_id] = []
        else:
            self.group_id = list(RadioButton.groups.keys())[-1]

        RadioButton.groups[self.group_id].append(self)

    def _on_paint(self, event: wx.Event) -> None:
        state = "default" if self._UseDefaults else self._get_state_as_string()

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        # drawing area
        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gcdc.SetBrush(wx.Brush(self.GetParent().GetBackgroundColour()))
        gcdc.DrawRectangle(drawing_rect)

        # text
        text_width, text_height = self._get_text_dimensions(self._Label, state, gc)

        # image
        bitmap, image_width, image_height = self._get_bitmap_and_dimensions(state)

        # we need to calculate the dimensions of an imaginary
        # rectangle containing both the text label and the image
        text_image_rectangle_width, text_image_rectangle_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config["image_separation"],
            self._config["image_side"])

        # now we calculate the coordinates for the previous rectangle
        # and the checkbox itself
        text_image_rectangle_x, text_image_rectangle_y, radiobutton_x, radiobutton_y = self._get_coords_object_sides(
            drawing_rect,
            text_image_rectangle_width, text_image_rectangle_height,
            self._config["radiobutton_diameter"], self._config["radiobutton_diameter"],
            self._config["radiobutton_separation"],
            self._config["radiobutton_side"])

        # create rectangles
        radiobutton_rectangle = wx.Rect(radiobutton_x, radiobutton_y,
                                        self._config["radiobutton_diameter"],
                                        self._config["radiobutton_diameter"])
        text_image_rectangle = wx.Rect(
            text_image_rectangle_x,
            text_image_rectangle_y,
            text_image_rectangle_width,
            text_image_rectangle_height)
        
        # draw text label and image 
        self._draw_text_and_bitmap(self._Label, text_width, text_height,
                                   bitmap, image_width, image_height,
                                   text_image_rectangle, gcdc)
        # draw radiobutton circle
        gcdc.SetPen(self._get_pen_element("radiobutton", state))
        gc.SetBrush(self._get_brush_element("radiobutton", state, gc))

        radiobutton_center_x = radiobutton_rectangle.GetX() + radiobutton_rectangle.GetWidth() // 2
        radiobutton_center_y = radiobutton_rectangle.GetY() + radiobutton_rectangle.GetHeight() // 2
        gcdc.DrawCircle(radiobutton_center_x, radiobutton_center_y, self._config[f"radiobutton_diameter"] // 2)
        
        # draw selection marker if radiobutton is selected
        if self._Value:
            gcdc.SetPen(wx.TRANSPARENT_PEN)
            gc.SetBrush(self._get_brush_element("selectionmarker", state, gc))
            gcdc.DrawCircle(radiobutton_center_x, radiobutton_center_y, self._config[f"selectionmarker_diameter_{state}"] // 2)

        # set mouse cursor
        self._configure_cursor()

    def SetValue(self, state: bool) -> None:
        """Overriding this method was necessary because we need to
        update the currently active radiobutton in the group.
        """
        if state == True: # explicit
            self._deselect_radiobuttons_in_group()
        self._Value = state
        self.Refresh()

    def _deselect_radiobuttons_in_group(self) -> None:
        for rb in RadioButton.groups[self.group_id]:
            if rb.GetValue():
                rb.SetValue(False)
    
    def _handle_event(self) -> None:
        if self._Hover:
            self._deselect_radiobuttons_in_group()
            self.SetValue(True)
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_RADIOBUTTON.typeId, self.GetId()))

    def DoGetBestClientSize(self) -> wx.Size:
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        state = "default" if self._UseDefaults else self._get_state_as_string()
        # state = "default"
        text_width, text_height = self._get_text_dimensions(self._Label, state, gc)
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        text_image_width, text_image_height = self._get_object_sides_dimensions(text_width, text_height,
                                                                                image_width, image_height,
                                                                                self._config[f"image_separation"],
                                                                                self._config[f"image_side"])
        width, height = self._get_object_sides_dimensions(text_image_width, text_image_height,
                                                          self._config["radiobutton_diameter"], self._config["radiobutton_diameter"],
                                                          self._config["radiobutton_separation"],
                                                          self._config["radiobutton_side"])
        # padding
        width += 2 * 10
        height += 2 * 5
        return wx.Size(int(width), int(height))
