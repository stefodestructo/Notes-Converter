#!/usr/bino/env python
# trunknotesio.py

from string import join

from tnotes.headers import titleheader
from tnotes.headers import timesaccessedheader 
from tnotes.headers import tagsheader
from tnotes.headers import metadataheader
from tnotes.headers import timestampheader
from tnotes.headers import lastaccessedheader 

class TrunkNotesParser:

    def __init__(self):
        """
        Insert docstring here
        """

        self.title_header = titleheader.TitleHeader()
        self.times_accessed_header = timesaccessedheader.TimesAccessedHeader()
        self.tags_header = tagsheader.TagsHeader()
        self.metadata_header = metadataheader.MetadataHeader()
        self.timestamp_header = timestampheader.TimestampHeader()
        self.last_accessed_header = lastaccessedheader.LastAccessedHeader()

        self.body = ''
    
    def parse_content(self, input_data):
        """
        Insert Docstring here
        """
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


    def parse_file(self, file_path):
        """
        Insert docstring here
        """
        try:
            note_file = open(file_path)
            input_data = note_file.read()
            note_file.close()
        except IOError as errno: 
            pass
            # No such directory Error
            #if errno.args[0] == 2:
            #    raise ParseError
            ## is a directory ERROR
            #if errno.args[0] == 21:
            #    raise ParseError
        else:
            return self.parse_content(input_data) 


    def dump_note(self, note_path):
        """
        Insert doctsring here
        """

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

