import re


class PaintValidations:
    def __init__(self):
        self.INVALID_INPUT = 'Invalid Input. Input must be in format:' \
                    '\n\"C width height\" \n\"L x1 y1 x2 y2 \"'' \
                    '' \n\"R x1 y1 x2 y2 \" \n\"B x y color(*)\"'

    INPUT_REGEX_VALIDATORS = {
        'C': '^[cC]{1} [0-9]{1,9} [0-9]{1,9}$',
        'L': '^[lL]{1} [0-9]{1,9} [0-9]{1,9} [0-9]{1,9} [0-9]{1,9}$',
        'R': '^[rR]{1} [0-9]{1,9} [0-9]{1,9} [0-9]{1,9} [0-9]{1,9}$',
        'B': '^[bB]{1} [0-9]{1,9} [0-9]{1,9} .{1}$'
    }

    def validate_and_reshape_input(self, cmd):
        c_regex = re.compile(self.INPUT_REGEX_VALIDATORS['C'])
        m_regex = re.compile(self.INPUT_REGEX_VALIDATORS['L'])
        r_regex = re.compile(self.INPUT_REGEX_VALIDATORS['R'])
        b_regex = re.compile(self.INPUT_REGEX_VALIDATORS['B'])
        if len(cmd) > 0 and type(cmd) is str:
            cmd = cmd.strip()
        else:
            raise ValueError(self.INVALID_INPUT)
        if len(c_regex.findall(cmd)) > 0 or len(m_regex.findall(cmd)) > 0 or len(r_regex.findall(cmd)) > 0 or len(
                b_regex.findall(cmd)) > 0:
            return True, self.reshape_input(cmd)
        else:
            raise ValueError(self.INVALID_INPUT)

    def reshape_input(self, input_cmd):
        cmd_array = []
        if len(input_cmd) > 0:
            cmd_array = input_cmd.replace('\"', '').split(" ")
            cmd_array[0] = cmd_array[0].upper()
        return cmd_array
