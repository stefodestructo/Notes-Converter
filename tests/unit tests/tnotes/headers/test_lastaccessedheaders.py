# test_lastaccessedheaders.py

import py
from tnotes.headers import lastaccessedheader


def test_last_accessed_header_read_method():
    """
    Insert docstring here
    """
    last_accessed_header_string = 'LastAccessed: 2010-12-29 23:43:58 -0500'
    expected_output = '2010-12-29 23:43:58 -0500'

    last_accessed_header = lastaccessedheader.LastAccessedHeader()

    last_accessed_header.read(last_accessed_header_string)

    assert(last_accessed_header.get_value() == expected_output)


def test_last_accessed_header_write_method():
    """
    Insert docstring here
    """
    last_accessed_header_value = '2010-12-29 23:43:58 -0500'
    expected_output = 'Last Accessed: 2010-12-29 23:43:58 -0500\n'

    last_accessed_header = lastaccessedheader.LastAccessedHeader()

    last_accessed_header.set_value(last_accessed_header_value)

    assert(last_accessed_header.write() == expected_output)


def test_last_accessed_header_correct_prefix():
    """
    Insert docstring here
    """
    expected_output = 'Last Accessed'

    last_accessed_header = lastaccessedheader.LastAccessedHeader()

    assert(last_accessed_header.get_prefix() == expected_output)
