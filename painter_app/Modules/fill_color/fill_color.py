from painter_app.utils import config
from .fill_color_validations import FillColorValidations
import sys
import os
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class FillColor:
    def __init__(self, layout):
        self._layout = layout
        self._to_replace = config.OUTER_LAYOUT['middle_char']

    def draw_shape(self, x, y, color):
        """
        Fill Area with given color

        Fills the area around given space using given color.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x : int
            x in space
        y : int
            y in space
        color : str
            color to fill space
        Returns
        -------
        Layout matrix filled with color from x,y

        """
        outer_layout = copy.deepcopy(self._layout)
        _validations = FillColorValidations(outer_layout, x, y)
        _validations.validate_fill_color()
        outer_layout = self.__draw_fill_color(outer_layout, x, y, color, self._to_replace)
        return outer_layout

    def __draw_fill_color(self, layout, x, y, color, to_replace):
        height = len(layout)-2 if len(layout) > 0 else 0
        width = len(layout[0]) if len(layout) > 0 else 0
        to_fill = set()
        to_fill.add((x, y))
        while to_fill:
            x, y = to_fill.pop()
            if not (1 <= x <= width and 1 <= y <= height):
                continue
            value = copy.deepcopy(layout[x][y])
            if value != to_replace:
                continue
            layout[x][y] = color
            to_fill.add((x - 1, y))
            to_fill.add((x + 1, y))
            to_fill.add((x, y - 1))
            to_fill.add((x, y + 1))
        return layout
