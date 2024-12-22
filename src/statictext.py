"""statictext.py

wxCustomizableControls
22/dec/2024
cenfra
"""


from ._window import Window
import wx


class StaticText(Window):
    def __init__(self, parent, id=wx.ID_ANY, label="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0,name=wx.StaticTextNameStr, config={}, **kwargs):

        # ------------------- control attributes ------------------- #
        
        kwargs["label"] = label

        if "use_defaults" not in kwargs.keys():
            kwargs["use_defaults"] = True

        self._WordWrap = kwargs.get("wordwrap", False)

        # ------------------- initialize window ------------------- #
        
        super().__init__(parent, id, pos, size, style, name, config, **kwargs)

    def _on_paint(self, event: wx.Event) -> None:

        # ------------ drawing contexts and background ------------ #
        
        gcdc, gc = self._get_drawing_contexts(self)
        gcdc.Clear()

        drawing_rect: wx.Rect = self.GetClientRect()
        gcdc.SetPen(wx.TRANSPARENT_PEN)
        gc.SetBrush(self._get_brush_parent_background())
        gcdc.DrawRectangle(drawing_rect)

        # ----------------------- draw words ----------------------- #

        gc.SetFont(*self._get_font())

        if self._WordWrap:

            horizontal_offset = 0
            vertical_offset = 0

            width_limit = self.GetSize()[0]
            
            words_list = self._Label.split(' ')

            space_width, space_height = gcdc.GetTextExtent(' ')
            
            for word in words_list:
                width, height = gcdc.GetTextExtent(word)

                if (horizontal_offset + width) < width_limit:
                    gcdc.DrawText(word, horizontal_offset, vertical_offset)
                else:
                    vertical_offset += height
                    horizontal_offset = 0
                    gcdc.DrawText(word, horizontal_offset, vertical_offset)

                gcdc.DrawText(' ', horizontal_offset, vertical_offset)
                horizontal_offset += space_width

                horizontal_offset += width

            # update panel size
            self.SetSize(wx.Size(-1, vertical_offset + space_height))

        else:     
            gcdc.DrawText(self._Label, 0, 0)

        # # ---------------------- mouse cursor ---------------------- #
        
        # self._configure_cursor()

    def DoGetBestClientSize(self):
        # get contexts
        dc = wx.ClientDC(self)
        gcdc = wx.GCDC(dc)
        gc: wx.GraphicsContext = gcdc.GetGraphicsContext()
        # get max dimensions
        width, height = self._get_text_dimensions(self._Label, gc)
        # padding
        width += 10
        height += 10
        if not self._WordWrap:
            return wx.Size(int(width), int(height))
        else:

            gc.SetFont(*self._get_font())
            
            horizontal_offset = 0
            vertical_offset = 0

            width_limit = self.GetSize()[0]
            
            words_list = self._Label.split(' ')

            space_width, space_height = gcdc.GetTextExtent(' ')
            
            for word in words_list:
                width, height = gcdc.GetTextExtent(word)

                if (horizontal_offset + width) < width_limit:
                    gcdc.DrawText(word, horizontal_offset, vertical_offset)
                else:
                    vertical_offset += height
                    horizontal_offset = 0
                    gcdc.DrawText(word, horizontal_offset, vertical_offset)

                gcdc.DrawText(' ', horizontal_offset, vertical_offset)
                horizontal_offset += space_width

                horizontal_offset += width

            # update panel size
            return wx.Size(-1, vertical_offset + space_height)
