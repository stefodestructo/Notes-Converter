# test_headerelement.py

from tnotes.body.headerelement import HeaderElement


def test_headerelement_read():
    """
    Insert docstring here
    """
    string_under_test = '#Hello World'
    expected_value = 'Hello World'
    expected_level = 1

    header_element = HeaderElement()
    header_element.read(string_under_test)

    assert(header_element.get_value() == expected_value)
    assert(header_element.get_level() == expected_level)


def test_headerelement_write():
    """
    Insert docstring here
    """
    test_value = 'Hello World'
    test_level = 3

    expected_output = '###Hello World'

    header_element = HeaderElement()

    header_element.set_value(test_value)
    header_element.set_level(test_level)

    assert(header_element.write() == expected_output)


def test_header_element_read_write():
    """
    Insert docstring here
    """
    string_under_test = '###Hello World'

    header_element = HeaderElement()

    header_element.read(string_under_test)

    assert(header_element.write() == string_under_test)
