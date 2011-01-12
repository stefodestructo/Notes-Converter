# tagsheader.py

class MetadataHeader():

    def __init__(self):
        """
        Insert doc string here
        """

        self._prefix = 'Metadata'
        self._value = []


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

        prefix, raw_tags = header_string.split(': ', 1)

        value = raw_tags.lstrip().split(',')
        #if tags == ['']:
        #    return None
        #else:
        #    return tags

        self._value = value

    def write(self):
        """
        Insert doc string here
        """

        header_template = 'Metadata: '

        raw_tags = ''
        
        for tag in self._value[:-1]:
            raw_tags = raw_tags + tag + ','

        raw_tags = raw_tags + self._value[-1]

        return header_template + raw_tags
