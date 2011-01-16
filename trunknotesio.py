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
    """
    Insert docstring here
    """

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
        Insert docstring here
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
            # No such directory Error
            if errno.args[0] == 2:
                # will be replace once code is ready for input checkecking
                pass
            ## is a directory ERROR
            if errno.args[0] == 21:
                # will be replace once code is ready for input checkecking
                pass
        else:   
            return self.parse_content(input_data) 

    def dump_note(self, note_path):
        """
        Insert docstring here
        """
        headers = self.title_header.write() 
        headers += self.timestamp_header.write()
        headers += self.last_accessed_header.write() 
        headers += self.times_accessed_header.write()
        headers += self.tags_header.write()
        headers += self.metadata_header.write() 

        output_data = headers + self.body 

        # create the file
        with open(note_path.__str__(), 'w') as note_file:
            # write to the file
            note_file.write(output_data)
