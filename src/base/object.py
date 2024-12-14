"""object.py

The CustomizableObject class will be inherited from all of the
customizable objects in the library (both controls and other windows
which are not controls, like panels). This class will keep track of
the object's configuration data and also include methods to modify
this data.

The CustomizableObject class will also include useful methods used
during the drawing process.

"""


from copy import copy
from typing import Tuple
import wx


class CustomizableObject:
    def __init__(self, config: dict):
        self._config = copy(config)

        # --------------------- object states --------------------- #

        self._Enabled = True
        self._Pressed = False
        self._Hover = False
        

    def SetConfig(self, config: dict):
        self._config = config

    def GetConfig(self):
        return self._config

    def _get_drawing_contexts(self, window=None) -> Tuple[wx.GCDC, wx.GraphicsContext]:
        """Creates the BufferedPaintDC and returns the GCDC with its
        GraphicsContext reference.
        """
        window = window if window else self
        dc = wx.BufferedPaintDC(window)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        return gcdc, gc

    

    


    
        

    

    

    

    
