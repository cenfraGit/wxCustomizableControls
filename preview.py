"""preview.py

A frame with customizable control examples.

wxCustomizableControls
cenfra
"""


import platform
import wxCustomizableControls as cc
import wx

# --------------------- platform setup --------------------- #

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
# elif platform.system() == "Linux":
#     import os
#     os.environ["GDK_BACKEND"] = "x11"


class Main(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_ui()


    def __init_ui(self):
        """Initializes the user interface."""

        self.SetTitle("wxCustomizableControls Preview")
        self.SetClientSize(wx.Size(900, 500))

        self.frame_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.frame_sizer)

        scrolledpanel = cc.ScrolledPanel(self)
        self.panel = scrolledpanel.GetPanel()
        self.sizer = wx.GridBagSizer()
        self.panel.SetSizer(self.sizer)

        # --------------------- panel configs --------------------- #

        config_panel = cc.Config(
            panel_borderwidth_default = 2,
            panel_cornerradius_default = 5,
        )

        # ------------------------ buttons ------------------------ #

        panel_buttons = cc.Panel(self.panel, config=config_panel)
        panel_buttons_sizer = wx.GridBagSizer()
        panel_buttons.SetSizer(panel_buttons_sizer)

        b1 = cc.Button(panel_buttons, label="Test")

        b2 = cc.Button(panel_buttons, label="Test",
                       # background colour
                       button_backgroundcolour_default=(0, 0, 0),
                       button_backgroundcolour_hover=(0, 0, 0),
                       button_backgroundcolour_pressed=(0, 0, 0),
                       # border colour
                       button_bordercolour_default=(255, 0, 0),
                       button_bordercolour_hover=(0, 255, 0),
                       button_bordercolour_pressed=(0, 0, 255),
                       # border width
                       button_borderwidth_default=3,
                       button_borderwidth_hover=3,
                       button_borderwidth_pressed=3,
                       # font colour
                       fontcolour_default=(200, 200, 200),
                       fontcolour_hover=(200, 200, 200),
                       fontcolour_pressed=(200, 200, 200))

        b3 = cc.Button(panel_buttons, label="Test",
                       # background colour
                       button_backgroundcolour_default=(255, 255, 255),
                       button_backgroundcolour_hover=(255, 255, 255),
                       button_backgroundcolour_pressed=(255, 255, 255),
                       # border colour
                       button_bordercolour_default=(255, 255, 255),
                       button_bordercolour_hover=(50, 50, 50),
                       button_bordercolour_pressed=(0, 0, 0),
                       # border width
                       button_borderwidth_default=1,
                       button_borderwidth_hover=2,
                       button_borderwidth_pressed=4,
                       # font colour
                       fontcolour_default=(0, 0, 0),
                       fontcolour_hover=(0, 0, 0),
                       fontcolour_pressed=(0, 0, 0))

        b4 = cc.Button(panel_buttons, label="Test",
                       # background colour
                       button_backgroundcolour_default=(0, 50, 100, 60, (52, 72, 160), (160, 72, 52)),
                       button_backgroundcolour_hover=(255, 255, 255),
                       button_backgroundcolour_pressed=(255, 255, 255),
                       # border colour
                       button_bordercolour_default=(255, 255, 255),
                       button_bordercolour_hover=(50, 50, 50),
                       button_bordercolour_pressed=(0, 0, 0),
                       # border width
                       button_borderwidth_default=1,
                       button_borderwidth_hover=2,
                       button_borderwidth_pressed=4,
                       # font colour
                       fontcolour_default=(0, 0, 0),
                       fontcolour_hover=(0, 0, 0),
                       fontcolour_pressed=(0, 0, 0))

        b5 = cc.Button(panel_buttons, label="Test",
                       image_path_default="images/example.png",
                       image_width_default=40,
                       image_height_default=40)

        b6 = cc.Button(panel_buttons, label="Test",
                       image_path_default="images/example.png",
                       image_width_default=40,
                       image_height_default=40,
                       image_side="top")

        b7 = cc.Button(panel_buttons, label="Test",
                       image_path_default="images/example.png",
                       image_width_default=40,
                       image_height_default=40,
                       image_side="bottom")

        b8 = cc.Button(panel_buttons, label="Test",
                       image_path_default="images/example.png",
                       image_width_default=40,
                       image_height_default=40,
                       image_side="right")

        # add buttons to sizer
        panel_buttons_sizer.Add(b1, pos=(0, 0), flag=wx.EXPAND|wx.LEFT|wx.TOP, border=10)
        panel_buttons_sizer.Add(b2, pos=(0, 1), flag=wx.EXPAND|wx.LEFT|wx.TOP, border=10)
        panel_buttons_sizer.Add(b3, pos=(0, 2), flag=wx.EXPAND|wx.LEFT|wx.TOP, border=10)
        panel_buttons_sizer.Add(b4, pos=(0, 3), flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT, border=10)
        
        panel_buttons_sizer.Add(b5, pos=(1, 0), flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        panel_buttons_sizer.Add(b6, pos=(1, 1), flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        panel_buttons_sizer.Add(b7, pos=(1, 2), flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        panel_buttons_sizer.Add(b8, pos=(1, 3), flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=10)

        panel_buttons_sizer.AddGrowableCol(0, 1)
        panel_buttons_sizer.AddGrowableCol(1, 1)
        panel_buttons_sizer.AddGrowableCol(2, 1)
        panel_buttons_sizer.AddGrowableCol(3, 1)

        panel_buttons_sizer.Layout()

        # ---------------- checkboxes and switches ---------------- #

        panel_checkboxes = cc.Panel(self.panel, config=config_panel)
        panel_checkboxes_sizer = wx.GridBagSizer()
        panel_checkboxes.SetSizer(panel_checkboxes_sizer)

        c1 = cc.CheckBox(panel_checkboxes, label="Test")

        c2 = cc.CheckBox(panel_checkboxes, label="Test",
                         checkbox_width=30,
                         checkbox_height=30,
                         checkbox_cornerradius_default=4,
                         checkbox_cornerradius_hover=2,
                         checkbox_borderwidth_default=3,
                         checkbox_bordercolour_default=(255, 0, 0),
                         checkbox_bordercolour_hover=(0, 255, 0),
                         checkbox_bordercolour_pressed=(0, 0, 255),
                         checkbox_backgroundcolour_hover=(50, 50, 50),
                         checkbox_backgroundcolour_pressed=(0, 0, 0),
                         fontweight_default="bold")

        c3 = cc.Switch(panel_checkboxes, label="Test",
                       selectionmarker_rounded=False)

        c4 = cc.Switch(panel_checkboxes, label="Test",
                       selectionmarker_rounded=True,
                       switch_cornerradius_default=8)

        # add checkboxes to sizer
        panel_checkboxes_sizer.Add(c1, pos=(0, 0), flag=wx.EXPAND|wx.BOTTOM|wx.LEFT|wx.TOP, border=10)
        panel_checkboxes_sizer.Add(c2, pos=(0, 1), flag=wx.EXPAND|wx.BOTTOM|wx.LEFT|wx.TOP, border=10)
        panel_checkboxes_sizer.Add(c3, pos=(0, 2), flag=wx.EXPAND|wx.BOTTOM|wx.LEFT|wx.TOP, border=10)
        panel_checkboxes_sizer.Add(c4, pos=(0, 3), flag=wx.EXPAND|wx.BOTTOM|wx.LEFT|wx.TOP|wx.RIGHT, border=10)
        
        panel_checkboxes_sizer.AddGrowableCol(0, 1)
        panel_checkboxes_sizer.AddGrowableCol(1, 1)
        panel_checkboxes_sizer.AddGrowableCol(2, 1)
        panel_checkboxes_sizer.AddGrowableCol(3, 1)

        panel_checkboxes_sizer.Layout()

        # ------------------------- gauges ------------------------- #

        panel_gauges = cc.Panel(self.panel, config=config_panel)
        panel_gauges_sizer = wx.BoxSizer()
        panel_gauges.SetSizer(panel_gauges_sizer)

        self.g1 = cc.Gauge(panel_gauges, size=wx.Size(-1, 50))
        self.g1_value = 0
        
        self.timer_gauges = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_gauge, self.timer_gauges)
        self.timer_gauges.Start(1000)

        panel_gauges_sizer.Add(self.g1, 1, wx.ALL, border=10)
        panel_gauges_sizer.Layout()

        # ------------------- statictext wrapped ------------------- #

        sample = ("I spill remy on imaginary graves, put my hat on my waves, "
                  "latter day saints say religious praise, heat graze the baby, yo, "
                  "foul shit made a welfare mom crazy, more bodies drop by the ratio, "
                  "paces blow, grizzly thoughts for makin doe, haitian bitch cast a "
                  "spell on my life for cash flow, so now it's on, never wasted a slug, "
                  "time is money, when it comes to mine, take it in blood!")

        panel_statictext = cc.Panel(self.panel, config=config_panel)
        panel_statictext_sizer = wx.BoxSizer()
        panel_statictext.SetSizer(panel_statictext_sizer)

        st = cc.StaticText(panel_statictext, label=sample, wordwrap=True, size=wx.Size(600, -1))

        panel_statictext_sizer.Add(st, 1, wx.ALL, border=10)
        panel_statictext_sizer.Layout()

        # ---------------------- radiobutton ---------------------- #

        panel_radiobuttons = cc.Panel(self.panel, config=config_panel)
        panel_radiobuttons_sizer = wx.BoxSizer()
        panel_radiobuttons.SetSizer(panel_radiobuttons_sizer)

        rad1 = cc.RadioButton(panel_radiobuttons, label="Test1", style=wx.RB_GROUP)
        rad2 = cc.RadioButton(panel_radiobuttons, label="Test2")
        rad3 = cc.RadioButton(panel_radiobuttons, label="Test3")
        rad4 = cc.RadioButton(panel_radiobuttons, label="Test4")

        panel_radiobuttons_sizer.Add(rad1, 1, wx.ALL|wx.ALIGN_LEFT, border=10)
        panel_radiobuttons_sizer.Add(rad2, 1, wx.ALL|wx.ALIGN_LEFT, border=10)
        panel_radiobuttons_sizer.Add(rad3, 1, wx.ALL|wx.ALIGN_LEFT, border=10)
        panel_radiobuttons_sizer.Add(rad4, 1, wx.ALL|wx.ALIGN_LEFT, border=10)
        panel_radiobuttons_sizer.Layout()

        # ------------------------ combobox ------------------------ #

        panel_combobox = cc.Panel(self.panel, config=config_panel)
        panel_combobox_sizer = wx.BoxSizer()
        panel_combobox.SetSizer(panel_combobox_sizer)

        options = ["option1", "option2", "option3"]

        combo = cc.ComboBox(panel_combobox, value="option1", choices=options)

        panel_combobox_sizer.Add(combo, 1, wx.ALL|wx.ALIGN_LEFT, border=10)
        panel_combobox_sizer.Layout()

        # ------------------ scrolled panel sizer ------------------ #

        self.sizer.Add(panel_buttons, pos=(0, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)
        self.sizer.Add(panel_checkboxes, pos=(1, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)
        self.sizer.Add(panel_gauges, pos=(2, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)
        self.sizer.Add(panel_radiobuttons, pos=(3, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)
        self.sizer.Add(panel_combobox, pos=(4, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)
        self.sizer.Add(panel_statictext, pos=(5, 0), border=10, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT)

        self.sizer.AddGrowableCol(0, 1)
        self.sizer.Layout()

        # --------------- add scrolledpanel to sizer --------------- #

        self.frame_sizer.Add(scrolledpanel, proportion=1, flag=wx.EXPAND)
        self.frame_sizer.Layout()

    def update_gauge(self, event):
        change = 10
        if self.g1_value + change <= 100:
            self.g1_value += change
        else:
            self.g1_value = 0
        self.g1.SetValue(self.g1_value)

        
        
if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
