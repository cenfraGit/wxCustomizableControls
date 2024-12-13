# example.py
# a frame with customizable control examples.
# 12/dec/2024
# wxCustomizableControls



import wx



class Main(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_ui()


        
    def __init_ui(self):

        """Initializes the user interface."""

        self.SetTitle("wxCustomizableControls Examples")
        self.SetMinClientSize(wx.Size(600, 300))
        
        pass


                
        
if __name__ == "__main__":
    app = wx.App()
    instance = Main(None)
    instance.Show()
    app.MainLoop()
