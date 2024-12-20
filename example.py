"""example.py

A frame with customizable control examples.

wxCustomizableControls
cenfra
"""


import platform
import src as cc
import wx

# --------------------- platform setup --------------------- #

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
elif platform.system() == "Linux":
    import os
    os.environ["GDK_BACKEND"] = "x11"


class Main(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_ui()


    def __init_ui(self):
        """Initializes the user interface."""

        self.SetTitle("wxCustomizableControls Examples")
        self.SetMinClientSize(wx.Size(1200, 600))

        self.main_panel = wx.Panel(self)
        self.main_panel.SetBackgroundColour(wx.Colour(60, 60, 60))

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_panel.SetSizer(self.main_sizer)

        button_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "cross",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolour_default": (0, 0, 0),
            "fontcolour_hover": (0, 0, 0),
            "fontcolour_pressed": (0, 0, 0),
            "fontcolour_disabled": (0, 0, 0),

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

            #"button_backgroundcolour_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "button_backgroundcolour_default": (0, 0, 0),
            "button_backgroundcolour_hover": (0, 0, 0),
            "button_backgroundcolour_pressed": (0, 0, 0),
            "button_backgroundcolour_disabled": (231, 1, 202),

            "button_backgroundstyle_default": "solid",
            "button_backgroundstyle_hover": "solid",
            "button_backgroundstyle_pressed": "solid",
            "button_backgroundstyle_disabled": "solid",

            "button_bordercolour_default": (255, 0, 0),
            "button_bordercolour_hover": (0, 255, 0),
            "button_bordercolour_pressed": (0, 0, 255),
            "button_bordercolour_disabled": (46, 31, 95),

            "button_borderwidth_default": 4,
            "button_borderwidth_hover": 30,
            "button_borderwidth_pressed": 4,
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

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "cross",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolour_default": (0, 0, 0),
            "fontcolour_hover": (0, 0, 0),
            "fontcolour_pressed": (0, 0, 0),
            "fontcolour_disabled": (0, 0, 0),

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

            # "checkbox_backgroundcolour_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "checkbox_backgroundcolour_default": (0, 0, 0),
            "checkbox_backgroundcolour_hover": (0, 0, 0),
            "checkbox_backgroundcolour_pressed": (0, 0, 0),
            "checkbox_backgroundcolour_disabled": (231, 1, 202),

            "checkbox_backgroundstyle_default": "solid",
            "checkbox_backgroundstyle_hover": "solid",
            "checkbox_backgroundstyle_pressed": "solid",
            "checkbox_backgroundstyle_disabled": "solid",

            "checkbox_bordercolour_default": (255, 0, 0),
            "checkbox_bordercolour_hover": (0, 255, 0),
            "checkbox_bordercolour_pressed": (0, 0, 255),
            "checkbox_bordercolour_disabled": (46, 31, 95),

            "checkbox_borderwidth_default": 1,
            "checkbox_borderwidth_hover": 30,
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
            "checkbox_separation": 4,

            # ------------------------- images ------------------------- #
            
            "image_separation": 10,
            "image_side": "top",

            # "image_path_default": "images/example.png",
            # "image_path_hover": "images/example.png",
            # "image_path_pressed": "",
            # "image_path_disabled": "",

            # "image_width_default": 70,
            # "image_width_hover": 70,
            # "image_width_pressed": 10,
            # "image_width_disabled": 10,

            # "image_height_default": 70, 
            # "image_height_hover": 70,
            # "image_height_pressed": 10,
            # "image_height_disabled": 10,

            "image_path_default": "",
            "image_path_hover": "",
            "image_path_pressed": "",
            "image_path_disabled": "",

            "image_width_default": 0,
            "image_width_hover": 0,
            "image_width_pressed": 0,
            "image_width_disabled": 0,

            "image_height_default": 0, 
            "image_height_hover": 0,
            "image_height_pressed": 0,
            "image_height_disabled": 0,

            "image_channels_default": (1.0, 1.0, 1.0, 1.0),
            "image_channels_hover": (1.0, 1.0, 1.0, 0.5),
            "image_channels_pressed": (1.0, 1.0, 1.0, 1.0),
            "image_channels_disabled": (1.0, 1.0, 1.0, 1.0),

            # -------------------- selection marker -------------------- #

            "selectionmarker_bordercolour_default": (255, 0, 0),
            "selectionmarker_bordercolour_hover": (0, 255, 0),
            "selectionmarker_bordercolour_pressed": (0, 0, 255),
            "selectionmarker_bordercolour_disabled": (255, 255, 255),

            "selectionmarker_borderwidth_default": 2,
            "selectionmarker_borderwidth_hover": 2,
            "selectionmarker_borderwidth_pressed": 2,
            "selectionmarker_borderwidth_disabled": 2,

            "selectionmarker_borderstyle_default": "solid",
            "selectionmarker_borderstyle_hover": "solid",
            "selectionmarker_borderstyle_pressed": "solid",
            "selectionmarker_borderstyle_disabled": "solid",
        }

        radiobutton_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "cross",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolour_default": (0, 0, 0),
            "fontcolour_hover": (0, 0, 0),
            "fontcolour_pressed": (0, 0, 0),
            "fontcolour_disabled": (0, 0, 0),

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

            # "radiobutton_backgroundcolour_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "radiobutton_backgroundcolour_default": (0, 0, 0),
            "radiobutton_backgroundcolour_hover": (0, 0, 0),
            "radiobutton_backgroundcolour_pressed": (0, 0, 0),
            "radiobutton_backgroundcolour_disabled": (0, 0, 0),

            "radiobutton_backgroundstyle_default": "solid",
            "radiobutton_backgroundstyle_hover": "solid",
            "radiobutton_backgroundstyle_pressed": "solid",
            "radiobutton_backgroundstyle_disabled": "solid",

            "radiobutton_bordercolour_default": (255, 0, 0),
            "radiobutton_bordercolour_hover": (0, 255, 0),
            "radiobutton_bordercolour_pressed": (0, 0, 255),
            "radiobutton_bordercolour_disabled": (0, 0, 0),

            "radiobutton_borderwidth_default": 2,
            "radiobutton_borderwidth_hover": 2,
            "radiobutton_borderwidth_pressed": 2,
            "radiobutton_borderwidth_disabled": 4,

            "radiobutton_borderstyle_default": "long_dash",
            "radiobutton_borderstyle_hover": "solid",
            "radiobutton_borderstyle_pressed": "solid",
            "radiobutton_borderstyle_disabled": "solid",

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
            "selectionmarker_diameter_hover": 8,
            "selectionmarker_diameter_pressed": 8,
            "selectionmarker_diameter_disabled": 7,

            "selectionmarker_backgroundcolour_default": (255, 0, 0),
            "selectionmarker_backgroundcolour_hover": (0, 255, 0),
            "selectionmarker_backgroundcolour_pressed": (0, 0, 255),
            "selectionmarker_backgroundcolour_disabled": (255, 255, 255),

            "selectionmarker_backgroundstyle_default": "solid",
            "selectionmarker_backgroundstyle_hover": "solid",
            "selectionmarker_backgroundstyle_pressed": "solid",
            "selectionmarker_backgroundstyle_disabled": "solid",
        }

        panel_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # ------------------------- panel ------------------------- #

            #"panel_backgroundcolour_default": (50, 10, 20, 30, (255, 0, 0), (0, 255, 255)),
            "panel_backgroundcolour_default": (0, 0, 0),
            "panel_backgroundcolour_hover": (0, 0, 0),
            "panel_backgroundcolour_pressed": (0, 0, 0),
            "panel_backgroundcolour_disabled": (231, 1, 202),

            "panel_backgroundstyle_default": "solid",
            "panel_backgroundstyle_hover": "solid",
            "panel_backgroundstyle_pressed": "solid",
            "panel_backgroundstyle_disabled": "solid",

            "panel_bordercolour_default": (255, 0, 0),
            "panel_bordercolour_hover": (0, 255, 0),
            "panel_bordercolour_pressed": (0, 0, 255),
            "panel_bordercolour_disabled": (46, 31, 95),

            "panel_borderwidth_default": 2,
            "panel_borderwidth_hover": 30,
            "panel_borderwidth_pressed": 2,
            "panel_borderwidth_disabled": 4,

            "panel_borderstyle_default": "solid",
            "panel_borderstyle_hover": "solid",
            "panel_borderstyle_pressed": "solid",
            "panel_borderstyle_disabled": "solid",

            "panel_cornerradius_default": 10,
            "panel_cornerradius_hover": 10,
            "panel_cornerradius_pressed": 10,
            "panel_cornerradius_disabled": 10,
        }

        staticbox_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # -------------------- font attributes -------------------- #

            "fontfacename_default": "Verdana",
            "fontfacename_hover": "Verdana",
            "fontfacename_pressed": "Verdana",
            "fontfacename_disabled": "Verdana",

            "fontcolour_default": (0, 0, 0),
            "fontcolour_hover": (0, 0, 0),
            "fontcolour_pressed": (0, 0, 0),
            "fontcolour_disabled": (0, 0, 0),

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

            # ----------------------- staticbox ----------------------- #

            "staticbox_bordercolour_default": (255, 0, 0),
            "staticbox_bordercolour_hover": (0, 255, 0),
            "staticbox_bordercolour_pressed": (0, 0, 255),
            "staticbox_bordercolour_disabled": (46, 31, 95),

            "staticbox_borderwidth_default": 2,
            "staticbox_borderwidth_hover": 8,
            "staticbox_borderwidth_pressed": 2,
            "staticbox_borderwidth_disabled": 4,

            "staticbox_borderstyle_default": "solid",
            "staticbox_borderstyle_hover": "solid",
            "staticbox_borderstyle_pressed": "solid",
            "staticbox_borderstyle_disabled": "solid",

            "staticbox_cornerradius_default": 10,
            "staticbox_cornerradius_hover": 10,
            "staticbox_cornerradius_pressed": 10,
            "staticbox_cornerradius_disabled": 10,
        }

        staticline_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 10000,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "hand",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # ----------------------- staticline ----------------------- #

            "staticline_bordercolour_default": (255, 0, 0),
            "staticline_bordercolour_hover": (0, 255, 0),
            "staticline_bordercolour_pressed": (0, 0, 255),
            "staticline_bordercolour_disabled": (46, 31, 95),

            "staticline_borderwidth_default": 2,
            "staticline_borderwidth_hover": 2,
            "staticline_borderwidth_pressed": 2,
            "staticline_borderwidth_disabled": 4,

            "staticline_borderstyle_default": "solid",
            "staticline_borderstyle_hover": "solid",
            "staticline_borderstyle_pressed": "solid",
            "staticline_borderstyle_disabled": "solid",
        }

        gauge_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 600,
            "colourtransition_ms_hover": 600,
            "colourtransition_ms_pressed": 600,
            
            "animation_ms": 200,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "cross",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # ------------------------- gauge ------------------------- #

            "gauge_backgroundcolour_default": (255, 255, 255),
            "gauge_backgroundcolour_hover": (255, 255, 255),
            "gauge_backgroundcolour_pressed": (255, 255, 255),
            "gauge_backgroundcolour_disabled": (231, 1, 202),

            "gauge_backgroundstyle_default": "solid",
            "gauge_backgroundstyle_hover": "solid",
            "gauge_backgroundstyle_pressed": "solid",
            "gauge_backgroundstyle_disabled": "solid",

            "gauge_bordercolour_default": (0, 0, 0),
            "gauge_bordercolour_hover": (0, 0, 0),
            "gauge_bordercolour_pressed": (0, 0, 0),
            "gauge_bordercolour_disabled": (46, 31, 95),

            "gauge_borderwidth_default": 2,
            "gauge_borderwidth_hover": 2,
            "gauge_borderwidth_pressed": 2,
            "gauge_borderwidth_disabled": 4,

            "gauge_borderstyle_default": "solid",
            "gauge_borderstyle_hover": "solid",
            "gauge_borderstyle_pressed": "solid",
            "gauge_borderstyle_disabled": "solid",

            "gauge_cornerradius_default": 3,
            "gauge_cornerradius_hover": 3,
            "gauge_cornerradius_pressed": 3,
            "gauge_cornerradius_disabled": 10,

            # ------------------------ progress ------------------------ #

            "progress_padding_default": 3,
            "progress_padding_hover": 3,
            "progress_padding_pressed": 3,
            "progress_padding_disabled": 3,

            "progress_startfrom": "left",

            "progress_backgroundcolour_default": (0, 255, 0),
            "progress_backgroundcolour_hover": (0, 255, 0),
            "progress_backgroundcolour_pressed": (0, 255, 0),
            "progress_backgroundcolour_disabled": (231, 1, 202),

            "progress_backgroundstyle_default": "solid",
            "progress_backgroundstyle_hover": "solid",
            "progress_backgroundstyle_pressed": "solid",
            "progress_backgroundstyle_disabled": "solid",

            "progress_bordercolour_default": (255, 0, 0),
            "progress_bordercolour_hover": (0, 255, 0),
            "progress_bordercolour_pressed": (0, 0, 255),
            "progress_bordercolour_disabled": (46, 31, 95),

            "progress_borderwidth_default": 2,
            "progress_borderwidth_hover": 2,
            "progress_borderwidth_pressed": 2,
            "progress_borderwidth_disabled": 4,

            "progress_borderstyle_default": "solid",
            "progress_borderstyle_hover": "solid",
            "progress_borderstyle_pressed": "solid",
            "progress_borderstyle_disabled": "solid",

            "progress_cornerradius_default": 3,
            "progress_cornerradius_hover": 3,
            "progress_cornerradius_pressed": 3,
            "progress_cornerradius_disabled": 10,
        }

        sp_style = {

            # ----------------------- animation ----------------------- #

            "colourtransition_ms_default": 1500,
            "colourtransition_ms_hover": 1500,
            "colourtransition_ms_pressed": 400,

            # ------------------------- cursor ------------------------- #

            "mousecursor_hover": "cross",
            "mousecursor_pressed": "arrow",
            "mousecursor_disabled": "arrow",

            # ------------------- track (background) ------------------- #

            "track_backgroundcolour_default": (0, 0, 0),
            "track_backgroundcolour_hover": (0, 0, 0),
            "track_backgroundcolour_pressed": (0, 0, 0),
            "track_backgroundcolour_disabled": (231, 1, 202),

            "track_backgroundstyle_default": "solid",
            "track_backgroundstyle_hover": "solid",
            "track_backgroundstyle_pressed": "solid",
            "track_backgroundstyle_disabled": "solid",

            "track_bordercolour_default": (255, 0, 0),
            "track_bordercolour_hover": (0, 255, 0),
            "track_bordercolour_pressed": (0, 0, 255),
            "track_bordercolour_disabled": (46, 31, 95),

            "track_borderwidth_default": 4,
            "track_borderwidth_hover": 30,
            "track_borderwidth_pressed": 4,
            "track_borderwidth_disabled": 4,

            "track_borderstyle_default": "solid",
            "track_borderstyle_hover": "solid",
            "track_borderstyle_pressed": "solid",
            "track_borderstyle_disabled": "solid",

            # ------------------- thumb (foreground) ------------------- #

            "thumb_padding_default": 3,
            "thumb_padding_hover": 3,
            "thumb_padding_pressed": 3,
            "thumb_padding_disabled": 3,

            "thumb_backgroundcolour_default": (255, 0, 0),
            "thumb_backgroundcolour_hover": (0, 255, 0),
            "thumb_backgroundcolour_pressed": (0, 0, 255),
            "thumb_backgroundcolour_disabled": (255, 255, 255),

            "thumb_backgroundstyle_default": "solid",
            "thumb_backgroundstyle_hover": "solid",
            "thumb_backgroundstyle_pressed": "solid",
            "thumb_backgroundstyle_disabled": "solid",

            "thumb_bordercolour_default": (255, 0, 0),
            "thumb_bordercolour_hover": (0, 255, 0),
            "thumb_bordercolour_pressed": (0, 0, 255),
            "thumb_bordercolour_disabled": (46, 31, 95),

            "thumb_borderwidth_default": 4,
            "thumb_borderwidth_hover": 30,
            "thumb_borderwidth_pressed": 4,
            "thumb_borderwidth_disabled": 4,

            "thumb_borderstyle_default": "solid",
            "thumb_borderstyle_hover": "solid",
            "thumb_borderstyle_pressed": "solid",
            "thumb_borderstyle_disabled": "solid",

            "thumb_cornerradius_default": 10,
            "thumb_cornerradius_hover": 10,
            "thumb_cornerradius_pressed": 10,
            "thumb_cornerradius_disabled": 10,
        }

        smooth = True

        # button = cc.Button(self.main_panel, label="test", config=button_style, use_smooth_transitions=smooth)
        # button.Bind(wx.EVT_BUTTON, lambda e: print("button pressed"))

        # checkbox = cc.CheckBox(self.main_panel, label="test checkbox", config=checkbox_style, pos=wx.Point(600, 0), use_smooth_transitions=smooth)
        # checkbox.Bind(wx.EVT_CHECKBOX, lambda e: print("checkbox pressed"))

        # radiobutton = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(10, 250), style=wx.RB_GROUP, use_smooth_transitions=smooth)
        # radiobutton.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton pressed"))
        # radiobutton1 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(210, 250), use_smooth_transitions=smooth)
        # radiobutton1.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton1 pressed"))
        # radiobutton2 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(410, 250), use_smooth_transitions=smooth)
        # radiobutton2.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton2 pressed"))
        # button1 = cc.Button(self.main_panel, label="change radiobutton value", config=button_style, pos=wx.Point(610, 250), use_smooth_transitions=smooth)
        # button1.Bind(wx.EVT_BUTTON, lambda e: radiobutton1.SetValue(True))

        # panel = cc.Panel(self.main_panel, config=panel_style, pos=wx.Point(10, 380), size=wx.Size(300, 110), use_defaults=False, use_smooth_transitions=smooth)
        # checkbox2 = cc.CheckBox(panel, label="inside panel", config=checkbox_style, pos=wx.Point(10, 10), use_smooth_transitions=smooth)
        # checkbox2.Bind(wx.EVT_ENTER_WINDOW, panel._on_enter_window)
        # checkbox2.Bind(wx.EVT_LEAVE_WINDOW, panel._on_leave_window)

        # staticbox = cc.StaticBox(self.main_panel, label="test", config=staticbox_style, pos=wx.Point(200, 10), size=wx.Size(200, 200), use_smooth_transitions=smooth, use_defaults=False)
        # staticbox_panel = staticbox.GetPanel()
        # staticbox_button = wx.Button(staticbox_panel, label="staticbox content")

        # staticline = cc.StaticLine(self.main_panel, use_defaults=False, style=wx.LI_HORIZONTAL, config=staticline_style, pos=wx.Point(200, 220), size=wx.Size(300, 70), use_smooth_transitions=smooth)


        # ------------------------- gauge ------------------------- #
        
        # gauge = cc.Gauge(self.main_panel, pos=(10, 10), size=(300, 60), config=gauge_style, use_smooth_transitions=smooth, use_defaults=False, style=wx.GA_HORIZONTAL)
        # gauge.SetRange(100)

        # self.val = 0
        
        # def test(event):

        #     self.val += 10
        #     if self.val > 100:
        #         self.val = 0
        #     gauge.SetValue(self.val)

        # b = wx.Button(self.main_panel, pos=(10, 60))
        # b.Bind(wx.EVT_BUTTON, test)

        # --------------------- scrolled panel --------------------- #

        sp = cc.ScrolledPanel(self.main_panel, pos=(10, 10), size=(300, 300), config=sp_style)
        sp_panel = sp.GetPanel()
        sp_sizer = wx.GridBagSizer()
        for i in range(50):
            sp_sizer.Add(wx.Button(sp_panel, label="test"), pos=(i, 0))
        sp_panel.SetSizer(sp_sizer)

        self.main_sizer.Add(sp, proportion=1, flag=wx.EXPAND)

        self.main_sizer.Layout()

        

        
        
if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
