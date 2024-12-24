"""switch.py

wxCustomizableControls
22/dec/2024
cenfra
"""


from copy import copy
from ._window import Window
import wx


class Switch(Window):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator,
                 name=wx.CheckBoxNameStr, config=None, **kwargs):

        # ------------------- control attributes ------------------- #
        
        kwargs["label"] = label
        kwargs["value"] = False

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

        # -------------- initialize animation values -------------- #

        self._current_values["switchmarker"] = {"current": 0, "target": 0, "start": 0}

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #

        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # --------- text, image and switch calculations --------- #
        
        text_width, text_height = self._get_text_dimensions(self._Label, gc)

        bitmap, image_width, image_height = self._get_bitmap_and_dimensions()

        # first we calculate the text label and image area dimensions
        text_image_rectangle_width, text_image_rectangle_height = self._get_object_sides_dimensions(
            text_width, text_height,
            image_width, image_height,
            self._config["image_separation"],
            self._config["image_side"])

        # now we calculate the coordinates for the previous rectangle
        # and the switch itself. we will take into consideration the
        # width of the switch border.
        text_image_rectangle_x, text_image_rectangle_y, switch_x, switch_y = self._get_coords_object_sides(
            drawing_rect,
            text_image_rectangle_width, text_image_rectangle_height,
            self._config["switch_width"] + self._get_max_value("borderwidth", "switch"),
            self._config["switch_height"] + self._get_max_value("borderwidth", "switch"),
            self._config["switch_separation"],
            self._config["switch_side"])

        # ----------------------- rectangles ----------------------- #

        switch_rectangle = wx.Rect(switch_x,
                                   switch_y,
                                   self._config["switch_width"] + self._get_max_value("borderwidth", "switch"),
                                   self._config["switch_height"] + self._get_max_value("borderwidth", "switch"))
        # we use deflate to automatically calculate the new top left
        # rectangle coordinates instead of doing it manually. this new
        # rectangle is the actual switch, without border width
        # consideration.
        switch_rectangle = switch_rectangle.Deflate(self._get_max_value("borderwidth", "switch") // 2 + 1,
                                                    self._get_max_value("borderwidth", "switch") // 2 + 1)
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
        # draw switch rectangle
        gcdc.SetPen(self._get_pen_current("switch"))
        gc.SetBrush(self._get_brush_current("switch", gc))
        gcdc.DrawRoundedRectangle(switch_rectangle,
                                  self._config[f"switch_cornerradius_{self._get_state()}"])

        # -------------------- selection marker -------------------- #

        # the animation_range value will be scaled (between 0 and 1)
        # depending on the current animation value.
        animation_range = (switch_rectangle.GetWidth() -
                           2 * self._config["selectionmarker_horizontalpadding"] -
                           self._get_pen_current("selectionmarker").GetWidth() -
                           self._config["selectionmarker_width"])

        animation_progress_scaled = self._current_values["switchmarker"]["current"] * animation_range


        selectionmarker_x = int(switch_rectangle.GetX() + self._config["selectionmarker_horizontalpadding"] + animation_progress_scaled)

        selectionmarker_y = (switch_rectangle.GetY() +
                             switch_rectangle.GetHeight() // 2 -
                             self._config["selectionmarker_height"] // 2)

        gcdc.SetPen(self._get_pen_current("selectionmarker"))
        gc.SetBrush(self._get_brush_current("selectionmarker", gc))

        width = self._config["selectionmarker_width"]
        height = self._config["selectionmarker_height"]

        if self._config["selectionmarker_rounded"]:
            gcdc.DrawEllipse(selectionmarker_x, selectionmarker_y, width, height)
        else:
            gcdc.DrawRectangle(selectionmarker_x, selectionmarker_y, width, height)

        # ---------------------- mouse cursor ---------------------- #
        
        self._configure_cursor()

    def _get_switch_marker_coord(self):
        if self._Value: 
            selectionmarker_x_scaler = 1         
        else:
            selectionmarker_x_scaler = 0
        return selectionmarker_x_scaler
                          
    def _handle_event(self) -> None:
        if self._Hover:
            self._Value = not self._Value
            wx.PostEvent(self, wx.PyCommandEvent(wx.EVT_CHECKBOX.typeId, self.GetId()))
            self._handle_animation()

    def SetValue(self, value:int) -> None:
        self._Value = value
        self._handle_animation()

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
            self._config["switch_width"] + self._get_max_value("borderwidth", "switch"),
            self._config["switch_height"] + self._get_max_value("borderwidth", "switch"),
            self._config["switch_separation"],
            self._config["switch_side"])
        # padding
        width += 5
        height += 5
        return wx.Size(int(width), int(height))
    
