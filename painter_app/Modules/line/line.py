from painter_app.utils import painter_utils
from painter_app.utils import config
from .line_validations import LineValidations
import sys
import os
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class Line:
    def __init__(self, layout):
        self._layout = layout
        self._layout_height = len(layout) if len(layout) > 0 else 0
        self._layout_width = len(self._layout[0]) if len(self._layout) > 0 else 0
        self._border_char = config.LINE['border']

    def draw_shape(self, x1, y1, x2, y2, char=None):
        """
        Draw Line

        Draw Line for given inputs and border char.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x1 : int
            x1 of Line
        y1 : int
            x1 of Line
        x2 : int
            y1 of Line
        y2 : int
            y2 of Line
        char : str
            char, which is border of Line

        Returns
        -------
        Layout Matrix with Line added inside

        """
        char = char if char is not None and len(char) > 0 else self._border_char
        outer_layout = copy.deepcopy(self._layout)
        _validations = LineValidations(outer_layout, x1, y1, x2, y2)
        _validations.validate_line()
        x1, y1, x2, y2 = painter_utils.order_inputs(x1, y1, x2, y2)
        outer_layout = self.__draw_line(outer_layout, x1, y1, x2, y2, char)
        return outer_layout

    def __draw_line(self, layout, x1, y1, x2, y2, char):
        if y1 == y2:
            line = copy.deepcopy(layout[y1])
            line = painter_utils.update_line(line, x1, x2, char, char, char)
            layout[y1] = line
        elif x1 == x2:
            for i in range(y1, y2 + 1):
                line = copy.deepcopy(layout[x1])
                line = painter_utils.update_line(line, x1, x1, char, char, char)
                layout[i] = line
        else:
            x = x1
            for i in range(y1, y2 + 1):
                line = copy.deepcopy(layout[i])
                line = painter_utils.update_line(line, x, x, char, char, char)
                layout[i] = line
                x += 1
        return layout
