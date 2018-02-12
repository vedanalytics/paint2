import copy
from Modules.layout.layout import Layout
from Modules.rectangle.rectangle import Rectangle
from Modules.line.line import Line
from Modules.fill_color.fill_color import FillColor
from utils import config
from paint_validations import PaintValidations
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class PaintUtils:
    def __init__(self, max_width=None, max_height=None):
        self._layout_matrix = []
        self._max_width = max_width if max_width > 0 else config.OUTER_LAYOUT['max_width']
        self._max_height = max_height if max_height > 0 else config.OUTER_LAYOUT['max_height']
        self.SHAPES = {
            "line": "L",
            "rectangle": "R",
            "fill_color": "B"
        }
        self._rectangle_border = config.RECTANGLE['border']
        self._line_border = config.LINE['border']

    is_input_overflown = False

    def draw_layout(self, width, height):
        """
        Draw Layout

        Draws layout using width and height
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        width:
        height:

        Returns
        -------
        Layout Matrix

        """
        layout = Layout(width, height, self._max_width, self._max_height)
        layout_matrix = layout.draw_shape()
        self._layout_matrix = layout_matrix
        return layout_matrix

    def draw_line(self, x1, y1, x2, y2, char=None):
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
        layout = copy.deepcopy(self._layout_matrix)
        line = Line(layout)
        layout_matrix = line.draw_shape(x1, y1, x2, y2, char)
        self._layout_matrix = layout_matrix
        return layout_matrix

    def draw_rectangle(self, x1, y1, x2, y2, char=None):
        """
        Draw Rectangle

        Draw Rectangle from given inputs and border char.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x1 : int
            x1 of Rectangle
        y1 : int
            x1 of Rectangle
        x2 : int
            y1 of Rectangle
        y2 : int
            y2 of Rectangle
        char : str
            char, which is border of Rectangle

        Returns
        -------
        Layout Matrix with Rectangle added inside

        """
        layout = copy.deepcopy(self._layout_matrix)
        rectangle = Rectangle(layout)
        layout_matrix = rectangle.draw_shape(x1, y1, x2, y2, char)
        self._layout_matrix = layout_matrix
        return layout_matrix

    def fill_color(self, x, y, color):
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
        layout = copy.deepcopy(self._layout_matrix)
        fill_color = FillColor(layout)
        layout_matrix = fill_color.draw_shape(x, y, color)
        self._layout_matrix = copy.deepcopy(layout_matrix)
        return layout_matrix

    def render(self, layout):
        if not self.is_input_overflown:
            for item in layout:
                print(''.join(item))

    def draw(self, input_cmd):
        _paint_validations = PaintValidations()
        is_input_valid, cmd = _paint_validations.validate_and_reshape_input(input_cmd)
        shape = str(cmd[0])
        if is_input_valid:
            if shape == 'C':
                return self.draw_layout(int(cmd[1]), int(cmd[2]))
            elif shape == 'L':
                return self.draw_line(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]), self._line_border)
            elif shape == 'R':
                return self.draw_rectangle(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]), self._rectangle_border)
            elif shape == 'B':
                return self.fill_color(int(cmd[1]), int(cmd[2]), cmd[3])
