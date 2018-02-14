import unittest
from painter_app.Modules.layout.layout import Layout
from painter_app.Modules.line.line import Line
from painter_app.Modules.fill_color.fill_color import FillColor
from painter_app.Modules.rectangle.rectangle import Rectangle


class TestModules(unittest.TestCase):
    _layout = ['------------',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '------------']

    _layout_height = 10
    _layout_width = 10
    _border_char = 'X'
    _layout_array = [list(item) for item in _layout]

    def test_draw_rect1(self):
        rect =  ['------------',
                 '|XXXX......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|XXXX......|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '------------']
        rect_array = [list(item) for item in rect]
        rect_obj = Rectangle(self._layout_array)
        output = rect_obj.draw_shape(1,1,4,5, self._border_char)
        self.assertEqual(len(rect_array), len(output))
        print('Testing if rectangle is aded in layout')

    def test_draw_rect2(self):
        rect =  ['------------',
                 '|XXXX......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|XXXX......|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '------------']
        rect_obj = Rectangle(self._layout_array)
        output = rect_obj.draw_shape(1,1,4,5, self._border_char)
        self.assertEqual(rect[1], ''.join(output[1]))
        print('Testing Rectangle dimensions')

    def test_draw_rect3(self):
        rect =  ['------------',
                 '|XXXX......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|XXXX......|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '------------']
        rect_obj = Rectangle(self._layout_array)
        try:
            output = rect_obj.draw_shape(100, 100, 400, 500, self._border_char)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Testing if exception is raised on error input')

    def test_draw_rect4(self):
        rect =  ['------------',
                 '|XXXX......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|XXXX......|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '------------']
        rect_obj = Rectangle(self._layout_array)
        output = rect_obj.draw_shape(4,5,1,1, self._border_char)
        self.assertEqual(rect[1], ''.join(output[1]))
        print('Testing Rectangle dimensions when given is reverse order')

    def test_draw_rect4(self):
        rect =  ['------------',
                 '|XXXX......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|X..X......|',
                 '|XXXX......|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '|..........|',
                 '------------']
        rect_obj = Rectangle(self._layout_array)
        try:
            output = rect_obj.draw_shape(-4, -5, 1, 1, self._border_char)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Testing Rectangle dimensions for negative inputs')

    def test_draw_line1(self):
        rect = ['------------',
               '|XXXX......|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '------------']
        linbe_arr = [list(item) for item in rect]
        line_obj = Line(self._layout_array)
        output = line_obj.draw_shape(1,1,4,1, self._border_char)
        self.assertEqual(len(linbe_arr), len(output))
        print('Testing if line is aded in layout')

    def test_draw_line2(self):
        line = ['------------',
               '|XXXX......|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '------------']
        line_arr = [list(item) for item in line]
        line_obj = Line(self._layout_array)
        output = line_obj.draw_shape(1,1,4,1, self._border_char)
        self.assertEqual(line[1], ''.join(output[1]))
        print('Testing Rectangle dimensions')

    def test_draw_line3(self):
        rect = ['------------',
               '|XXXX......|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '|..........|',
               '------------']
        rect_array = [list(item) for item in rect]
        rect_obj = Line(self._layout_array)
        try:
            output = rect_obj.draw_shape(1000,10000,4,1, self._border_char)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Testing if exception is raised on error input')

    def test_draw_layout1(self):
        layout_obj = Layout(10,10,100,100)
        output = layout_obj.draw_shape()
        self.assertEqual(12, len(output))
        print('Testing if Layout is drawn as per input')

    def test_draw_layout2(self):
        layout_obj = Layout(10, 10, 100, 100)
        output = layout_obj.draw_shape()
        self.assertEqual('-', output[0][0])
        print('Testing if Borders are set correctly in Layout')

    def test_draw_layout3(self):
        layout_obj = Layout(1000, 1000, 100, 100)
        try:
            output = layout_obj.draw_shape()
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Testing if exception is raised on error input for Layout')

    def test_draw_fill_color1(self):
        layout_arr = [list(item) for item in self._layout]
        fill_color_obj = FillColor(layout_arr)
        output = fill_color_obj.draw_shape(1,1,'c')
        self.assertEqual(12, len(output))
        print('Testing if Color is filled as per input')

    def test_draw_fill_color2(self):
        layout_arr = Layout(10,10,100,100).draw_shape()
        fill_color_obj = FillColor(layout_arr)
        output = fill_color_obj.draw_shape(3, 3, 'c')
        self.assertEqual('c', output[1][1])
        print('Testing if Color is filled as per input')

    def test_draw_fill_color3(self):
        layout_arr = Layout(10, 10, 100, 100).draw_shape()
        fill_color_obj = FillColor(layout_arr)
        try:
            output = fill_color_obj.draw_shape(100, 100, 'c')
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Testing if exception is raised on error input for Fill Color')

