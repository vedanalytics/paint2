from painter_app.paint_main import PaintMain
import copy


class Painter:
    def __init__(self):
        self._paint_utils = None
        self.input_command = []
        self._layout_matrix = []
        self.MAX_WIDTH = 300
        self.MAX_HEIGHT = 300
        self._paint_utils = PaintMain(self.MAX_WIDTH, self.MAX_HEIGHT)

    print('Welcome to the Painter')

    def execute_command(self, input_cmd):
        try:
            self._layout_matrix = copy.deepcopy(self._paint_utils.draw(input_cmd))
            self._paint_utils.render(self._layout_matrix)
        except ValueError as ex:
            print(str(ex))

if __name__ == "__main__":
    in_command_loop = True
    painter = Painter()
    while in_command_loop:
        cmd = input("Enter Command: ")
        if cmd == 'Q':
            break
        painter.execute_command(cmd)
