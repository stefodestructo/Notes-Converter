#!/usr/bin/env python
# test_trunknotes_data_parse.py

#example data
#title: homepage                                                    DONE
#timestamp: 2010-11-16 14:14:48 -0500                               Done
#last accessed: 2010-11-16 14:15:05 -0500                           Done
#times accessed: 17                                                 Done
#tags: git, ffgga, fcc ff                                           Done
#metadata: gpslongitude=-85.617570,gpslatitude=42.280990      Done 

import unittest
from datetime import datetime

import trunknotesio

from test_trunknotes_test_cases import TestTrunkNotesParser

class TestTrunkNotesParserTitle(TestTrunkNotesParser):
    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_title
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_TITLE_DATA

    def test_title_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_title()""" 

        input_line = 'Title: HomePage'
        expected_value = 'HomePage'
        self.assertEqual(self.target_method(input_line), expected_value)

    def test_title_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = 'HomePage'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)
                
    def test_title_exception_missing_title_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Title\"?"""

        input_line = 'Blah: HomePage'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

class TestTrunkNotesParserTimestamp(TestTrunkNotesParser):
    """Test trunk_notes_parser.get_timestamp"""
    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_time_stamp
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_TIMESTAMP_DATA

    def test_timestamp_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_timestamp()""" 

        input_line = 'Timestamp: 2010-11-16 14:14:48 -0500'
        expected_value = datetime(2010, 11, 16, 14, 14, 48) 
        self.assertEqual(self.target_method(input_line), expected_value)

    def test_timestamp_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = '2010-11-16 14:14:48 -0500'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

    def test_timestamp_exception_wrong_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Timestamp\"?"""

        input_line = 'Blah: 2010-11-16 14:14:48 -0500'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

class TestTrunkNotesParserLastAccessed(TestTrunkNotesParser):
    """Test trunk_notes_parser.get_last_accessed"""

    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_last_accessed
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_LAST_ACCESSED_DATA

    def test_last_accessed_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_last_accessed()""" 

        input_line = 'Last Accessed: 2010-11-16 14:15:05 -0500'
        expected_value = datetime(2010, 11, 16, 14, 15, 05) 

        self.assertEqual(self.target_method(input_line), expected_value)

    def test_last_accessed_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = '2010-11-16 14:15:05 -0500'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)


    def test_last_accessed_exception_wrong_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Last Accessed\"?"""

        input_line = 'Blah: 2010-11-16 14:14:48 -0500'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

    def test_last_accessed_exception_correct_prefix_sans_colon(self):
        """Does the ParseError exception get raised when there's not a colon
        after the prefix?"""

        input_line = 'Last Accessed'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

class TestTrunkNotesParserTimesAccessed(TestTrunkNotesParser):
    """Test trunk_notes_parser.get_times_accessed"""

    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_times_accessed
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_TIMES_ACCESSED_DATA

    def test_times_accessed_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_times_accessed()""" 

        input_line = 'Times Accessed: 17'
        expected_value = 17

        self.assertEqual(self.target_method(input_line), expected_value)

    def test_times_accessed_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = '17'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

    def test_times_accessed_exception_wrong_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Times Accessed\"?"""

        input_line = 'Blah: HomePage'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

class TestTrunkNotesParserTags(TestTrunkNotesParser):
    """Test trunk_notes_parser.get_tags"""

    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_tags
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_TAGS_DATA

    def test_tags_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_tags()""" 

        input_line = 'Tags: Git, Ffgga, FCC Ff'
        expected_value = ['Git', 'Ffgga', 'FCC Ff']

        self.assertEqual(self.target_method(input_line), expected_value)
    
    def test_tags_returns_correct_value_no_tags(self):
        input_line = 'Tags:'
        expected_value = None
        self.assertEqual(self.target_method(input_line), expected_value)

    def test_tags_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = 'blah, blah'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

    
    def test_tags_exception_missing_tags_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Tags\"?"""

        input_line = 'Blah: HomePage'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

class TestTrunkNotesParserMetadata(TestTrunkNotesParser):
    """Test trunk_notes_parser.get_meta_data"""

    def setUp(self):
        TestTrunkNotesParser.setUp(self)
        self.target_method = self.trunk_notes_parser.get_metadata
        self.expected_exception = trunknotesio.ParseError
        self.expected_exception_args = trunknotesio.UNPARSABLE_METADATA_DATA 
        
    def test_metadata_returns_correct_value(self):
        """Test what gets returned by TrunkNotesParser.get_meta_data()""" 
        input_line = 'Metadata: gpslongitude=-85.617570,gpslatitude=42.280990'
        expected_value = ['gpslongitude=-85.617570', 'gpslatitude=42.280990']

        self.assertEqual(self.target_method(input_line), expected_value)

    def test_metadata_returns_correct_value_given_no_metadata(self):
        """Test what gets returned by TrunkNotesParser.get_meta_data()""" 

        input_line = 'Metadata:'
        expected_value = None

        self.assertEqual(self.target_method(input_line), expected_value)

    def test_metadata_exception_missing_prefix(self):
        """Does the ParseError exception get raised when the prefix is missing?""" 

        input_line = 'blah, blah'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)

    def test_meta_data_exception_wrong_prefix(self):
        """Does the ParseError exception get raised when the prefix is not \"Metadata\"?"""

        input_line = 'Blah: HomePage'

        self.assert_raises_plus_plus(self.expected_exception,
                self.expected_exception_args, self.target_method, input_line)
