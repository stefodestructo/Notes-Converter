# test_timesaccessedheader.py

import py
from tnotes.headers import timesaccessedheader


def test_times_accessed_header_read_method():
    """
    Insert docstring here
    """
    times_accessed_header_string = 'Times Accessed: 42'
    expected_output = 42

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()

    times_accessed_header.read(times_accessed_header_string)

    assert(times_accessed_header.get_value() == expected_output)


def test_times_accessed_header_write_method():
    """
    Insert docstring here
    """
    times_accessed_header_value = 42
    expected_output = 'Times Accessed: 42\n'

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()

    times_accessed_header.set_value(times_accessed_header_value)

    assert(times_accessed_header.write() == expected_output)


def test_times_accessed_header_correct_prefix():
    """
    Insert docstring here
    """
    expected_output = 'Times Accessed'

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()

    assert(times_accessed_header.get_prefix() == expected_output)
