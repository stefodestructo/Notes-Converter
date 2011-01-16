# test_tagsheader.py

import py
from tnotes.headers import tagsheader

# Baseline Tests (no exceptions)
# Tags Tests

def test_tags_header_read_method():

    tags_header_string = 'Tags: epic, lol, foo, bar'
    expected_output = ['epic', 'lol', 'foo', 'bar']
    
    tags_header = tagsheader.TagsHeader()

    tags_header.read(tags_header_string)

    assert(tags_header.get_value() == expected_output)

def test_tags_header_write_method():
    
    tags_header_value = ['epic', 'lol', 'foo', 'bar']
    expected_output = 'Tags: epic, lol, foo, bar'

    tags_header = tagsheader.TagsHeader()
    
    tags_header.set_value(tags_header_value)

    assert(tags_header.write() == expected_output)

def test_tags_header_correct_prefix():

    expected_output = 'Tags'

    tags_header = tagsheader.TagsHeader()

    assert(tags_header.get_prefix() == expected_output)
