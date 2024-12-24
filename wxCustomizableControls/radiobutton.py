"""radiobutton.py

wxCustomizableControls
15/dec/2024
cenfra
"""


import builtins
from ._window import Window
import wx


class RadioButton(Window):

    groups = {} # used to keep track of radiobutton grups
    
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator,
                 name=wx.RadioButtonNameStr, config=None, **kwargs):

        # ------------------- control attributes ------------------- #
        
        kwargs["label"] = label
        kwargs["value"] = False

        # ------------------- initialize window ------------------- #

        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # ------------------- radiobutton groups ------------------- #

        # each instance of radiobuttons can create a new group by
        # having the wx.RB_GROUP style flag set. we'll check at the
        # very beginning if the new instance is creating a new group
        # and if not, we'll add it to the last created group.

        if style & wx.RB_GROUP or not RadioButton.groups:
            # create new group id and use it to create a new group
            self.group_id = builtins.id(self)
            RadioButton.groups[self.group_id] = []
        else:
            # use the id of the last created group
            self.group_id = list(RadioButton.groups.keys())[-1]

        # we then add this radiobutton instance to the correct group
        RadioButton.groups[self.group_id].append(self)

    def SetValue(self, state: bool) -> None:
        """Sets the value of the radiobutton and updates the rest of
        the group.
        """
        if state == True: # explicit
            self._deselect_radiobuttons_in_group()
        self._Value = state
        self._handle_colour_transition()
        self.Refresh()

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # --------- text, image and checkbox calculations --------- #

        text_width, text_height = self._get_text_dimensions(self._Label, gc)

        bitmap, image_width, image_height = self._get_bitmap_and_dimensions()

        # first we calculate the text label and image area dimensions
        text_image_rectangle_width, text_image_rectangle_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config["image_separation"],
            self._config["image_side"])

        # now we calculate the coordinates for the previous rectangle
        # and the radiobutton itself. we will take into consideration
        # the width of the radiobutton border.
        text_image_rectangle_x, text_image_rectangle_y, radiobutton_x, radiobutton_y = self._get_coords_object_sides(
            drawing_rect,
            text_image_rectangle_width, text_image_rectangle_height,
            self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"),
            self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"),
            self._config["radiobutton_separation"],
            self._config["radiobutton_side"])

        # ----------------------- rectangles ----------------------- #
        
        radiobutton_rectangle = wx.Rect(radiobutton_x,
                                        radiobutton_y,
                                        self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"),
                                        self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"))
        # we use deflate to automatically calculate the new top left
        # rectangle coordinates instead of doing it manually. inside
        # this new rectangle is the actual radiobutton, without border
        # width consideration.
        radiobutton_rectangle = radiobutton_rectangle.Deflate(self._get_max_value("borderwidth", "radiobutton") // 2 + 1,
                                                              self._get_max_value("borderwidth", "radiobutton") // 2 + 1)
        text_image_rectangle = wx.Rect(
            text_image_rectangle_x,
            text_image_rectangle_y,
            text_image_rectangle_width,
            text_image_rectangle_height)
        
        # ------------------- drawing rectangles ------------------- #

        # draw text label and image
        self._draw_text_and_bitmap(self._Label, text_width, text_height,
                                   bitmap, image_width, image_height,
                                   text_image_rectangle, gcdc)
        # draw radiobutton circle
        gcdc.SetPen(self._get_pen_current("radiobutton"))
        gc.SetBrush(self._get_brush_current("radiobutton", gc))
        radiobutton_center_x = radiobutton_rectangle.GetX() + radiobutton_rectangle.GetWidth() // 2
        radiobutton_center_y = radiobutton_rectangle.GetY() + radiobutton_rectangle.GetHeight() // 2
        gcdc.DrawCircle(radiobutton_center_x, radiobutton_center_y, self._config[f"radiobutton_diameter"] // 2)

        # -------------------- selection marker -------------------- #

        if self._Value:
            gcdc.SetPen(wx.TRANSPARENT_PEN)
            gc.SetBrush(self._get_brush_current("selectionmarker", gc))
            gcdc.DrawCircle(radiobutton_center_x, radiobutton_center_y, self._config[f"selectionmarker_diameter_{self._get_state()}"] // 2)

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()

    def _handle_event(self) -> None:
        if self._Hover:
            self._deselect_radiobuttons_in_group()
            self.SetValue(True)
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_RADIOBUTTON.typeId, self.GetId()))

    def _deselect_radiobuttons_in_group(self) -> None:
        for rb in RadioButton.groups[self.group_id]:
            if rb.GetValue():
                rb.SetValue(False)

    def DoGetBestClientSize(self) -> wx.Size:
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        text_width, text_height = self._get_text_dimensions(self._Label, gc)
        image_width = self._get_max_value("width", "image")
        image_height = self._get_max_value("height", "image")
        text_image_width, text_image_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config[f"image_separation"],
            self._config[f"image_side"])
        width, height = self._get_object_sides_dimensions(
            text_image_width, text_image_height,
            self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"),
            self._config["radiobutton_diameter"] + self._get_max_value("borderwidth", "radiobutton"),
            self._config["radiobutton_separation"],
            self._config["radiobutton_side"])
        # padding
        width += 5
        height += 5
        return wx.Size(int(width), int(height))
