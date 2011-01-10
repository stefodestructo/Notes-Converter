# timesaccessedheader.py
class TimesAccessedHeader():

    def __init__(self):
        self._prefix = 'Times Accessed'
        self._value = ''


    def get_prefix(self):
        return self._prefix


    def set_value(self, value):
        self._value = int(value)


    def get_value(self):
        return self._value

    def read(self, header_string):
        """
        Insert doc string here
        """

        prefix, value = header_string.split(': ', 1)

        self._value = int(value)
        # original method
        #
        #try:
        #    prefix, value = input_string.split(': ', 1)

        #    if prefix == 'Title':
        #        return value

        #    else:
        #        raise ParseError(UNPARSABLE_TITLE_DATA)

        #except ValueError:
        #    raise ParseError(UNPARSABLE_TITLE_DATA)

    def write(self):
        header_template = 'Times Accessed: '

        return header_template + str(self._value)
