#test_py_test.py
import py
import os.path
import filecmp
import trunknotesio



class SetupFileCompare:
    def __init__(self, request):
        self.tmpdir = request.getfuncargvalue("tmpdir")

    def setup_fixtures(self):
        #self.trunknotesio = trunknotesio.TrunkNotesParser()
        #return (self.tmpdir.dirpath(), self.trunknotesio)
        return self

    def teardown_fixtures(self, args):
       tmpdir_path,  trunknotesio = args
       #tmpdir.remove(rec=0, ignore_errors=True)

    def run(self):
        pass

    def get_trunknotesio(self):
        return trunknotesio.TrunkNotesParser()

    def get_tmpdir(self):
        return self.tmpdir

def pytest_funcarg__setup_file_compare(request):
    
    file_compare_setup = SetupFileCompare(request)

    return request.cached_setup(
            setup = file_compare_setup.setup_fixtures,
            teardown = file_compare_setup.teardown_fixtures,
            scope = 'function'
            )

def test_setup_file_compare(setup_file_compare):
    """
    Parse a note file, send the parsed data to the save method and compare the
    file that was read to what was saved to a temporary directory.
    """

    # Get Fixtures
    tnotes = setup_file_compare.get_trunknotesio()
    tmpdir = setup_file_compare.get_tmpdir()

    # Define Test Parameters
    input_note_directory = 'tests/data/single_notes/'
    input_note_file_name = 'HomePage'
    input_note_path = os.path.join(input_note_directory, input_note_file_name)

    output_note_directory = tmpdir.dirpath()
    output_note_file_name= input_note_file_name
    #output_note_path = os.path.join(output_note_directory,
    #        output_note_file_name)
    output_note_path = tmpdir.dirpath(input_note_file_name)

    # Run methods under test
    input_data = tnotes.parse_file(input_note_path)
    tnotes.dump_note(input_data, output_note_path)
    
    # Open the input and output files
    #try:
    #    input_file = open(input_file_path)
    #    output_file = open(output_file_path)
    
    # If there's a problem opening up either of the files under test, the test
    # should fail
    #except:
    #   pass 

    ## Read the input and output files    
    #input_file_content = input_file.read() 
    #output_file_content = output_file.read()
    #
    ## Close input and output files
    #input_file.close()
    #output_file.close()

    # Test that the input and output files have the same contents
    assert(filecmp.cmp(input_note_path, output_note_path.__str__()))
