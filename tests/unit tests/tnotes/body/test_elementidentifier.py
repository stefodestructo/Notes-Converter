# test_elementidentifier.py

from tnotes.body.elementidentifier import ElementIdentifier
from tnotes.body.headerelement import HeaderElement
from tnotes.body.textelement import TextElement


def test_elementidentifier_header():
    """
    Insert docstring here
    """
    string_under_test = '#Hello World'
    element_identifier = ElementIdentifier(HeaderElement, TextElement)

    assert(element_identifier.identify(string_under_test) == HeaderElement.__name__)

