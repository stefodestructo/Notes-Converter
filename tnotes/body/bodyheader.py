#bodyheader.py


class BodyHeader:
    """
    Insert docstring here
    """

    def __init__(self):
        """
        Insert docstring here
        """
        self._value = ''
        self._level = 0

    def read(self, input_string):
        """
        Insert docstring here
        """
        # remove whitespace at the beginning of the input_string
        input_string = input_string.lstrip()

        # Seperate #s at the beginning of the string from the
        # rest of input_string
        self._value = input_string.lstrip('#')

        # count #s that where seperated
        self._level = len(input_string) - len(self._value)

    def set_value(self, value):
        """
        Insert docstring here
        """
        self._value = value

    def get_value(self):
        """
        Insert docstring here
        """
        return self._value

    def set_level(self, level):
        """
        Insert docstring here
        """
        self._level = level

    def get_level(self):
        """
        Insert docstring here
        """
        return self._level

    def write(self):
        """
        Insert docstring here
        """
        prefix = '#' * self._level
        return prefix + self._value
