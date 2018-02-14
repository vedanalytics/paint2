class FillColorValidations:
    def __init__(self, layout, x, y):
        self._x = x
        self._y = y
        self._layout = layout
        self._max_height = len(layout)-2
        self._max_width = len(layout[0])-2 if self._max_height > 0 else 0
        self.INPUT_RANGE_EXCEED ='Invalid Input for Fill Color' \
                                 '\nx must be between 1 and ' + str(self._max_width) + '' \
                                 '\ny must be between 1 and ' + str(self._max_height)
        self.NO_LAYOUT_FOUND = 'Please draw the layout first'

    def validate_fill_color(self):
        is_layout_drawn = self.__is_layout_drawn(self._layout)
        if not is_layout_drawn:
            raise ValueError(self.NO_LAYOUT_FOUND)
        is_valid = self.__is_input_valid(self._max_width, self._max_height, self._x, self._y)
        if not is_valid:
            raise ValueError(self.INPUT_RANGE_EXCEED)

    def __is_input_valid(self, width, height, x, y):
        return True if 1 <= x <= width and 1 <= y <= height else False

    def __is_layout_drawn(self, layout):
        return True if len(layout) > 0 else False
