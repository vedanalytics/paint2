class RectangleValidations:
    def __init__(self, layout, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._layout = layout
        self._max_height = len(layout)
        self._max_width = len(layout[0]) if self._max_height > 0 else 0
        self.INPUT_RANGE_EXCEED ='Invalid Input for Rectangle' \
                                 '\nx1 and x2 must be between 1 and ' + str(self._max_width) + '' \
                                 '\ny1 and y2 must be between 1 and ' + str(self._max_height)
        self.NO_LAYOUT_FOUND = 'Please draw the layout first'

    def validate_rectangle(self):
        is_layout_drawn = self.__is_layout_drawn(self._layout)
        if not is_layout_drawn:
            raise ValueError(self.NO_LAYOUT_FOUND)
        is_valid = self.__is_input_valid(self._max_width, self._max_height, self._x1, self._y1, self._x2, self._y2)
        if not is_valid:
            raise ValueError(self.INPUT_RANGE_EXCEED)

    def __is_input_valid(self, width, height, x1, y1, x2, y2):
        if x1 < 1 or x1 > width or x2 < 1 or x2 > width:
            return False
        if y1 < 1 or y1 > height or y2 < 1 or y2 > height:
            return False
        return True

    def __is_layout_drawn(self, layout):
        return True if len(layout) > 0 else False



