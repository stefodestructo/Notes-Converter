# test_timestampheader.py

import py
from tnotes.headers import timestampheader

# Baseline Tests (no exceptions)
# Timestamp Header Tests
def test_timestamp_header_read_method():


    timestamp_header_string = 'Timestamp: 2010-12-29 23:43:58 -0500'
    expected_output = '2010-12-29 23:43:58 -0500'

    timestamp_header = timestampheader.TimestampHeader()

    timestamp_header.read(timestamp_header_string)

    assert(timestamp_header.get_value() == expected_output)

def test_timestamp_header_write_method():
    
    timestamp_header_value = '2010-12-29 23:43:58 -0500'
    expected_output = 'Timestamp: 2010-12-29 23:43:58 -0500\n'

    timestamp_header = timestampheader.TimestampHeader()
    
    timestamp_header.set_value(timestamp_header_value)

    assert(timestamp_header.write() == expected_output)

def test_timestamp_header_correct_prefix():

    expected_output = 'Timestamp'

    timestamp_header = timestampheader.TimestampHeader()

    assert(timestamp_header.get_prefix() == expected_output)

