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
    
    # Create a HeaderElement mock object
    header_element1 = Mock(['write'], name='header_element1')
    header_element1.write.return_value = '#Hello World1'

    header_element2 = Mock(['write'], name='header_element2')
    header_element2.write.return_value = '##Hello World2'

    body.append(header_element1)
    body.append(header_element2)

    assert(body.write() == expected_output)
   
def test_body_write_body_header_text():
    """
    Insert doctstring here
    """
    expected_output = """\
#hello World
This is just a test\
"""

    body = Body()

    # Create a HeaderElement mock object
    header_element = Mock(['write'], name='header_element')
    header_element.write.return_value = '#Hello World'

    # Create a TextElement mock object
    text_element = Mock(['write'], name='text_element')
    text_element.write.return_value = 'This is just a test'

    body.append(header_element)
    body.append(text_element)
