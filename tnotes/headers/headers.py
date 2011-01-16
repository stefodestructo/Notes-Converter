# headers.py

class Headers:
    """
    Insert docstring here
    """
    def __init__(self, title_header, timestamp_header, last_accessed_header,
            times_accessed_header, tags_header, metadata_header):
        """
        Insert docstring here
        """
        self.title_header = title_header
        self.timestamp_header = timestamp_header
        self.last_accessed_header = last_accessed_header
        self.times_accessed_header = times_accessed_header
        self.tags_header = tags_header
        self.metadata_header = metadata_header

    def get_prefixes(self):
        """
        Returns list of the headers' prefixes
        """
        prefixes = []
        prefixes.append(self.title_header.get_prefix())
        prefixes.append(self.timestamp_header.get_prefix())
        prefixes.append(self.last_accessed_header.get_prefix())
        prefixes.append(self.times_accessed_header.get_prefix())
        prefixes.append(self.tags_header.get_prefix())
        prefixes.append(self.metadata_header.get_prefix())
        return prefixes

    def read(self, input_string):
        """
        Insert docstring here
        """
        self.title_header.read(input_string.splitlines(False)[0])
        self.timestamp_header.read(input_string.splitlines(False)[1])
        self.last_accessed_header.read(input_string.splitlines(False)[2])
        self.times_accessed_header.read(input_string.splitlines(False)[3])
        self.tags_header.read(input_string.splitlines(False)[4])
        self.metadata_header.read(input_string.splitlines(False)[5])

