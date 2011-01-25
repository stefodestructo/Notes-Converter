# elementidentifier.py

class ElementIdentifier:
    """
    insert docstring here
    """

    def __init__(self, header_element, text_element):
        """
        insert docstring here
        """
        self.HeaderElement = header_element
        self.TextElement = text_element

    def identify(self, element_string):
        """
        Insert docstring here
        """
        if element_string.startswith('#'):
            return self.HeaderElement.__name__
