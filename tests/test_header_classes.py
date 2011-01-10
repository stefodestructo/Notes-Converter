# test_header_classes.py

import py
from tnotes.headers import titleheader, timesaccessedheader 


# Baseline Tests (no exceptions)

# Title Header Tests
def test_title_header_read_method():


    title_header_string = 'Title: Hello World'
    expected_output = 'Hello World'

    title_header = titleheader.TitleHeader()

    title_header.read(title_header_string)

    assert(title_header.get_value() == expected_output)


def test_title_header_write_method():

    
    title_header_value = 'Hello World'
    expected_output = 'Title: Hello World'

    title_header = titleheader.TitleHeader()
    
    title_header.set_value(title_header_value)

    assert(title_header.write() == expected_output)

def test_title_header_correct_prefix():
    

    expected_output = 'Title'

    title_header = titleheader.TitleHeader()

    assert(title_header.get_prefix() == expected_output)

# Times Accessed Tests

def test_times_accessed_header_read_method():


    times_accessed_header_string = 'Times Accessed: 42'
    expected_output = 42

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()

    times_accessed_header.read(times_accessed_header_string)

    assert(times_accessed_header.get_value() == expected_output)


def test_times_accessed_header_write_method():

    
    times_accessed_header_value = 42
    expected_output = 'Times Accessed: 42'

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()
    
    times_accessed_header.set_value(times_accessed_header_value)

    assert(times_accessed_header.write() == expected_output)

def test_times_accessed_header_correct_prefix():
    

    expected_output = 'Times Accessed'

    times_accessed_header = timesaccessedheader.TimesAccessedHeader()

    assert(times_accessed_header.get_prefix() == expected_output)
