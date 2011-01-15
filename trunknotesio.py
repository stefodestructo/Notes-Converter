#!/usr/bino/env python
# convertnotes.py

import datetime 
from string import join

from tnotes.headers import titleheader
from tnotes.headers import timesaccessedheader 
from tnotes.headers import tagsheader
from tnotes.headers import metadataheader
from tnotes.headers import timestampheader
from tnotes.headers import lastaccessedheader 

class TrunkNotesParser:

    def __init__(self):
        
        self.title_header = titleheader.TitleHeader()
        self.times_accessed_header = timesaccessedheader.TimesAccessedHeader()
        self.tags_header = tagsheader.TagsHeader()
        self.metadata_header = metadataheader.MetadataHeader()
        self.timestamp_header = timestampheader.TimestampHeader()
        self.last_accessed_header = lastaccessedheader.LastAccessedHeader()

        self.body = ''
    
    time_format = "%Y-%m-%d %H:%M:%S"

    def get_title(self, input_string):
        try:
            prefix, value = input_string.split(': ', 1)

            if prefix == 'Title':
                return value

            else:
                raise ParseError(UNPARSABLE_TITLE_DATA)

        except ValueError:
            raise ParseError(UNPARSABLE_TITLE_DATA)



    def get_time_stamp(self, input_string):
        try:
            prefix, value = input_string.split(': ', 1)

            #HACK - strptime tzdela functionality seems to be broken
            if value[-5] == '+' or '-':
                #delta = value[-5:-1]
                value = value[0:-6]

            if prefix == 'Timestamp':
                return datetime.datetime.strptime(value, self.time_format) 

            else:
                raise ParseError(UNPARSABLE_TIMESTAMP_DATA)

        except ValueError:
            raise ParseError(UNPARSABLE_TIMESTAMP_DATA)


    def get_last_accessed(self, input_string):
        try:
            prefix, value = input_string.split(': ', 1)

            #HACK - strptime tzdela functionality seems to be broken
            if value[-5] == '+' or '-':
                #delta = value[-5:-1]
                value = value[0:-6]

            if prefix == 'Last Accessed':
                return datetime.datetime.strptime(value, self.time_format) 

            else:
                raise ParseError(UNPARSABLE_LAST_ACCESSED_DATA)

        except:
            raise ParseError(UNPARSABLE_LAST_ACCESSED_DATA)

    
    def get_times_accessed(self, input_string):
        try:
            prefix, value = input_string.split(': ', 1)

            if prefix == 'Times Accessed':
                return int(value)

            else:
                raise ParseError(UNPARSABLE_TIMES_ACCESSED_DATA)

        except (ValueError):
            raise ParseError(UNPARSABLE_TIMES_ACCESSED_DATA)


    def get_tags(self, input_string):
        try:
            prefix, value = input_string.split(':', 1)

            if prefix == 'Tags':
                tags = value.lstrip().split(', ')
                if tags == ['']:
                    return None
                else:
                    return tags

            else:
                raise ParseError(UNPARSABLE_TAGS_DATA)

        except ValueError:
            raise ParseError(UNPARSABLE_TAGS_DATA)

    def get_metadata(self, input_string):
        try:
            prefix, value = input_string.split(':', 1)

            if prefix == 'Metadata':
                tags = value.lstrip().split(',')
                if tags == ['']:
                    return None
                else:
                    return tags

            else:
                raise ParseError(UNPARSABLE_METADATA_DATA)

        except ValueError:
            raise ParseError(UNPARSABLE_METADATA_DATA)


    def parse_content(self, input_data):
        errors = list() 
        metadata = input_data.splitlines()[0:6]
        content = input_data.splitlines()[6:]

        self.title_header.read(metadata[0])
        self.timestamp_header.read(metadata[1])
        self.last_accessed_header.read(metadata[2])
        self.times_accessed_header.read(metadata[3])
        self.tags_header.read(metadata[4])
        self.metadata_header.read(metadata[5])

        # HACK it appears that the method I use the to form the body cuts out 
        # the last new line
        self.body = join(content, '\n') + '\n'

        if len(errors) != 0:
            raise ParseErrors(errors)

    def parse_file(self, file_path):
        try:
            note_file = open(file_path)
            input_data = note_file.read()
            note_file.close()
        except IOError as errno: 
            # No such directory Error
            if errno.args[0] == 2:
                raise ParseError
            # is a directory ERROR
            if errno.args[0] == 21:
                raise ParseError
        else:
            return self.parse_content(input_data) 

    def dump_note(self, note_path):
        # convert the input_data dict to a string
        # prolly should be it's own method

        headers = self.title_header.write() + '\n' 
        headers += self.timestamp_header.write() + '\n'
        headers += self.last_accessed_header.write() + '\n'
        headers += self.times_accessed_header.write() + '\n'
        headers += self.tags_header.write() + '\n'
        headers += self.metadata_header.write() +'\n'

        output_data = headers + self.body 

        # create the file
        with open(note_path.__str__(), 'w') as note_file:
            # write to the file
            note_file.write(output_data)

class ParseError(Exception):
    def __init__(self, value = None):
        self.value = value

    def __str__(self):
        return repr(self.args)


class ParseErrors(Exception):
    def __init__(self, value = None):
        self.value = value

    def __str__(self):
        return repr(self.args)
    def __init__(self, value = None):
        self.value = value

    def __str__(self):
        return repr(self.args)

UNPARSABLE_TITLE_DATA = (1, 'Unable to parse the title data')
UNPARSABLE_TIMESTAMP_DATA = (2, 'Unable to parse the timestamp data')
UNPARSABLE_LAST_ACCESSED_DATA = (3, 'Unable to parse the last accessed data')
UNPARSABLE_TIMES_ACCESSED_DATA = (4, 'Unable to parse the times accessed data')
UNPARSABLE_TAGS_DATA = (5, 'Unable to parse the tags data')
UNPARSABLE_METADATA_DATA = (6, 'Unable to parse the metadata data')
UNPARSABLE_CONTENT_DATA = (7, 'Unable to parse the content data')

