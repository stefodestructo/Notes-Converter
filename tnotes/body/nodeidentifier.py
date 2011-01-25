# nodeidentifier.py

class NodeIdentifier:
    """
    insert docstring here
    """

    def __init__(self, header_node, text_node):
        """
        insert docstring here
        """
        self.HeaderNode = header_node
        self.TextNode = text_node

    def identify(self, element_string):
        """
        Insert docstring here
        """
        if element_string.startswith('#'):
            return self.HeaderNode.__name__
