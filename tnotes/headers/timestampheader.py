# timestampheader.py

class TimestampHeader():

    def __init__(self):
        """
        Insert doc string here
        """

        self._prefix = 'Timestamp'
        self._value = ''


    def get_prefix(self):
        """
        Insert doc string here
        """

        return self._prefix


    def set_value(self, value):
        """
        Insert doc string here
        """

        self._value = value


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
        self._value = value


    def write(self):
        header_template = 'Timestamp: '

        return header_template + self._value
