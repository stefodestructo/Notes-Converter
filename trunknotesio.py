#!/usr/bino/env python
# convertnotes.py

import datetime 
from string import join

class TrunkNotesParser:
    
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

        output_dict = dict()
        
        try:
            output_dict['title'] = self.get_title(metadata[0])
        except ParseError as exception:
            errors.append(exception.value)
        
        try:
            output_dict['timestamp'] = self.get_time_stamp(metadata[1])
        except ParseError as exception:
            errors.append(exception.value)

        try:
            output_dict['last accessed'] = self.get_last_accessed(metadata[2])
        except ParseError as exception:
            errors.append(exception.value)

        try:
            output_dict['times accessed'] = self.get_times_accessed(metadata[3])
        except ParseError as exception:
            errors.append(exception.value)

        try:
            output_dict['tags'] = self.get_tags(metadata[4])
        except ParseError as exception:
            errors.append(exception.value)

        try:
            output_dict['metadata'] = self.get_metadata(metadata[5])
        except ParseError as exception:
            errors.append(exception.value)

        # HACK it appears that the method I use the to form the body cuts out 
        # the last new line
        output_dict['body'] = join(content, '\n') + '\n'
        if len(errors) != 0:
            raise ParseErrors(errors)
        return output_dict

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

    def dump_note(self, input_data, note_path):
        # convert the input_data dict to a string
        # prolly should be it's own method

	from string import Template

	if input_data['metadata'] == None:
		input_data['metadata'] = '' 
	
	if input_data['tags'] == None:
		input_data['tags'] = ''	
	template_string = """Title: $title
Timestamp: $timestamp
Last Accessed: $lastaccessed
Times Accessed: $timesaccessed
Tags: $tags
Metadata: $metadata
$body"""
	template = Template(template_string)
	output_data = template.substitute(
		title=input_data['title'],
		timestamp=str(input_data['timestamp']) + ' -0500',
		lastaccessed=str(input_data['last accessed']) + ' -0500',
		timesaccessed=input_data['times accessed'],
		tags=input_data['tags'],
		metadata=input_data['metadata'],
		body=input_data['body'],
	)

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

