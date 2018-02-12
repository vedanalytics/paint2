import unittest
from Modules.layout.layout import Layout
from Modules.line.line import Line
from Modules.fill_color.fill_color import FillColor
from Modules.rectangle.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
