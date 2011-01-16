# test_tagsheader.py

import py
from tnotes.headers import tagsheader


def test_tags_header_read_method():
    """
    Insert docstring here
    """
    tags_header_string = 'Tags: epic, lol, foo, bar'
    expected_output = ['epic', 'lol', 'foo', 'bar']

    tags_header = tagsheader.TagsHeader()

    tags_header.read(tags_header_string)

    assert(tags_header.get_value() == expected_output)


def test_tags_header_write_method():
    """
    Insert docstring here
    """
    tags_header_value = ['epic', 'lol', 'foo', 'bar']
    expected_output = 'Tags: epic, lol, foo, bar\n'

    tags_header = tagsheader.TagsHeader()

    tags_header.set_value(tags_header_value)

    assert(tags_header.write() == expected_output)


def test_tags_header_correct_prefix():
    """
    Insert docstring here
    """
    expected_output = 'Tags'

    tags_header = tagsheader.TagsHeader()

    assert(tags_header.get_prefix() == expected_output)
