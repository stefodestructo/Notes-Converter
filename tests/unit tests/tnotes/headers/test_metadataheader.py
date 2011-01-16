# test_metadataheader.py

import py
from tnotes.headers import metadataheader


def test_metadata_header_read_method():
    """
    Insert docstring here
    """
    metadata_header_string = \
            'Metadata: gpslongitude=-85.617570,gpslatitude=42.280990'
    expected_output = ['gpslongitude=-85.617570', 'gpslatitude=42.280990']

    metadata_header = metadataheader.MetadataHeader()

    metadata_header.read(metadata_header_string)

    assert(metadata_header.get_value() == expected_output)


def test_metadata_header_write_method():
    """
    Insert docstring here
    """
    metadata_header_value = ['gpslongitude=-85.617570',\
            'gpslatitude=42.280990']
    expected_output = \
            'Metadata: gpslongitude=-85.617570,gpslatitude=42.280990\n'

    metadata_header = metadataheader.MetadataHeader()

    metadata_header.set_value(metadata_header_value)

    assert(metadata_header.write() == expected_output)


def test_metadata_header_correct_prefix():
    """
    Insert docstring here
    """
    expected_output = 'Metadata'

    metadata_header = metadataheader.MetadataHeader()

    assert(metadata_header.get_prefix() == expected_output)
