"""example.py

A frame with customizable control examples.

wxCustomizableControls
cenfra
"""


import src as cc
import wx


class Main(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_ui()


    def __init_ui(self):
        """Initializes the user interface."""

        self.SetTitle("wxCustomizableControls Examples")
        self.SetMinClientSize(wx.Size(600, 300))

        self.main_panel = wx.Panel(self)
        self.SetBackgroundColour(wx.Colour(60, 60, 60))

        button_style = {

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "cross",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolor_default": (0, 0, 0),
            "fontcolor_hover": (0, 0, 0),
            "fontcolor_pressed": (0, 0, 0),
            "fontcolor_disabled": (0, 0, 0),

            "fontsize_default": 12,
            "fontsize_hover": 12,
            "fontsize_pressed": 12,
            "fontsize_disabled": 12,

            "fontstyle_default": "normal",
            "fontstyle_hover": "italic",
            "fontstyle_pressed": "normal",
            "fontstyle_disabled": "normal",

            "fontweight_default": "normal",
            "fontweight_hover": "bold",
            "fontweight_pressed": "normal",
            "fontweight_disabled": "normal",

            # ------------------------- button ------------------------- #

            "button_backgroundcolor_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "button_backgroundcolor_hover": (224, 203, 224),
            "button_backgroundcolor_pressed": (124, 185, 182),
            "button_backgroundcolor_disabled": (231, 1, 202),

            "button_backgroundstyle_default": "solid",
            "button_backgroundstyle_hover": "solid",
            "button_backgroundstyle_pressed": "solid",
            "button_backgroundstyle_disabled": "solid",

            "button_bordercolor_default": (29, 11, 175),
            "button_bordercolor_hover": (195, 15, 132),
            "button_bordercolor_pressed": (48, 221, 224),
            "button_bordercolor_disabled": (46, 31, 95),

            "button_borderwidth_default": 1,
            "button_borderwidth_hover": 2,
            "button_borderwidth_pressed": 3,
            "button_borderwidth_disabled": 4,

            "button_borderstyle_default": "solid",
            "button_borderstyle_hover": "solid",
            "button_borderstyle_pressed": "solid",
            "button_borderstyle_disabled": "solid",

            "button_cornerradius_default": 10,
            "button_cornerradius_hover": 10,
            "button_cornerradius_pressed": 10,
            "button_cornerradius_disabled": 10,

            # ------------------------- images ------------------------- #

            "image_path_default": "images/example.png",
            "image_path_hover": "images/example.png",
            "image_path_pressed": "",
            "image_path_disabled": "",

            "image_width_default": 70,
            "image_width_hover": 70,
            "image_width_pressed": 10,
            "image_width_disabled": 10,

            "image_height_default": 70, 
            "image_height_hover": 70,
            "image_height_pressed": 10,
            "image_height_disabled": 10,

            "image_channels_default": (1.0, 1.0, 1.0, 1.0),
            "image_channels_hover": (1.0, 1.0, 1.0, 0.5),
            "image_channels_pressed": (1.0, 1.0, 1.0, 1.0),
            "image_channels_disabled": (1.0, 1.0, 1.0, 1.0),

            "image_separation": 10,
            "image_side": "right",
        }

        checkbox_style = {

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "cross",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolor_default": (0, 0, 0),
            "fontcolor_hover": (0, 0, 0),
            "fontcolor_pressed": (0, 0, 0),
            "fontcolor_disabled": (0, 0, 0),

            "fontsize_default": 12,
            "fontsize_hover": 12,
            "fontsize_pressed": 12,
            "fontsize_disabled": 12,

            "fontstyle_default": "normal",
            "fontstyle_hover": "italic",
            "fontstyle_pressed": "normal",
            "fontstyle_disabled": "normal",

            "fontweight_default": "normal",
            "fontweight_hover": "bold",
            "fontweight_pressed": "normal",
            "fontweight_disabled": "normal",

            # ------------------------ checkbox ------------------------ #

            "checkbox_backgroundcolor_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "checkbox_backgroundcolor_hover": (224, 203, 224),
            "checkbox_backgroundcolor_pressed": (124, 185, 182),
            "checkbox_backgroundcolor_disabled": (231, 1, 202),

            "checkbox_backgroundstyle_default": "solid",
            "checkbox_backgroundstyle_hover": "solid",
            "checkbox_backgroundstyle_pressed": "solid",
            "checkbox_backgroundstyle_disabled": "solid",

            "checkbox_bordercolor_default": (29, 11, 175),
            "checkbox_bordercolor_hover": (195, 15, 132),
            "checkbox_bordercolor_pressed": (48, 221, 224),
            "checkbox_bordercolor_disabled": (46, 31, 95),

            "checkbox_borderwidth_default": 1,
            "checkbox_borderwidth_hover": 2,
            "checkbox_borderwidth_pressed": 3,
            "checkbox_borderwidth_disabled": 4,

            "checkbox_borderstyle_default": "solid",
            "checkbox_borderstyle_hover": "solid",
            "checkbox_borderstyle_pressed": "solid",
            "checkbox_borderstyle_disabled": "solid",

            "checkbox_cornerradius_default": 3,
            "checkbox_cornerradius_hover": 3,
            "checkbox_cornerradius_pressed": 3,
            "checkbox_cornerradius_disabled": 3,

            "checkbox_width": 20,
            "checkbox_height": 20,
            "checkbox_side": "left",
            "checkbox_separation": 10,

            # ------------------------- images ------------------------- #
            
            "image_separation": 10,
            "image_side": "top",

            "image_path_default": "images/example.png",
            "image_path_hover": "images/example.png",
            "image_path_pressed": "",
            "image_path_disabled": "",

            "image_width_default": 70,
            "image_width_hover": 70,
            "image_width_pressed": 10,
            "image_width_disabled": 10,

            "image_height_default": 70, 
            "image_height_hover": 70,
            "image_height_pressed": 10,
            "image_height_disabled": 10,

            "image_channels_default": (1.0, 1.0, 1.0, 1.0),
            "image_channels_hover": (1.0, 1.0, 1.0, 0.5),
            "image_channels_pressed": (1.0, 1.0, 1.0, 1.0),
            "image_channels_disabled": (1.0, 1.0, 1.0, 1.0),

            # ----------------------- checkmark ----------------------- #

            "checkmark_bordercolor_default": (255, 255, 255),
            "checkmark_bordercolor_hover": (255, 255, 255),
            "checkmark_bordercolor_pressed": (255, 255, 255),
            "checkmark_bordercolor_disabled": (255, 255, 255),

            "checkmark_borderwidth_default": 2,
            "checkmark_borderwidth_hover": 3,
            "checkmark_borderwidth_pressed": 4,
            "checkmark_borderwidth_disabled": 2,

            "checkmark_borderstyle_default": "solid",
            "checkmark_borderstyle_hover": "solid",
            "checkmark_borderstyle_pressed": "solid",
            "checkmark_borderstyle_disabled": "solid",
        }

        b = cc.Button(self.main_panel, label="test", config=button_style)
        b.Bind(wx.EVT_BUTTON, lambda e: print("button pressed"))

        c = cc.CheckBox(self.main_panel, label="test checkbox", config=checkbox_style, pos=(10, 100))
        

if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
