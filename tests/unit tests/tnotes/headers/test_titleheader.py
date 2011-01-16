# test_titleheader.py

import py
from tnotes.headers import titleheader

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
