# test_trunknotes_files.py

from nose import tools
from glob import iglob
import imp
from os import path
from hashlib import md5

import trunknotesio

def setup():
    pass

def teardown():
    pass

def get_module(module_path):
    #ripped from http://code.davidjanes.com/blog/2008/11/27/how-to-dynamically-load-python-code/

    module_dir = path.dirname(module_path)
    module_filename = path.basename(module_path)
    
    module_file = open(module_path, 'rb')

    module = imp.load_source(md5(module_path).hexdigest(), module_path,
            module_file)

    module_file.close()
    return module

def _get_dict(path, dict_name):
    module = get_module(path)
    return getattr(module, dict_name)

def _file(target_path, target_dict):
    trunk_notes_parser = trunknotesio.TrunkNotesParser()
    tools.assert_equal(trunk_notes_parser.parse_file(target_path),
            target_dict)

def test_files():
    dict_name = 'expected_data'

    files = [f for f in iglob('tests/data/single_notes/*') if not path.isdir(f)]

    target_note_files = [f for f in files if not f.endswith('.py')]
    target_py_files = [f for f in files if f.endswith('.py')] 

    target_pairs = [(f, _get_dict(f + '.py', dict_name)) for f in target_note_files if f + '.py' in
            target_py_files]

    for (target_path, target_dict) in target_pairs:
        print "foo"
        yield _file, target_path, target_dict

@tools.raises(trunknotesio.ParseError)
def test_nonexisting_file_exception():


    target_path = 'tests/data/single_notes/no_one_home'

    trunk_notes_parser = trunknotesio.TrunkNotesParser()
    trunk_notes_parser.parse_file(target_path)
    

@tools.raises(trunknotesio.ParseError)
def test_file_is_directory_exception():
    target_path = 'tests/data/single_notes/'

    trunk_notes_parser = trunknotesio.TrunkNotesParser()
    trunk_notes_parser.parse_file(target_path)
