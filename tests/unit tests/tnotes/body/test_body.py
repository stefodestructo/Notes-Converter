# test_body.py

from mock import Mock

from tnotes.body.body import Body
#from tnotes.body.bodyheader import BodyHeader


def test_body_write_body_header():
    """
    Insert docstring here
    """
    expected_output = '#Hello World'
    body = Body()
    
    # Create mock BodyHeader object
    body_header = Mock(['write'], name='body_header')
    body_header.write.return_value = '#Hello World'

    body.append(body_header)

    assert(body.write() == expected_output)
   

def test_body_write_body_header():
    """
    Insert docstring here
    """
    expected_output = """\
#Hello World1
##Hello World2\
"""
    body = Body()
    
    # Create mock BodyHeader object
    body_header1 = Mock(['write'], name='body_header1')
    body_header1.write.return_value = '#Hello World1'

    body_header2 = Mock(['write'], name='body_header2')
    body_header2.write.return_value = '##Hello World2'

    body.append(body_header1)
    body.append(body_header2)

    assert(body.write() == expected_output)
   
