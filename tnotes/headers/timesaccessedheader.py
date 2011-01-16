# timesaccessedheader.py

class TimesAccessedHeader():

    def __init__(self):
        """
        Insert doc string here
        """

        self._prefix = 'Times Accessed'
        self._value = 0


    def get_prefix(self):
        """
        Insert doc string here
        """

        return self._prefix


    def set_value(self, value):
        """
        Insert doc string here
        """

        self._value = int(value)


    def get_value(self):
        """
        Insert doc string here
        """

        return self._value

    def read(self, header_string):
        """
        Insert doc string here
        """

        prefix, value = header_string.split(': ', 1)

        self._value = int(value)

    def write(self):
        header_template = 'Times Accessed: '

        return header_template + str(self._value) + '\n'
