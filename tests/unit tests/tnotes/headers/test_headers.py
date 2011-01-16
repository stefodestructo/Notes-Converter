# test_headers.py
from tnotes.headers.headers import Headers
from mock import Mock

def test_headers_get_prefixes():
    """
    Insert docstring here
    """
    expected_prefixes = ['Title', 'Timestamp', 'Last Accessed',
            'Times Accessed', 'Tags', 'Metadata']

    # Make mock objects
    title_header = Mock(['get_prefix'], name='title_header')
    title_header.get_prefix.return_value = 'Title'

    timestamp_header = Mock(['get_prefix'], name='timestamp_header')  
    timestamp_header.get_prefix.return_value = 'Timestamp'

    last_accessed_header = Mock(['get_prefix'], name='last_accessed_header')
    last_accessed_header.get_prefix.return_value = 'Last Accessed'


    times_accessed_header = Mock(['get_prefix'], name='times_accessed_header')
    times_accessed_header.get_prefix.return_value = 'Times Accessed'

    tags_header = Mock(['get_prefix'], name='tags_header')
    tags_header.get_prefix.return_value = 'Tags'

    metadata_header = Mock(['get_prefix'], name='metadata_header')
    metadata_header.get_prefix.return_value = 'Metadata'

    headers = Headers(title_header, timestamp_header, last_accessed_header, 
            times_accessed_header, tags_header, metadata_header)

    assert(headers.get_prefixes() == expected_prefixes)

def test_headers_read():
    """
    Insert docstring here
    """
    sample_input_data = """\
Title: HelloWorld
Timestamp: 2010-11-18 18:10:33 -0500
Last Accessed: 2010-11-19 20:02:28 -0500
Times Accessed: 24
Tags:
Metadata:
"""

    # Make mock objects
    title_header = Mock(['read'], name='title_header')
    timestamp_header = Mock(['read'], name='timestamp_header')
    last_accessed_header = Mock(['read'], name='last_accessed_header')
    times_accessed_header = Mock(['read'], name='times_accessed_header')
    tags_header = Mock(['read'], name='tags_header')
    metadata_header = Mock(['read'], name='metadata_header')
    
    # build object under test 
    headers = Headers(title_header, timestamp_header, last_accessed_header, 
            times_accessed_header, tags_header, metadata_header)

    # run method under test
    headers.read(sample_input_data)
    
    # test that the headers' read was called once and
    # that the parameters they received are correct
    title_header.read.assert_called_once_with('Title: HelloWorld')
    timestamp_header.read.assert_called_once_with(
            'Timestamp: 2010-11-18 18:10:33 -0500')
    last_accessed_header.read.assert_called_once_with(
            'Last Accessed: 2010-11-19 20:02:28 -0500')
    times_accessed_header.read.assert_called_once_with('Times Accessed: 24')
    tags_header.read.assert_called_once_with('Tags:')
    metadata_header.read.assert_called_once_with('Metadata:')
