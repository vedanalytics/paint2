class LineValidations:
    def __init__(self, layout, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._layout = layout
        self._max_height = len(layout)-2
        self._max_width = len(layout[0])-2 if self._max_height > 0 else 0
        self.INPUT_RANGE_EXCEED ='Invalid Input for Line' \
                                 '\nx1 and x2 must be between 1 and ' + str(self._max_width) + '' \
                                 '\ny1 and y2 must be between 1 and ' + str(self._max_height) + '' \
                                '\nDistance between (x1,x2) must be same as (y1,y2)'
        self.NO_LAYOUT_FOUND = 'Please draw the layout first'

    def validate_line(self):
        is_layout_drawn = self.__is_layout_drawn(self._layout)
        if not is_layout_drawn:
            raise ValueError(self.NO_LAYOUT_FOUND)
        is_not_valid = not self.__is_input_valid(self._max_width, self._max_height, self._x1, self._y1, self._x2, self._y2)
        is_line_input_not_valid = not self.__is_line_input_valid(self._layout, self._x1, self._y1, self._x2, self._y2)
        if is_not_valid or is_line_input_not_valid:
            raise ValueError(self.INPUT_RANGE_EXCEED)

    def __is_input_valid(self, width, height, x1, y1, x2, y2):
        if x1 < 1 or x1 > width or x2 < 1 or x2 > width:
            return False
        if y1 < 1 or y1 > height or y2 < 1 or y2 > height:
            return False
        return True

    def __is_line_input_valid(self, layout, x1, y1, x2, y2):
        is_valid = True if x1 == x2 or y1 == y2 else abs(x1 - x2) == abs(y1 - y2)
        return is_valid

    def __is_layout_drawn(self, layout):
        return True if len(layout) > 0 else False
