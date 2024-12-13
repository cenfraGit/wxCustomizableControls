"""object.py

This module contains two classes:

The DrawingTools class contains methods used while in the drawing
process for the customizable objects, like getting the appropiate pen
and brush for the current task, calculating coordinates for images and
text which are side by side, etc.

The CustomizableObject class will be inherited from all of the
customizable objects in the library (both controls and other windows
which are not controls, like panels). This class will keep track of
the object's configuration data and also include methods to modify
this data.

The CustomizableObject class will also inherit the methods from the
DrawingTools class, so all customizable objects in the library will
have access to these tools.
"""


import wx
from typing import Tuple


class DrawingTools:

    def _get_drawing_contexts(self, window=None) -> Tuple[wx.GCDC, wx.GraphicsContext]:
        """Creates the BufferedPaintDC and returns the GCDC with its
        GraphicsContext reference.
        """
        window = window if window else self
        dc = wx.BufferedPaintDC(window)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        return gcdc, gc


class Object
