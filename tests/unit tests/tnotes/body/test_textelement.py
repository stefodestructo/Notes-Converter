# test_textelement.py

from tnotes.body.textelement import TextElement


def test_textelement_read():
    """
    Insert docstring here
    """
    string_under_test = 'Hello World'
    expected_value = 'Hello World'

    text_element = TextElement()
    text_element.read(string_under_test) 

    assert(text_element.get_value() == expected_value)
