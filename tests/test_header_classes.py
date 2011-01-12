# test_header_classes.py

import py
from tnotes.headers import titleheader, timesaccessedheader, tagsheader, metadataheader


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


# Metadata Tests

def test_metadata_header_read_method():


    metadata_header_string = 'Metadata: gpslongitude=-85.617570,gpslatitude=42.280990'
    expected_output = ['gpslongitude=-85.617570', 'gpslatitude=42.280990']
    
    metadata_header = metadataheader.MetadataHeader()

    metadata_header.read(metadata_header_string)

    assert(metadata_header.get_value() == expected_output)


def test_metadata_header_write_method():

    
    metadata_header_value = ['gpslongitude=-85.617570', 'gpslatitude=42.280990']
    expected_output = 'Metadata: gpslongitude=-85.617570,gpslatitude=42.280990'

    metadata_header = metadataheader.MetadataHeader()
    
    metadata_header.set_value(metadata_header_value)

    assert(metadata_header.write() == expected_output)

def test_metadata_header_correct_prefix():
    

    expected_output = 'Metadata'

    metadata_header = metadataheader.MetadataHeader()

    assert(metadata_header.get_prefix() == expected_output)
