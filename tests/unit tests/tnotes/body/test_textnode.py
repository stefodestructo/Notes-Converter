# test_textelement.py

from tnotes.body.textnode import TextNode


def test_textnode_read():
    """
    Insert docstring here
    """
    string_under_test = 'Hello World'
    expected_value = 'Hello World'

    text_node = TextNode()
    text_node.read(string_under_test) 

    assert(text_node.get_value() == expected_value)
