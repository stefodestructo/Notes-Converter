# body.py


class Body:
    """
    Insert docstring here
    """
    def __init__(self):
        """
        Insert docstring here
        """
        self._nodes = []

    def append(self, node):
        """
        Insert docstring here
        """
        self._nodes.append(node)

    def write(self):
       """
       Insert docstring here
       """
       output_string = ''

       # Add a newline character to all but the last element
       for node in  self._nodes[:-1]:
           output_string += node.write() + '\n'
       output_string += self._nodes[-1].write()

       return output_string
