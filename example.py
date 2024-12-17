"""example.py

A frame with customizable control examples.

wxCustomizableControls
cenfra
"""


import platform
import src as cc
import wx


if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)


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

            # -------------------- colour transition -------------------- #

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

            "button_borderwidth_default": 40,
            "button_borderwidth_hover": 8,
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

            # -------------------- colour transition -------------------- #

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

            "checkbox_borderwidth_default": 2,
            "checkbox_borderwidth_hover": 2,
            "checkbox_borderwidth_pressed": 2,
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

            # -------------------- colour transition -------------------- #

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

            # -------------------- colour transition -------------------- #

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
            "panel_borderwidth_hover": 2,
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

            # -------------------- colour transition -------------------- #

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
            "staticbox_borderwidth_hover": 2,
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

            # -------------------- colour transition -------------------- #

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

        smooth = True

        button = cc.Button(self.main_panel, label="test", config=button_style, use_smooth_transitions=smooth)
        button.Bind(wx.EVT_BUTTON, lambda e: print("button pressed"))

        checkbox = cc.CheckBox(self.main_panel, label="test checkbox", config=checkbox_style, pos=wx.Point(10, 100), use_smooth_transitions=smooth)
        checkbox.Bind(wx.EVT_CHECKBOX, lambda e: print("checkbox pressed"))

        radiobutton = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(10, 250), style=wx.RB_GROUP, use_smooth_transitions=smooth)
        radiobutton.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton pressed"))
        radiobutton1 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(210, 250), use_smooth_transitions=smooth)
        radiobutton1.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton1 pressed"))
        radiobutton2 = cc.RadioButton(self.main_panel, label="test radiobutton", config=radiobutton_style, pos=wx.Point(410, 250), use_smooth_transitions=smooth)
        radiobutton2.Bind(wx.EVT_RADIOBUTTON, lambda e: print("radiobutton2 pressed"))
        button1 = cc.Button(self.main_panel, label="change radiobutton value", config=button_style, pos=wx.Point(610, 250), use_smooth_transitions=smooth)
        button1.Bind(wx.EVT_BUTTON, lambda e: radiobutton1.SetValue(True))

        panel = cc.Panel(self.main_panel, config=panel_style, pos=wx.Point(10, 380), size=wx.Size(300, 110), use_defaults=False, use_smooth_transitions=smooth)
        checkbox2 = cc.CheckBox(panel, label="inside panel", config=checkbox_style, pos=wx.Point(10, 10), use_smooth_transitions=smooth)
        checkbox2.Bind(wx.EVT_ENTER_WINDOW, panel._on_enter_window)
        checkbox2.Bind(wx.EVT_LEAVE_WINDOW, panel._on_leave_window)

        staticbox = cc.StaticBox(self.main_panel, label="test", config=staticbox_style, pos=wx.Point(200, 10), size=wx.Size(200, 200), use_smooth_transitions=smooth, use_defaults=False)
        staticbox_panel = staticbox.GetPanel()
        staticbox_button = wx.Button(staticbox_panel, label="staticbox content")

        staticline = cc.StaticLine(self.main_panel, use_defaults=False, style=wx.LI_HORIZONTAL, config=staticline_style, pos=wx.Point(200, 220), size=wx.Size(300, 70), use_smooth_transitions=smooth)

        


        
if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
