# test_headernode.py

from tnotes.body.headernode import HeaderNode


def test_headernode_read():
    """
    Insert docstring here
    """
    string_under_test = '#Hello World'
    expected_value = 'Hello World'
    expected_level = 1

    header_node = HeaderNode()
    header_node.read(string_under_test)

    assert(header_node.get_value() == expected_value)
    assert(header_node.get_level() == expected_level)


def test_headernode_write():
    """
    Insert docstring here
    """
    test_value = 'Hello World'
    test_level = 3

    expected_output = '###Hello World'

    header_node = HeaderNode()

    header_node.set_value(test_value)
    header_node.set_level(test_level)

    assert(header_node.write() == expected_output)


def test_header_node_read_write():
    """
    Insert docstring here
    """
    string_under_test = '###Hello World'

    header_node = HeaderNode()

    header_node.read(string_under_test)

    assert(header_node.write() == string_under_test)
