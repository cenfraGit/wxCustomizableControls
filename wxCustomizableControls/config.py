"""config.py

wxCustomizableControls
23/dec/2024
cenfra
"""


class Config:
    def __init__(self, **kwargs):

        # ----------------------- animation ----------------------- #

        self.colourtransition_ms_default = kwargs.get("colourtransition_ms_default", 200)
        self.colourtransition_ms_hover = kwargs.get("colourtransition_ms_hover", 200)
        self.colourtransition_ms_pressed = kwargs.get("colourtransition_ms_pressed", 200)

        self.animation_ms = kwargs.get("animation_ms", 200)

        # ------------------------- cursor ------------------------- #

        self.mousecursor_hover = kwargs.get("mousecursor_hover", "arrow")
        self.mousecursor_pressed = kwargs.get("mousecursor_pressed", "arrow")
        self.mousecursor_disabled = kwargs.get("mousecursor_disabled", "arrow")

        # -------------------------- font -------------------------- #

        self.fontfacename_default = kwargs.get("fontfacename_default", "Verdana")
        self.fontfacename_hover = kwargs.get("fontfacename_hover", "Verdana")
        self.fontfacename_pressed = kwargs.get("fontfacename_pressed", "Verdana")
        self.fontfacename_disabled = kwargs.get("fontfacename_disabled", "Verdana")

        self.fontcolour_default = kwargs.get("fontcolour_default", (0, 0, 0))
        self.fontcolour_hover = kwargs.get("fontcolour_hover", (0, 0, 0))
        self.fontcolour_pressed = kwargs.get("fontcolour_pressed", (0, 0, 0))
        self.fontcolour_disabled = kwargs.get("fontcolour_disabled", (0, 0, 0))

        self.fontsize_default = kwargs.get("fontsize_default", 12)
        self.fontsize_hover = kwargs.get("fontsize_hover", 12)
        self.fontsize_pressed = kwargs.get("fontsize_pressed", 12)
        self.fontsize_disabled = kwargs.get("fontsize_disabled", 12)

        self.fontstyle_default = kwargs.get("fontstyle_default", "normal")
        self.fontstyle_hover = kwargs.get("fontstyle_hover", "normal")
        self.fontstyle_pressed = kwargs.get("fontstyle_pressed", "normal")
        self.fontstyle_disabled = kwargs.get("fontstyle_disabled", "normal")

        self.fontweight_default = kwargs.get("fontweight_default", "normal")
        self.fontweight_hover = kwargs.get("fontweight_hover", "normal")
        self.fontweight_pressed = kwargs.get("fontweight_pressed", "normal")
        self.fontweight_disabled = kwargs.get("fontweight_disabled", "normal")

        # ------------------------- images ------------------------- #

        self.image_path_default = kwargs.get("image_path_default", "")
        self.image_path_hover = kwargs.get("image_path_hover", "")
        self.image_path_pressed = kwargs.get("image_path_pressed", "")
        self.image_path_disabled = kwargs.get("image_path_disabled", "")

        self.image_width_default = kwargs.get("image_width_default", 0)
        self.image_width_hover = kwargs.get("image_width_hover", 0)
        self.image_width_pressed = kwargs.get("image_width_pressed", 0)
        self.image_width_disabled = kwargs.get("image_width_disabled", 0)

        self.image_height_default = kwargs.get("image_height_default", 0)
        self.image_height_hover = kwargs.get("image_height_hover", 0)
        self.image_height_pressed = kwargs.get("image_height_pressed", 0)
        self.image_height_disabled = kwargs.get("image_height_disabled", 0)

        self.image_channels_default = kwargs.get("image_channels_default", (1.0, 1.0, 1.0, 1.0))
        self.image_channels_hover = kwargs.get("image_channels_hover", (1.0, 1.0, 1.0, 1.0))
        self.image_channels_pressed = kwargs.get("image_channels_pressed", (1.0, 1.0, 1.0, 1.0))
        self.image_channels_disabled = kwargs.get("image_channels_disabled", (1.0, 1.0, 1.0, 1.0))

        self.image_separation = kwargs.get("image_separation", 10)
        self.image_side = kwargs.get("image_side", "right")

        # -------------------- selection marker -------------------- #

        self.selectionmarker_rounded = kwargs.get("selectionmarker_rounded", True)
        self.selectionmarker_width = kwargs.get("selectionmarker_width", 15)
        self.selectionmarker_height = kwargs.get("selectionmarker_height", 15)
        self.selectionmarker_horizontalpadding = kwargs.get("selectionmarker_horizontalpadding", 4)

        self.selectionmarker_diameter_default = kwargs.get("selectionmarker_diameter_default", 8)
        self.selectionmarker_diameter_hover = kwargs.get("selectionmarker_diameter_hover", 8)
        self.selectionmarker_diameter_pressed = kwargs.get("selectionmarker_diameter_pressed", 8)
        self.selectionmarker_diameter_disabled = kwargs.get("selectionmarker_diameter_disabled", 8)

        self.selectionmarker_backgroundcolour_default = kwargs.get("selectionmarker_backgroundcolour_default", (173, 173, 173))
        self.selectionmarker_backgroundcolour_hover = kwargs.get("selectionmarker_backgroundcolour_hover", (173, 173, 173))
        self.selectionmarker_backgroundcolour_pressed = kwargs.get("selectionmarker_backgroundcolour_pressed", (173, 173, 173))
        self.selectionmarker_backgroundcolour_disabled = kwargs.get("selectionmarker_backgroundcolour_disabled", (0, 0, 0))

        self.selectionmarker_backgroundstyle_default = kwargs.get("selectionmarker_backgroundstyle_default", "solid")
        self.selectionmarker_backgroundstyle_hover = kwargs.get("selectionmarker_backgroundstyle_hover", "solid")
        self.selectionmarker_backgroundstyle_pressed = kwargs.get("selectionmarker_backgroundstyle_pressed", "solid")
        self.selectionmarker_backgroundstyle_disabled = kwargs.get("selectionmarker_backgroundstyle_disabled", "solid")

        self.selectionmarker_bordercolour_default = kwargs.get("selectionmarker_bordercolour_default", (173, 173, 173))
        self.selectionmarker_bordercolour_hover = kwargs.get("selectionmarker_bordercolour_hover", (0, 120, 215))
        self.selectionmarker_bordercolour_pressed = kwargs.get("selectionmarker_bordercolour_pressed", (0, 84, 153))
        self.selectionmarker_bordercolour_disabled = kwargs.get("selectionmarker_bordercolour_disabled", (0, 0, 0))

        self.selectionmarker_borderwidth_default = kwargs.get("selectionmarker_borderwidth_default", 2)
        self.selectionmarker_borderwidth_hover = kwargs.get("selectionmarker_borderwidth_hover", 2)
        self.selectionmarker_borderwidth_pressed = kwargs.get("selectionmarker_borderwidth_pressed", 2)
        self.selectionmarker_borderwidth_disabled = kwargs.get("selectionmarker_borderwidth_disabled", 2)

        self.selectionmarker_borderstyle_default = kwargs.get("selectionmarker_borderstyle_default", "solid")
        self.selectionmarker_borderstyle_hover = kwargs.get("selectionmarker_borderstyle_hover", "solid")
        self.selectionmarker_borderstyle_pressed = kwargs.get("selectionmarker_borderstyle_pressed", "solid")
        self.selectionmarker_borderstyle_disabled = kwargs.get("selectionmarker_borderstyle_disabled", "solid")

        # --------- active (checkbox, radiobutton, switch) --------- #

        self.active_backgroundcolour_default = kwargs.get("active_backgroundcolour_default", (52, 60, 180))
        self.active_backgroundcolour_hover = kwargs.get("active_backgroundcolour_hover", (52, 72, 200))
        self.active_backgroundcolour_pressed = kwargs.get("active_backgroundcolour_pressed", (52, 60, 140))
        self.active_backgroundcolour_disabled = kwargs.get("active_backgroundcolour_disabled", (0, 0, 0))

        self.active_backgroundstyle_default = kwargs.get("active_backgroundstyle_default", "solid")
        self.active_backgroundstyle_hover = kwargs.get("active_backgroundstyle_hover", "solid")
        self.active_backgroundstyle_pressed = kwargs.get("active_backgroundstyle_pressed", "solid")
        self.active_backgroundstyle_disabled = kwargs.get("active_backgroundstyle_disabled", "solid")

        self.active_bordercolour_default = kwargs.get("active_bordercolour_default", (40, 45, 131))
        self.active_bordercolour_hover = kwargs.get("active_bordercolour_hover", (40, 45, 131))
        self.active_bordercolour_pressed = kwargs.get("active_bordercolour_pressed", (40, 45, 131))
        self.active_bordercolour_disabled = kwargs.get("active_bordercolour_disabled", (40, 45, 131))

        self.active_borderwidth_default = kwargs.get("active_borderwidth_default", 2)
        self.active_borderwidth_hover = kwargs.get("active_borderwidth_hover", 2)
        self.active_borderwidth_pressed = kwargs.get("active_borderwidth_pressed", 2)
        self.active_borderwidth_disabled = kwargs.get("active_borderwidth_disabled", 2)

        self.active_borderstyle_default = kwargs.get("active_borderstyle_default", "solid")
        self.active_borderstyle_hover = kwargs.get("active_borderstyle_hover", "solid")
        self.active_borderstyle_pressed = kwargs.get("active_borderstyle_pressed", "solid")
        self.active_borderstyle_disabled = kwargs.get("active_borderstyle_disabled", "solid")

        self.active_cornerradius_default = kwargs.get("active_cornerradius_default", 0)
        self.active_cornerradius_hover = kwargs.get("active_cornerradius_hover", 0)
        self.active_cornerradius_pressed = kwargs.get("active_cornerradius_pressed", 0)
        self.active_cornerradius_disabled = kwargs.get("active_cornerradius_disabled", 0)

        # ------------------------- button ------------------------- #

        self.button_backgroundcolour_default = kwargs.get("button_backgroundcolour_default", (225, 225, 225))
        self.button_backgroundcolour_hover = kwargs.get("button_backgroundcolour_hover", (229, 241, 251))
        self.button_backgroundcolour_pressed = kwargs.get("button_backgroundcolour_pressed", (204, 228, 247))
        self.button_backgroundcolour_disabled = kwargs.get("button_backgroundcolour_disabled", (179, 179, 179))

        self.button_backgroundstyle_default = kwargs.get("button_backgroundstyle_default", "solid")
        self.button_backgroundstyle_hover = kwargs.get("button_backgroundstyle_hover", "solid")
        self.button_backgroundstyle_pressed = kwargs.get("button_backgroundstyle_pressed", "solid")
        self.button_backgroundstyle_disabled = kwargs.get("button_backgroundstyle_disabled", "solid")

        self.button_bordercolour_default = kwargs.get("button_bordercolour_default", (173, 173, 173))
        self.button_bordercolour_hover = kwargs.get("button_bordercolour_hover", (0, 120, 215))
        self.button_bordercolour_pressed = kwargs.get("button_bordercolour_pressed", (0, 84, 153))
        self.button_bordercolour_disabled = kwargs.get("button_bordercolour_disabled", (0, 0, 0))

        self.button_borderwidth_default = kwargs.get("button_borderwidth_default", 2)
        self.button_borderwidth_hover = kwargs.get("button_borderwidth_hover", 2)
        self.button_borderwidth_pressed = kwargs.get("button_borderwidth_pressed", 2)
        self.button_borderwidth_disabled = kwargs.get("button_borderwidth_disabled", 0)

        self.button_borderstyle_default = kwargs.get("button_borderstyle_default", "solid")
        self.button_borderstyle_hover = kwargs.get("button_borderstyle_hover", "solid")
        self.button_borderstyle_pressed = kwargs.get("button_borderstyle_pressed", "solid")
        self.button_borderstyle_disabled = kwargs.get("button_borderstyle_disabled", "solid")

        self.button_cornerradius_default = kwargs.get("button_cornerradius_default", 0)
        self.button_cornerradius_hover = kwargs.get("button_cornerradius_hover", 0)
        self.button_cornerradius_pressed = kwargs.get("button_cornerradius_pressed", 0)
        self.button_cornerradius_disabled = kwargs.get("button_cornerradius_disabled", 0)

        # ------------------------ checkbox ------------------------ #

        self.checkbox_width = kwargs.get("checkbox_width", 20)
        self.checkbox_height = kwargs.get("checkbox_heght", 20)
        self.checkbox_separation = kwargs.get("checkbox_separation", 5)
        self.checkbox_side = kwargs.get("checkbox_side", "left")

        self.checkbox_backgroundcolour_default = kwargs.get("checkbox_backgroundcolour_default", (255, 255, 255))
        self.checkbox_backgroundcolour_hover = kwargs.get("checkbox_backgroundcolour_hover", (229, 241, 251))
        self.checkbox_backgroundcolour_pressed = kwargs.get("checkbox_backgroundcolour_pressed", (204, 228, 247))
        self.checkbox_backgroundcolour_disabled = kwargs.get("checkbox_backgroundcolour_disabled", (0, 0, 0))

        self.checkbox_backgroundstyle_default = kwargs.get("checkbox_backgroundstyle_default", "solid")
        self.checkbox_backgroundstyle_hover = kwargs.get("checkbox_backgroundstyle_hover", "solid")
        self.checkbox_backgroundstyle_pressed = kwargs.get("checkbox_backgroundstyle_pressed", "solid")
        self.checkbox_backgroundstyle_disabled = kwargs.get("checkbox_backgroundstyle_disabled", "solid")

        self.checkbox_bordercolour_default = kwargs.get("checkbox_bordercolour_default", (173, 173, 173))
        self.checkbox_bordercolour_hover = kwargs.get("checkbox_bordercolour_hover", (0, 120, 215))
        self.checkbox_bordercolour_pressed = kwargs.get("checkbox_bordercolour_pressed", (0, 84, 153))
        self.checkbox_bordercolour_disabled = kwargs.get("checkbox_bordercolour_disabled", (0, 0, 0))

        self.checkbox_borderwidth_default = kwargs.get("checkbox_borderwidth_default", 2)
        self.checkbox_borderwidth_hover = kwargs.get("checkbox_borderwidth_hover", 2)
        self.checkbox_borderwidth_pressed = kwargs.get("checkbox_borderwidth_pressed", 2)
        self.checkbox_borderwidth_disabled = kwargs.get("checkbox_borderwidth_disabled", 0)

        self.checkbox_borderstyle_default = kwargs.get("checkbox_borderstyle_default", "solid")
        self.checkbox_borderstyle_hover = kwargs.get("checkbox_borderstyle_hover", "solid")
        self.checkbox_borderstyle_pressed = kwargs.get("checkbox_borderstyle_pressed", "solid")
        self.checkbox_borderstyle_disabled = kwargs.get("checkbox_borderstyle_disabled", "solid")

        self.checkbox_cornerradius_default = kwargs.get("checkbox_cornerradius_default", 0)
        self.checkbox_cornerradius_hover = kwargs.get("checkbox_cornerradius_hover", 0)
        self.checkbox_cornerradius_pressed = kwargs.get("checkbox_cornerradius_pressed", 0)
        self.checkbox_cornerradius_disabled = kwargs.get("checkbox_cornerradius_disabled", 0)

        # ------------------------- switch ------------------------- #

        self.switch_width = kwargs.get("switch_width", 60)
        self.switch_height = kwargs.get("switch_heght", 30)
        self.switch_separation = kwargs.get("switch_separation", 5)
        self.switch_side = kwargs.get("switch_side", "left")

        self.switch_backgroundcolour_default = kwargs.get("switch_backgroundcolour_default", (225, 225, 225))
        self.switch_backgroundcolour_hover = kwargs.get("switch_backgroundcolour_hover", (229, 241, 251))
        self.switch_backgroundcolour_pressed = kwargs.get("switch_backgroundcolour_pressed", (204, 228, 247))
        self.switch_backgroundcolour_disabled = kwargs.get("switch_backgroundcolour_disabled", (0, 0, 0))

        self.switch_backgroundstyle_default = kwargs.get("switch_backgroundstyle_default", "solid")
        self.switch_backgroundstyle_hover = kwargs.get("switch_backgroundstyle_hover", "solid")
        self.switch_backgroundstyle_pressed = kwargs.get("switch_backgroundstyle_pressed", "solid")
        self.switch_backgroundstyle_disabled = kwargs.get("switch_backgroundstyle_disabled", "solid")

        self.switch_bordercolour_default = kwargs.get("switch_bordercolour_default", (173, 173, 173))
        self.switch_bordercolour_hover = kwargs.get("switch_bordercolour_hover", (0, 120, 215))
        self.switch_bordercolour_pressed = kwargs.get("switch_bordercolour_pressed", (0, 84, 153))
        self.switch_bordercolour_disabled = kwargs.get("switch_bordercolour_disabled", (0, 0, 0))

        self.switch_borderwidth_default = kwargs.get("switch_borderwidth_default", 2)
        self.switch_borderwidth_hover = kwargs.get("switch_borderwidth_hover", 2)
        self.switch_borderwidth_pressed = kwargs.get("switch_borderwidth_pressed", 2)
        self.switch_borderwidth_disabled = kwargs.get("switch_borderwidth_disabled", 2)

        self.switch_borderstyle_default = kwargs.get("switch_borderstyle_default", "solid")
        self.switch_borderstyle_hover = kwargs.get("switch_borderstyle_hover", "solid")
        self.switch_borderstyle_pressed = kwargs.get("switch_borderstyle_pressed", "solid")
        self.switch_borderstyle_disabled = kwargs.get("switch_borderstyle_disabled", "solid")

        self.switch_cornerradius_default = kwargs.get("switch_cornerradius_default", 0)
        self.switch_cornerradius_hover = kwargs.get("switch_cornerradius_hover", 0)
        self.switch_cornerradius_pressed = kwargs.get("switch_cornerradius_pressed", 0)
        self.switch_cornerradius_disabled = kwargs.get("switch_cornerradius_disabled", 0)
        
        # ---------------------- radiobutton ---------------------- #

        self.radiobutton_diameter = kwargs.get("radiobutton_diameter", 20)
        self.radiobutton_separation = kwargs.get("radiobutton_separation", 10)
        self.radiobutton_side = kwargs.get("radiobutton_side", "left")

        self.radiobutton_backgroundcolour_default = kwargs.get("radiobutton_backgroundcolour_default", (225, 225, 225))
        self.radiobutton_backgroundcolour_hover = kwargs.get("radiobutton_backgroundcolour_hover", (229, 241, 251))
        self.radiobutton_backgroundcolour_pressed = kwargs.get("radiobutton_backgroundcolour_pressed", (204, 228, 247))
        self.radiobutton_backgroundcolour_disabled = kwargs.get("radiobutton_backgroundcolour_disabled", (0, 0, 0))

        self.radiobutton_backgroundstyle_default = kwargs.get("radiobutton_backgroundstyle_default", "solid")
        self.radiobutton_backgroundstyle_hover = kwargs.get("radiobutton_backgroundstyle_hover", "solid")
        self.radiobutton_backgroundstyle_pressed = kwargs.get("radiobutton_backgroundstyle_pressed", "solid")
        self.radiobutton_backgroundstyle_disabled = kwargs.get("radiobutton_backgroundstyle_disabled", "solid")

        self.radiobutton_bordercolour_default = kwargs.get("radiobutton_bordercolour_default", (173, 173, 173))
        self.radiobutton_bordercolour_hover = kwargs.get("radiobutton_bordercolour_hover", (0, 120, 215))
        self.radiobutton_bordercolour_pressed = kwargs.get("radiobutton_bordercolour_pressed", (0, 84, 153))
        self.radiobutton_bordercolour_disabled = kwargs.get("radiobutton_bordercolour_disabled", (0, 0, 0))

        self.radiobutton_borderwidth_default = kwargs.get("radiobutton_borderwidth_default", 2)
        self.radiobutton_borderwidth_hover = kwargs.get("radiobutton_borderwidth_hover", 2)
        self.radiobutton_borderwidth_pressed = kwargs.get("radiobutton_borderwidth_pressed", 2)
        self.radiobutton_borderwidth_disabled = kwargs.get("radiobutton_borderwidth_disabled", 0)

        self.radiobutton_borderstyle_default = kwargs.get("radiobutton_borderstyle_default", "solid")
        self.radiobutton_borderstyle_hover = kwargs.get("radiobutton_borderstyle_hover", "solid")
        self.radiobutton_borderstyle_pressed = kwargs.get("radiobutton_borderstyle_pressed", "solid")
        self.radiobutton_borderstyle_disabled = kwargs.get("radiobutton_borderstyle_disabled", "solid")

        # ------------------------- panel ------------------------- #

        self.panel_backgroundcolour_default = kwargs.get("panel_backgroundcolour_default", (255, 255, 255))
        self.panel_backgroundcolour_hover = kwargs.get("panel_backgroundcolour_hover", (255, 255, 255))
        self.panel_backgroundcolour_pressed = kwargs.get("panel_backgroundcolour_pressed", (255, 255, 255))
        self.panel_backgroundcolour_disabled = kwargs.get("panel_backgroundcolour_disabled", (255, 255, 255))

        self.panel_backgroundstyle_default = kwargs.get("panel_backgroundstyle_default", "solid")
        self.panel_backgroundstyle_hover = kwargs.get("panel_backgroundstyle_hover", "solid")
        self.panel_backgroundstyle_pressed = kwargs.get("panel_backgroundstyle_pressed", "solid")
        self.panel_backgroundstyle_disabled = kwargs.get("panel_backgroundstyle_disabled", "solid")

        self.panel_bordercolour_default = kwargs.get("panel_bordercolour_default", (179, 179, 179))
        self.panel_bordercolour_hover = kwargs.get("panel_bordercolour_hover", (179, 179, 179))
        self.panel_bordercolour_pressed = kwargs.get("panel_bordercolour_pressed", (179, 179, 179))
        self.panel_bordercolour_disabled = kwargs.get("panel_bordercolour_disabled", (179, 179, 179))

        self.panel_borderwidth_default = kwargs.get("panel_borderwidth_default", 0)
        self.panel_borderwidth_hover = kwargs.get("panel_borderwidth_hover", 0)
        self.panel_borderwidth_pressed = kwargs.get("panel_borderwidth_pressed", 0)
        self.panel_borderwidth_disabled = kwargs.get("panel_borderwidth_disabled", 0)

        self.panel_borderstyle_default = kwargs.get("panel_borderstyle_default", "solid")
        self.panel_borderstyle_hover = kwargs.get("panel_borderstyle_hover", "solid")
        self.panel_borderstyle_pressed = kwargs.get("panel_borderstyle_pressed", "solid")
        self.panel_borderstyle_disabled = kwargs.get("panel_borderstyle_disabled", "solid")

        self.panel_cornerradius_default = kwargs.get("panel_cornerradius_default", 0)
        self.panel_cornerradius_hover = kwargs.get("panel_cornerradius_hover", 0)
        self.panel_cornerradius_pressed = kwargs.get("panel_cornerradius_pressed", 0)
        self.panel_cornerradius_disabled = kwargs.get("panel_cornerradius_disabled", 0)

        # ----------------------- staticbox ----------------------- #

        self.staticbox_bordercolour_default = kwargs.get("staticbox_bordercolour_default", (179, 179, 179))
        self.staticbox_bordercolour_hover = kwargs.get("staticbox_bordercolour_hover", (179, 179, 179))
        self.staticbox_bordercolour_pressed = kwargs.get("staticbox_bordercolour_pressed", (179, 179, 179))
        self.staticbox_bordercolour_disabled = kwargs.get("staticbox_bordercolour_disabled", (179, 179, 179))

        self.staticbox_borderwidth_default = kwargs.get("staticbox_borderwidth_default", 2)
        self.staticbox_borderwidth_hover = kwargs.get("staticbox_borderwidth_hover", 2)
        self.staticbox_borderwidth_pressed = kwargs.get("staticbox_borderwidth_pressed", 2)
        self.staticbox_borderwidth_disabled = kwargs.get("staticbox_borderwidth_disabled", 2)

        self.staticbox_borderstyle_default = kwargs.get("staticbox_borderstyle_default", "solid")
        self.staticbox_borderstyle_hover = kwargs.get("staticbox_borderstyle_hover", "solid")
        self.staticbox_borderstyle_pressed = kwargs.get("staticbox_borderstyle_pressed", "solid")
        self.staticbox_borderstyle_disabled = kwargs.get("staticbox_borderstyle_disabled", "solid")

        self.staticbox_cornerradius_default = kwargs.get("staticbox_cornerradius_default", 0)
        self.staticbox_cornerradius_hover = kwargs.get("staticbox_cornerradius_hover", 0)
        self.staticbox_cornerradius_pressed = kwargs.get("staticbox_cornerradius_pressed", 0)
        self.staticbox_cornerradius_disabled = kwargs.get("staticbox_cornerradius_disabled", 0)

        # ----------------------- staticline ----------------------- #

        self.staticline_bordercolour_default = kwargs.get("staticline_bordercolour_default", (179, 179, 179))
        self.staticline_bordercolour_hover = kwargs.get("staticline_bordercolour_hover", (179, 179, 179))
        self.staticline_bordercolour_pressed = kwargs.get("staticline_bordercolour_pressed", (179, 179, 179))
        self.staticline_bordercolour_disabled = kwargs.get("staticline_bordercolour_disabled", (179, 179, 179))

        self.staticline_borderwidth_default = kwargs.get("staticline_borderwidth_default", 2)
        self.staticline_borderwidth_hover = kwargs.get("staticline_borderwidth_hover", 2)
        self.staticline_borderwidth_pressed = kwargs.get("staticline_borderwidth_pressed", 2)
        self.staticline_borderwidth_disabled = kwargs.get("staticline_borderwidth_disabled", 2)

        self.staticline_borderstyle_default = kwargs.get("staticline_borderstyle_default", "solid")
        self.staticline_borderstyle_hover = kwargs.get("staticline_borderstyle_hover", "solid")
        self.staticline_borderstyle_pressed = kwargs.get("staticline_borderstyle_pressed", "solid")
        self.staticline_borderstyle_disabled = kwargs.get("staticline_borderstyle_disabled", "solid")

        # ------------------------- gauge ------------------------- #

        self.gauge_backgroundcolour_default = kwargs.get("gauge_backgroundcolour_default", (225, 225, 225))
        self.gauge_backgroundcolour_hover = kwargs.get("gauge_backgroundcolour_hover", (229, 241, 251))
        self.gauge_backgroundcolour_pressed = kwargs.get("gauge_backgroundcolour_pressed", (204, 228, 247))
        self.gauge_backgroundcolour_disabled = kwargs.get("gauge_backgroundcolour_disabled", (0, 0, 0))

        self.gauge_backgroundstyle_default = kwargs.get("gauge_backgroundstyle_default", "solid")
        self.gauge_backgroundstyle_hover = kwargs.get("gauge_backgroundstyle_hover", "solid")
        self.gauge_backgroundstyle_pressed = kwargs.get("gauge_backgroundstyle_pressed", "solid")
        self.gauge_backgroundstyle_disabled = kwargs.get("gauge_backgroundstyle_disabled", "solid")

        self.gauge_bordercolour_default = kwargs.get("gauge_bordercolour_default", (173, 173, 173))
        self.gauge_bordercolour_hover = kwargs.get("gauge_bordercolour_hover", (0, 120, 215))
        self.gauge_bordercolour_pressed = kwargs.get("gauge_bordercolour_pressed", (0, 84, 153))
        self.gauge_bordercolour_disabled = kwargs.get("gauge_bordercolour_disabled", (0, 0, 0))

        self.gauge_borderwidth_default = kwargs.get("gauge_borderwidth_default", 2)
        self.gauge_borderwidth_hover = kwargs.get("gauge_borderwidth_hover", 2)
        self.gauge_borderwidth_pressed = kwargs.get("gauge_borderwidth_pressed", 2)
        self.gauge_borderwidth_disabled = kwargs.get("gauge_borderwidth_disabled", 2)

        self.gauge_borderstyle_default = kwargs.get("gauge_borderstyle_default", "solid")
        self.gauge_borderstyle_hover = kwargs.get("gauge_borderstyle_hover", "solid")
        self.gauge_borderstyle_pressed = kwargs.get("gauge_borderstyle_pressed", "solid")
        self.gauge_borderstyle_disabled = kwargs.get("gauge_borderstyle_disabled", "solid")

        self.gauge_cornerradius_default = kwargs.get("gauge_cornerradius_default", 0)
        self.gauge_cornerradius_hover = kwargs.get("gauge_cornerradius_hover", 0)
        self.gauge_cornerradius_pressed = kwargs.get("gauge_cornerradius_pressed", 0)
        self.gauge_cornerradius_disabled = kwargs.get("gauge_cornerradius_disabled", 0)

        # ------------------------ progress ------------------------ #

        self.progress_startfrom = kwargs.get("progress_startfrom", "left")
        
        self.progress_padding_default = kwargs.get("progress_padding_default", 3)
        self.progress_padding_hover = kwargs.get("progress_padding_hover", 3)
        self.progress_padding_pressed = kwargs.get("progress_padding_pressed", 3)
        self.progress_padding_disabled = kwargs.get("progress_padding_disabled", 3)

        self.progress_backgroundcolour_default = kwargs.get("progress_backgroundcolour_default", (52, 60, 180))
        self.progress_backgroundcolour_hover = kwargs.get("progress_backgroundcolour_hover", (81, 88, 184))
        self.progress_backgroundcolour_pressed = kwargs.get("progress_backgroundcolour_pressed", (43, 47, 113))
        self.progress_backgroundcolour_disabled = kwargs.get("progress_backgroundcolour_disabled", (195, 194, 218))

        self.progress_backgroundstyle_default = kwargs.get("progress_backgroundstyle_default", "solid")
        self.progress_backgroundstyle_hover = kwargs.get("progress_backgroundstyle_hover", "solid")
        self.progress_backgroundstyle_pressed = kwargs.get("progress_backgroundstyle_pressed", "solid")
        self.progress_backgroundstyle_disabled = kwargs.get("progress_backgroundstyle_disabled", "solid")

        self.progress_bordercolour_default = kwargs.get("progress_bordercolour_default", (0, 0, 0))
        self.progress_bordercolour_hover = kwargs.get("progress_bordercolour_hover", (0, 0, 0))
        self.progress_bordercolour_pressed = kwargs.get("progress_bordercolour_pressed", (0, 0, 0))
        self.progress_bordercolour_disabled = kwargs.get("progress_bordercolour_disabled", (0, 0, 0))

        self.progress_borderwidth_default = kwargs.get("progress_borderwidth_default", 0)
        self.progress_borderwidth_hover = kwargs.get("progress_borderwidth_hover", 0)
        self.progress_borderwidth_pressed = kwargs.get("progress_borderwidth_pressed", 0)
        self.progress_borderwidth_disabled = kwargs.get("progress_borderwidth_disabled", 0)

        self.progress_borderstyle_default = kwargs.get("progress_borderstyle_default", "solid")
        self.progress_borderstyle_hover = kwargs.get("progress_borderstyle_hover", "solid")
        self.progress_borderstyle_pressed = kwargs.get("progress_borderstyle_pressed", "solid")
        self.progress_borderstyle_disabled = kwargs.get("progress_borderstyle_disabled", "solid")

        self.progress_cornerradius_default = kwargs.get("progress_cornerradius_default", 0)
        self.progress_cornerradius_hover = kwargs.get("progress_cornerradius_hover", 0)
        self.progress_cornerradius_pressed = kwargs.get("progress_cornerradius_pressed", 0)
        self.progress_cornerradius_disabled = kwargs.get("progress_cornerradius_disabled", 0)

        # ------------------ scrolledpanel track ------------------ #

        self.track_backgroundcolour_default = kwargs.get("track_backgroundcolour_default", (225, 225, 225))
        self.track_backgroundcolour_hover = kwargs.get("track_backgroundcolour_hover", (225, 225, 225))
        self.track_backgroundcolour_pressed = kwargs.get("track_backgroundcolour_pressed", (225, 225, 225))
        self.track_backgroundcolour_disabled = kwargs.get("track_backgroundcolour_disabled", (225, 225, 225))

        self.track_backgroundstyle_default = kwargs.get("track_backgroundstyle_default", "solid")
        self.track_backgroundstyle_hover = kwargs.get("track_backgroundstyle_hover", "solid")
        self.track_backgroundstyle_pressed = kwargs.get("track_backgroundstyle_pressed", "solid")
        self.track_backgroundstyle_disabled = kwargs.get("track_backgroundstyle_disabled", "solid")

        self.track_bordercolour_default = kwargs.get("track_bordercolour_default", (0, 0, 0))
        self.track_bordercolour_hover = kwargs.get("track_bordercolour_hover", (0, 0, 0))
        self.track_bordercolour_pressed = kwargs.get("track_bordercolour_pressed", (0, 0, 0))
        self.track_bordercolour_disabled = kwargs.get("track_bordercolour_disabled", (0, 0, 0))

        self.track_borderwidth_default = kwargs.get("track_borderwidth_default", 0)
        self.track_borderwidth_hover = kwargs.get("track_borderwidth_hover", 0)
        self.track_borderwidth_pressed = kwargs.get("track_borderwidth_pressed", 0)
        self.track_borderwidth_disabled = kwargs.get("track_borderwidth_disabled", 0)

        self.track_borderstyle_default = kwargs.get("track_borderstyle_default", "solid")
        self.track_borderstyle_hover = kwargs.get("track_borderstyle_hover", "solid")
        self.track_borderstyle_pressed = kwargs.get("track_borderstyle_pressed", "solid")
        self.track_borderstyle_disabled = kwargs.get("track_borderstyle_disabled", "solid")

        # ------------------ scrolledpanel thumb ------------------ #

        self.thumb_width = kwargs.get("thumb_width", 15)

        self.thumb_padding_default = kwargs.get("thumb_padding_default", 3)
        self.thumb_padding_hover = kwargs.get("thumb_padding_hover", 3)
        self.thumb_padding_pressed = kwargs.get("thumb_padding_pressed", 3)
        self.thumb_padding_disabled = kwargs.get("thumb_padding_disabled", 3)

        self.thumb_backgroundcolour_default = kwargs.get("thumb_backgroundcolour_default", (173, 173, 173))
        self.thumb_backgroundcolour_hover = kwargs.get("thumb_backgroundcolour_hover", (130, 130, 130))
        self.thumb_backgroundcolour_pressed = kwargs.get("thumb_backgroundcolour_pressed", (100, 100, 100))
        self.thumb_backgroundcolour_disabled = kwargs.get("thumb_backgroundcolour_disabled", (0, 0, 0))

        self.thumb_backgroundstyle_default = kwargs.get("thumb_backgroundstyle_default", "solid")
        self.thumb_backgroundstyle_hover = kwargs.get("thumb_backgroundstyle_hover", "solid")
        self.thumb_backgroundstyle_pressed = kwargs.get("thumb_backgroundstyle_pressed", "solid")
        self.thumb_backgroundstyle_disabled = kwargs.get("thumb_backgroundstyle_disabled", "solid")

        self.thumb_bordercolour_default = kwargs.get("thumb_bordercolour_default", (0, 0, 0))
        self.thumb_bordercolour_hover = kwargs.get("thumb_bordercolour_hover", (0, 0, 0))
        self.thumb_bordercolour_pressed = kwargs.get("thumb_bordercolour_pressed", (0, 0, 0))
        self.thumb_bordercolour_disabled = kwargs.get("thumb_bordercolour_disabled", (0, 0, 0))

        self.thumb_borderwidth_default = kwargs.get("thumb_borderwidth_default", 0)
        self.thumb_borderwidth_hover = kwargs.get("thumb_borderwidth_hover", 0)
        self.thumb_borderwidth_pressed = kwargs.get("thumb_borderwidth_pressed", 0)
        self.thumb_borderwidth_disabled = kwargs.get("thumb_borderwidth_disabled", 0)

        self.thumb_borderstyle_default = kwargs.get("thumb_borderstyle_default", "solid")
        self.thumb_borderstyle_hover = kwargs.get("thumb_borderstyle_hover", "solid")
        self.thumb_borderstyle_pressed = kwargs.get("thumb_borderstyle_pressed", "solid")
        self.thumb_borderstyle_disabled = kwargs.get("thumb_borderstyle_disabled", "solid")

        self.thumb_cornerradius_default = kwargs.get("thumb_cornerradius_default", 4)
        self.thumb_cornerradius_hover = kwargs.get("thumb_cornerradius_hover", 4)
        self.thumb_cornerradius_pressed = kwargs.get("thumb_cornerradius_pressed", 4)
        self.thumb_cornerradius_disabled = kwargs.get("thumb_cornerradius_disabled", 0)

        # ---------------- scrolledpanel properties ---------------- #

        self.scroll_x = kwargs.get("scroll_x", True)
        self.scroll_y = kwargs.get("scroll_y", True)
        self.rate_x = kwargs.get("rate_x", 20)
        self.rate_y = kwargs.get("rate_y", 20)

        # ------------------------ combobox ------------------------ #

        self.combobox_backgroundcolour_default = kwargs.get("combobox_backgroundcolour_default", (225, 225, 225))
        self.combobox_backgroundcolour_hover = kwargs.get("combobox_backgroundcolour_hover", (229, 241, 251))
        self.combobox_backgroundcolour_pressed = kwargs.get("combobox_backgroundcolour_pressed", (204, 228, 247))
        self.combobox_backgroundcolour_disabled = kwargs.get("combobox_backgroundcolour_disabled", (179, 179, 179))

        self.combobox_backgroundstyle_default = kwargs.get("combobox_backgroundstyle_default", "solid")
        self.combobox_backgroundstyle_hover = kwargs.get("combobox_backgroundstyle_hover", "solid")
        self.combobox_backgroundstyle_pressed = kwargs.get("combobox_backgroundstyle_pressed", "solid")
        self.combobox_backgroundstyle_disabled = kwargs.get("combobox_backgroundstyle_disabled", "solid")

        self.combobox_bordercolour_default = kwargs.get("combobox_bordercolour_default", (173, 173, 173))
        self.combobox_bordercolour_hover = kwargs.get("combobox_bordercolour_hover", (0, 120, 215))
        self.combobox_bordercolour_pressed = kwargs.get("combobox_bordercolour_pressed", (0, 84, 153))
        self.combobox_bordercolour_disabled = kwargs.get("combobox_bordercolour_disabled", (0, 0, 0))

        self.combobox_borderwidth_default = kwargs.get("combobox_borderwidth_default", 2)
        self.combobox_borderwidth_hover = kwargs.get("combobox_borderwidth_hover", 2)
        self.combobox_borderwidth_pressed = kwargs.get("combobox_borderwidth_pressed", 2)
        self.combobox_borderwidth_disabled = kwargs.get("combobox_borderwidth_disabled", 2)

        self.combobox_borderstyle_default = kwargs.get("combobox_borderstyle_default", "solid")
        self.combobox_borderstyle_hover = kwargs.get("combobox_borderstyle_hover", "solid")
        self.combobox_borderstyle_pressed = kwargs.get("combobox_borderstyle_pressed", "solid")
        self.combobox_borderstyle_disabled = kwargs.get("combobox_borderstyle_disabled", "solid")

        self.combobox_cornerradius_default = kwargs.get("combobox_cornerradius_default", 0)
        self.combobox_cornerradius_hover = kwargs.get("combobox_cornerradius_hover", 0)
        self.combobox_cornerradius_pressed = kwargs.get("combobox_cornerradius_pressed", 0)
        self.combobox_cornerradius_disabled = kwargs.get("combobox_cornerradius_disabled", 0)

        # --------------------- combobox arrow --------------------- #

        self.arrow_width = kwargs.get("arrow_width", 15)
        self.arrow_height = kwargs.get("arrow_height", 5)
        self.arrow_separation = kwargs.get("arrow_separation", 50)
        self.arrow_side = kwargs.get("arrow_side", "right")

        self.arrow_bordercolour_default = kwargs.get("arrow_bordercolour_default", (173, 173, 173))
        self.arrow_bordercolour_hover = kwargs.get("arrow_bordercolour_hover", (0, 120, 215))
        self.arrow_bordercolour_pressed = kwargs.get("arrow_bordercolour_pressed", (0, 84, 153))
        self.arrow_bordercolour_disabled = kwargs.get("arrow_bordercolour_disabled", (0, 0, 0))

        self.arrow_borderwidth_default = kwargs.get("arrow_borderwidth_default", 2)
        self.arrow_borderwidth_hover = kwargs.get("arrow_borderwidth_hover", 2)
        self.arrow_borderwidth_pressed = kwargs.get("arrow_borderwidth_pressed", 2)
        self.arrow_borderwidth_disabled = kwargs.get("arrow_borderwidth_disabled", 2)

        self.arrow_borderstyle_default = kwargs.get("arrow_borderstyle_default", "solid")
        self.arrow_borderstyle_hover = kwargs.get("arrow_borderstyle_hover", "solid")
        self.arrow_borderstyle_pressed = kwargs.get("arrow_borderstyle_pressed", "solid")
        self.arrow_borderstyle_disabled = kwargs.get("arrow_borderstyle_disabled", "solid")

        self._check_wrong_arguments(kwargs)

    def _check_wrong_arguments(self, kwargs:dict):
        # looks for invalid arguments
        attributes = self.__dict__.keys()
        for key in kwargs.keys():
            if key not in attributes:
                print(f"Config::Key \"{key}\" not in attributes.")        
