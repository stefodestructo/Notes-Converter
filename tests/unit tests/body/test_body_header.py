# test_body_header.py

from tnotes.body.bodyheader import BodyHeader


def test_body_header_read():
    """
    Insert docstring here
    """
    string_under_test = '#Hello World'
    expected_value = 'Hello World'
    expected_level = 1

    body_header = BodyHeader()
    body_header.read(string_under_test)

    assert(body_header.get_value() == expected_value)
    assert(body_header.get_level() == expected_level)


def test_body_header_write():
    """
    Insert docstring here
    """
    test_value = 'Hello World'
    test_level = 3

    expected_output = '###Hello World'

    body_header = BodyHeader()

    body_header.set_value(test_value)
    body_header.set_level(test_level)

    assert(body_header.write() == expected_output)


def test_body_header_read_write():
    """
    Insert docstring here
    """
    string_under_test = '###Hello World'

    body_header = BodyHeader()

    body_header.read(string_under_test)

    assert(body_header.write() == string_under_test)
