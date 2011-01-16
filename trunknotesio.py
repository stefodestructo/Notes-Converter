#!/usr/bino/env python
# trunknotesio.py

from string import join

from tnotes.headers.headers import Headers
from tnotes.headers.titleheader import TitleHeader
from tnotes.headers.timesaccessedheader import TimesAccessedHeader
from tnotes.headers.tagsheader import TagsHeader
from tnotes.headers.metadataheader import MetadataHeader
from tnotes.headers.timestampheader import TimestampHeader
from tnotes.headers.lastaccessedheader import LastAccessedHeader


class TrunkNotesParser:
    """
    Insert docstring here
    """

    def __init__(self):
        """
        Insert docstring here
        """
        self.headers = Headers(TitleHeader(), TimestampHeader(),
                LastAccessedHeader(), TimesAccessedHeader(), TagsHeader(),
                MetadataHeader())
        self.body = ''

    def parse_content(self, input_data):
        """
        Insert docstring here
        """
        metadata = join(input_data.splitlines()[0:6], '\n')
        self.body = join(input_data.splitlines(True)[6:], '')

        self.headers.read(metadata)

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
        output_data = self.headers.write() + self.body

        # create the file
        with open(note_path.__str__(), 'w') as note_file:
            # write to the file
            note_file.write(output_data)
