# body.py


class Body:
    """
    Insert docstring here
    """
    def __init__(self):
        """
        Insert docstring here
        """
        self._elements = []

    def append(self, element):
        """
        Insert docstring here
        """
        self._elements.append(element)

    def write(self):
       """
       Insert docstring here
       """
       output_string = ''

       # Add a newline character to all but the last element
       for element in  self._elements[:-1]:
           output_string += element.write() + '\n'
       output_string += self._elements[-1].write()

       return output_string
