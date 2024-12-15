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

            # ------------------------- button ------------------------- #

            "backgroundcolor_button_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "backgroundcolor_button_hover": (224, 203, 224),
            "backgroundcolor_button_pressed": (124, 185, 182),
            "backgroundcolor_button_disabled": (231, 1, 202),

            "backgroundstyle_button_default": "solid",
            "backgroundstyle_button_hover": "solid",
            "backgroundstyle_button_pressed": "solid",
            "backgroundstyle_button_disabled": "solid",

            "bordercolor_button_default": (29, 11, 175),
            "bordercolor_button_hover": (195, 15, 132),
            "bordercolor_button_pressed": (48, 221, 224),
            "bordercolor_button_disabled": (46, 31, 95),

            "borderwidth_button_default": 1,
            "borderwidth_button_hover": 2,
            "borderwidth_button_pressed": 3,
            "borderwidth_button_disabled": 4,

            "borderstyle_button_default": "solid",
            "borderstyle_button_hover": "solid",
            "borderstyle_button_pressed": "solid",
            "borderstyle_button_disabled": "solid",

            "cornerradius_button_default": 10,
            "cornerradius_button_hover": 10,
            "cornerradius_button_pressed": 10,
            "cornerradius_button_disabled": 10,

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

            # ------------------------- images ------------------------- #

            "path_image_default": "images/example.png",
            "path_image_hover": "images/example.png",
            "path_image_pressed": "",
            "path_image_disabled": "",

            "width_image_default": 70,
            "width_image_hover": 70,
            "width_image_pressed": 10,
            "width_image_disabled": 10,

            "height_image_default": 70, 
            "height_image_hover": 70,
            "height_image_pressed": 10,
            "height_image_disabled": 10,

            "channels_image_default": (1.0, 1.0, 1.0, 1.0),
            "channels_image_hover": (1.0, 1.0, 1.0, 0.5),
            "channels_image_pressed": (1.0, 1.0, 1.0, 1.0),
            "channels_image_disabled": (1.0, 1.0, 1.0, 1.0),

            "separation_image": 10,
            "side_image": "right",
        }

        checkbox_style = {

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "cross",
            "mousecursor_disabled": "arrow", 

            # ------------------------ checkbox ------------------------ #

            "backgroundcolor_checkbox_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "backgroundcolor_checkbox_hover": (224, 203, 224),
            "backgroundcolor_checkbox_pressed": (124, 185, 182),
            "backgroundcolor_checkbox_disabled": (231, 1, 202),

            "backgroundstyle_checkbox_default": "solid",
            "backgroundstyle_checkbox_hover": "solid",
            "backgroundstyle_checkbox_pressed": "solid",
            "backgroundstyle_checkbox_disabled": "solid",

            "bordercolor_checkbox_default": (29, 11, 175),
            "bordercolor_checkbox_hover": (195, 15, 132),
            "bordercolor_checkbox_pressed": (48, 221, 224),
            "bordercolor_checkbox_disabled": (46, 31, 95),

            "borderwidth_checkbox_default": 1,
            "borderwidth_checkbox_hover": 2,
            "borderwidth_checkbox_pressed": 3,
            "borderwidth_checkbox_disabled": 4,

            "borderstyle_checkbox_default": "solid",
            "borderstyle_checkbox_hover": "solid",
            "borderstyle_checkbox_pressed": "solid",
            "borderstyle_checkbox_disabled": "solid",

            "cornerradius_checkbox_default": 3,
            "cornerradius_checkbox_hover": 3,
            "cornerradius_checkbox_pressed": 3,
            "cornerradius_checkbox_disabled": 3,

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

            # ------------------------- images ------------------------- #
            
            "separation_image": 10,
            "side_image": "right",

            "path_image_default": "images/example.png",
            "path_image_hover": "images/example.png",
            "path_image_pressed": "",
            "path_image_disabled": "",

            "width_image_default": 70,
            "width_image_hover": 70,
            "width_image_pressed": 10,
            "width_image_disabled": 10,

            "height_image_default": 70, 
            "height_image_hover": 70,
            "height_image_pressed": 10,
            "height_image_disabled": 10,

            "channels_image_default": (1.0, 1.0, 1.0, 1.0),
            "channels_image_hover": (1.0, 1.0, 1.0, 0.5),
            "channels_image_pressed": (1.0, 1.0, 1.0, 1.0),
            "channels_image_disabled": (1.0, 1.0, 1.0, 1.0),

            # ------------------------ checkbox ------------------------ #

            "separation_checkbox": 10,
            "side_checkbox": "top",

            "width_checkbox": 20,
            "height_checkbox": 20,

            # checkmark

            "bordercolor_checkmark_default": (255, 255, 255),
            "bordercolor_checkmark_hover": (255, 255, 255),
            "bordercolor_checkmark_pressed": (255, 255, 255),
            "bordercolor_checkmark_disabled": (255, 255, 255),

            "borderwidth_checkmark_default": 2,
            "borderwidth_checkmark_hover": 3,
            "borderwidth_checkmark_pressed": 4,
            "borderwidth_checkmark_disabled": 2,

            "borderstyle_checkmark_default": "solid",
            "borderstyle_checkmark_hover": "solid",
            "borderstyle_checkmark_pressed": "solid",
            "borderstyle_checkmark_disabled": "solid",
        }

        b = cc.Button(self.main_panel, label="test", config=button_style)
        b.Bind(wx.EVT_BUTTON, lambda e: print("button pressed"))

        c = cc.CheckBox(self.main_panel, label="test checkbox", config=checkbox_style, pos=(10, 100))
        

if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
