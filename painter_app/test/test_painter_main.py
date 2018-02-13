import unittest
from painter_app.paint_main import PaintMain


class TestPainterMain(unittest.TestCase):
    def test_layout_valid_input(self):
        _paint_utils = PaintMain()
        _layout = _paint_utils.draw_layout(10,10)
        self.assertEqual(12, len(_layout))
        print('Test Layout with Valid inputs')

    def test_layout_invalid_input(self):
        _paint_utils = PaintMain()
        try:
            _layout = _paint_utils.draw_layout(1000, 1000)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Layout wifht invalid inputs')

    def test_layout_nagative_input(self):
        _paint_utils = PaintMain()
        try:
            _layout = _paint_utils.draw_layout(-100, -100)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Layout with negative inputs')

    def test_rect_valid_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20,20)

        _layout = _paint_utils.draw_rectangle(10,10,15,15)
        self.assertEqual(22, len(_layout))
        print('Test Rectangle with Valid inputs')

    def test_rect_invalid_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        try:
            _layout = _paint_utils.draw_rectangle(100, 100, 15, 15)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Rectangle with invalid inputs')

    def test_rect_nagative_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        try:
            _layout = _paint_utils.draw_rectangle(-100, -100, 15, 15)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Rectangle with negative inputs')

    def test_line_valid_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20,20)

        _layout = _paint_utils.draw_line(10,10,15,15)
        self.assertEqual(22, len(_layout))
        print('Test Line with Valid inputs')

    def test_line_invalid_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        try:
            _layout = _paint_utils.draw_line(100, 100, 15, 15)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Line wifht invalid inputs')

    def test_line_nagative_input(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        try:
            _layout = _paint_utils.draw_line(-100, -100, 15, 15)
        except ValueError as ex:
            self.assertIsInstance(ex, ValueError)
        print('Test Line with negative inputs')

    def test_draw_layout(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw('C 30 30')
        self.assertEqual(32, len(_paint_utils._layout_matrix))
        print('Testing in input command for Layout rendering proerly')

    def test_draw_layout_wrong_input(self):
        _paint_utils = PaintMain()
        try:
            _paint_utils._layout_matrix = _paint_utils.draw('C 30r 30c')
        except ValueError as ex:
            self.assertIsInstance(ex,ValueError)
        print('Testing in input command for Layout with invalid input')

    def test_draw_rect(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        _paint_utils._layout_matrix = _paint_utils.draw('R 1 1 20 20')
        self.assertEqual('X', _paint_utils._layout_matrix[20][20])
        print('Testing in input command for Rectangle rendering proerly')

    def test_draw_rect(self):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        _paint_utils._layout_matrix = _paint_utils.draw('R 20 20 1 1')
        self.assertEqual('X', _paint_utils._layout_matrix[20][20])
        print('Testing in input command for Rectangle rendering proerly')

    def test_draw_rect_wrong_input(self):
        _paint_utils = PaintMain()
        try:
            _paint_utils._layout_matrix = _paint_utils.draw('R 30r 30c')
        except ValueError as ex:
            self.assertIsInstance(ex,ValueError)
        print('Testing in input command for Rect with invalid input')

    def test_draw_rect_wrong_input2(self):
        _paint_utils = PaintMain()
        try:
            _paint_utils._layout_matrix = _paint_utils.draw(345345)
        except ValueError as ex:
            self.assertIsInstance(ex,ValueError)
        print('Testing in input command for Rect with invalid input')

    def test_draw_line(self,i=1):
        _paint_utils = PaintMain()
        _paint_utils._layout_matrix = _paint_utils.draw_layout(20, 20)
        _paint_utils._layout_matrix = _paint_utils.draw('L 1 1 20 20')
        self.assertEqual('X', _paint_utils._layout_matrix[i][i])
        print('Testing in input command for Line rendering proerly')

    def test_draw_line_wrong_input(self):
        _paint_utils = PaintMain()
        try:
            _paint_utils._layout_matrix = _paint_utils.draw('L 30r 30c')
        except ValueError as ex:
            self.assertIsInstance(ex,ValueError)
        print('Testing in input command for Line with invalid input')

if __name__ == '__main__':
    unittest.main()
