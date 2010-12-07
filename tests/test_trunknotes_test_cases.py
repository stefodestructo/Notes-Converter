# test_trunknotes_test_cases.py

import unittest

import trunknotesio

class TestTrunkNotesParser(unittest.TestCase):

    def setUp(self):
        self.trunk_notes_parser = trunknotesio.TrunkNotesParser()


    def assert_raises_plus_plus(self, exception, exception_value, function,
            parameter):

        
        try: 
            function(parameter)
            self.fail('No exceptions where raised')

        except exception, raised_exception:
            self.assertEquals(exception_value, raised_exception.value)
        
        except Exception:
            self.fail('Raised wrong exception!')
