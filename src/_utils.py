"""_utils.py

wxCustomizableControls
16/dec/2024
cenfra
"""


from typing import Union, Tuple
import wx


class VectorRGB:
    """This class represents an RGB color with channels within the
    range (-255 - 255). Negative values are included because this
    class is also used to represent change in color.

    All operations involving two of these vectors are element-wise.
    """
    def __init__(self,
                 r: Union[int, float],
                 g: Union[int, float],
                 b: Union[int, float]):
        self.r = self._check_legal(r)
        self.g = self._check_legal(g)
        self.b = self._check_legal(b)

    @staticmethod
    def _check_legal(channel_value: Union[int, float]) -> int:
        """Returns the integer value of the channel if its value is
        within range (-255 - 255). Raises ValueError otherwise.
        """
        if (-255 <= channel_value <= 255):
            return int(channel_value)
        else:
            raise ValueError("VectorRGB input rgb value is out of range.")

    def _cap_value(self, channel_value: Union[int, float]) -> int:
        """Limits the value if out of range and returns its integer
        value.
        """
        if channel_value < -255:
            return 0
        elif channel_value > 255:
            return 255
        else:
            return int(channel_value)

    def __add__(self, other):
        if isinstance(other, VectorRGB):
            r = self._cap_value(self.r + other.r)
            g = self._cap_value(self.g + other.g)
            b = self._cap_value(self.b + other.b)
            return VectorRGB(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            return VectorRGB(self._cap_value(self.r + other),
                             self._cap_value(self.g + other),
                             self._cap_value(self.b + other))
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, VectorRGB):
            r = self._cap_value(self.r - other.r)
            g = self._cap_value(self.g - other.g)
            b = self._cap_value(self.b - other.b)
            return VectorRGB(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            return VectorRGB(self._cap_value(self.r - other),
                             self._cap_value(self.g - other),
                             self._cap_value(self.b - other))
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, VectorRGB):
            r = self._cap_value(self.r * other.r)
            g = self._cap_value(self.g * other.g)
            b = self._cap_value(self.b * other.b)
            return VectorRGB(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            return VectorRGB(self._cap_value(self.r * other),
                             self._cap_value(self.g * other),
                             self._cap_value(self.b * other))
        raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, VectorRGB):
            r = self._cap_value(self.r / other.r)
            g = self._cap_value(self.g / other.g)
            b = self._cap_value(self.b / other.b)
            return VectorRGB(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            return VectorRGB(self._cap_value(self.r / other),
                             self._cap_value(self.g / other),
                             self._cap_value(self.b / other))
        raise NotImplementedError

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        if isinstance(other, VectorRGB):
            return (self.r == other.r) and (self.g == other.g) and (self.b == other.b)
        return False
    
    def __repr__(self):
        return f"VectorRGB({self.r}, {self.g}, {self.b})"

    def GetRGB(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    def GetValue(self) -> wx.Colour:
        return wx.Colour(self.r, self.g, self.b)
    
