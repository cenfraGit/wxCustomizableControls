# example.py
# a frame with customizable control examples.
# 12/dec/2024
# wxCustomizableControls



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
        #self.main_panel.SetBackgroundColour(wx.WHITE)

        b_style = {
            'backgroundcolor_drawingarea_default': (182, 30, 62),
            'backgroundcolor_drawingarea_hover': (224, 203, 224),
            'backgroundcolor_drawingarea_pressed': (124, 185, 182),
            'backgroundcolor_drawingarea_disabled': (231, 1, 202),

            'backgroundstyle_drawingarea_default': 'solid',
            'backgroundstyle_drawingarea_hover': 'solid',
            'backgroundstyle_drawingarea_pressed': 'solid',
            'backgroundstyle_drawingarea_disabled': 'solid',

            'bordercolor_drawingarea_default': (29, 11, 175),
            'bordercolor_drawingarea_hover': (195, 15, 132),
            'bordercolor_drawingarea_pressed': (48, 221, 224),
            'bordercolor_drawingarea_disabled': (46, 31, 95),

            'borderwidth_drawingarea_default': 1,
            'borderwidth_drawingarea_hover': 2,
            'borderwidth_drawingarea_pressed': 3,
            'borderwidth_drawingarea_disabled': 4,

            'borderstyle_drawingarea_default': 'solid',
            'borderstyle_drawingarea_hover': 'solid',
            'borderstyle_drawingarea_pressed': 'solid',
            'borderstyle_drawingarea_disabled': 'solid',

            # ------------------------- button ------------------------- #

            'backgroundcolor_button_default': (255, 255, 0),
            'backgroundcolor_button_hover': (224, 203, 224),
            'backgroundcolor_button_pressed': (124, 185, 182),
            'backgroundcolor_button_disabled': (231, 1, 202),

            'backgroundstyle_button_default': 'solid',
            'backgroundstyle_button_hover': 'solid',
            'backgroundstyle_button_pressed': 'solid',
            'backgroundstyle_button_disabled': 'solid',

            'bordercolor_button_default': (29, 11, 175),
            'bordercolor_button_hover': (195, 15, 132),
            'bordercolor_button_pressed': (48, 221, 224),
            'bordercolor_button_disabled': (46, 31, 95),

            'borderwidth_button_default': 1,
            'borderwidth_button_hover': 2,
            'borderwidth_button_pressed': 3,
            'borderwidth_button_disabled': 4,

            'borderstyle_button_default': 'solid',
            'borderstyle_button_hover': 'solid',
            'borderstyle_button_pressed': 'solid',
            'borderstyle_button_disabled': 'solid',

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
            "path_image_hover": "",
            "path_image_pressed": "",
            "path_image_disabled": "",

            "width_image_default": 80,
            "width_image_hover": 10,
            "width_image_pressed": 10,
            "width_image_disabled": 10,

            "height_image_default": 80, 
            "height_image_hover": 10,
            "height_image_pressed": 10,
            "height_image_disabled": 10,

            "channels_image_default": (1.0, 1.0, 1.0, 1.0),
            "channels_image_hover": (1.0, 1.0, 1.0, 1.0),
            "channels_image_pressed": (1.0, 1.0, 1.0, 1.0),
            "channels_image_disabled": (1.0, 1.0, 1.0, 1.0),

            "separation_image_default": 10,
            "separation_image_hover": 10,
            "separation_image_pressed": 10,
            "separation_image_disabled": 10,

            "side_image_default": "left",
            "side_image_hover": "left",
            "side_image_pressed": "left",
            "side_image_disabled": "left",
        }

        cc.Button(self.main_panel, label="test", config=b_style)

                
        
if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
