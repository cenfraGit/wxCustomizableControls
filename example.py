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

            # -------------------- selection marker -------------------- #

            "selectionmarker_bordercolor_default": (255, 255, 255),
            "selectionmarker_bordercolor_hover": (255, 255, 255),
            "selectionmarker_bordercolor_pressed": (255, 255, 255),
            "selectionmarker_bordercolor_disabled": (255, 255, 255),

            "selectionmarker_borderwidth_default": 2,
            "selectionmarker_borderwidth_hover": 3,
            "selectionmarker_borderwidth_pressed": 4,
            "selectionmarker_borderwidth_disabled": 2,

            "selectionmarker_borderstyle_default": "solid",
            "selectionmarker_borderstyle_hover": "solid",
            "selectionmarker_borderstyle_pressed": "solid",
            "selectionmarker_borderstyle_disabled": "solid",
        }

        radiobutton_style = {

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

            # ---------------------- radiobutton ---------------------- #

            "radiobutton_backgroundcolor_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "radiobutton_backgroundcolor_hover": (224, 203, 224),
            "radiobutton_backgroundcolor_pressed": (124, 185, 182),
            "radiobutton_backgroundcolor_disabled": (231, 1, 202),

            "radiobutton_backgroundstyle_default": "solid",
            "radiobutton_backgroundstyle_hover": "solid",
            "radiobutton_backgroundstyle_pressed": "solid",
            "radiobutton_backgroundstyle_disabled": "solid",

            "radiobutton_bordercolor_default": (29, 11, 175),
            "radiobutton_bordercolor_hover": (195, 15, 132),
            "radiobutton_bordercolor_pressed": (48, 221, 224),
            "radiobutton_bordercolor_disabled": (46, 31, 95),

            "radiobutton_borderwidth_default": 1,
            "radiobutton_borderwidth_hover": 2,
            "radiobutton_borderwidth_pressed": 3,
            "radiobutton_borderwidth_disabled": 4,

            "radiobutton_borderstyle_default": "solid",
            "radiobutton_borderstyle_hover": "solid",
            "radiobutton_borderstyle_pressed": "solid",
            "radiobutton_borderstyle_disabled": "solid",

            "radiobutton_cornerradius_default": 3,
            "radiobutton_cornerradius_hover": 3,
            "radiobutton_cornerradius_pressed": 3,
            "radiobutton_cornerradius_disabled": 3,

            "radiobutton_diameter": 20,
            "radiobutton_side": "left",
            "radiobutton_separation": 10,

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

            # -------------------- selection marker -------------------- #

            "selectionmarker_diameter_default": 8,
            "selectionmarker_diameter_hover": 6,
            "selectionmarker_diameter_pressed": 4,
            "selectionmarker_diameter_disabled": 7,

            "selectionmarker_backgroundcolor_default": (120, 120, 120),
            "selectionmarker_backgroundcolor_hover": (170, 60, 60),
            "selectionmarker_backgroundcolor_pressed": (255, 0, 0),
            "selectionmarker_backgroundcolor_disabled": (255, 255, 255),

            "selectionmarker_backgroundstyle_default": "solid",
            "selectionmarker_backgroundstyle_hover": "solid",
            "selectionmarker_backgroundstyle_pressed": "solid",
            "selectionmarker_backgroundstyle_disabled": "solid",
        }

        button = cc.Button(self.main_panel, label="test", config=button_style)
        button.Bind(wx.EVT_BUTTON, lambda e: print("button pressed"))

        checkbox = cc.CheckBox(self.main_panel, label="test checkbox", config=checkbox_style, pos=wx.Point(10, 100))
        checkbox.Bind(wx.EVT_CHECKBOX, lambda e: print("checkbox pressed"))

        radiobutton = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(10, 250), style=wx.RB_GROUP)
        radiobutton.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton pressed"))
        radiobutton1 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(210, 250))
        radiobutton1.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton1 pressed"))
        radiobutton2 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(410, 250))
        radiobutton2.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton2 pressed"))
        button1 = cc.Button(self.main_panel, label="change radiobutton value", config=button_style, pos=wx.Point(610, 250))
        button1.Bind(wx.EVT_BUTTON, lambda e: radiobutton1.SetValue(True))

        
        
        

if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
