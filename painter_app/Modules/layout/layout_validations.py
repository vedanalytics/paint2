class LayoutValidations:
    def __init__(self, max_width, max_height):
        self._max_width = max_width
        self._max_height = max_height
        self.INPUT_RANGE_EXCEED = 'Input Range Exceed the allowed Limits ' \
                             '\nWidth Must be between 1 and ' + str(self._max_width) + '' \
                             '\nHeight Must be between 1 and ' + str(self._max_height)

    def validate_layout(self, width, height):
        if width not in range(1, self._max_width) and height not in range(1, self._max_height):
            raise ValueError(self.INPUT_RANGE_EXCEED)


