# test_nodeidentifier.py

from tnotes.body.nodeidentifier import NodeIdentifier
from tnotes.body.headernode import HeaderNode
from tnotes.body.textnode import TextNode


def test_nodeidentifier_header():
    """
    Insert docstring here
    """
    string_under_test = '#Hello World'
    node_identifier = NodeIdentifier(HeaderNode, TextNode)

    assert(node_identifier.identify(string_under_test) == HeaderNode.__name__)

