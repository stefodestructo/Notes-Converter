# textelement.py


class TextElement:
    """
    Insert docstring here
    """
    def __init__(self):
        """
        Insert docstring here
        """
        self._value = ''


    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value == value

    def read(self, input_string):
        self._value = input_string
