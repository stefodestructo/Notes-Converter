# test_body.py

from mock import Mock

from tnotes.body.body import Body


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
    
    # Create a HeaderNode mock object
    header_node1 = Mock(['write'], name='header_node1')
    header_node1.write.return_value = '#Hello World1'

    header_node2 = Mock(['write'], name='header_node2')
    header_node2.write.return_value = '##Hello World2'

    body.append(header_node1)
    body.append(header_node2)

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

    # Create a HeaderNode mock object
    header_node = Mock(['write'], name='header_node')
    header_node.write.return_value = '#Hello World'

    # Create a TextNode mock object
    text_node = Mock(['write'], name='text_node')
    text_node.write.return_value = 'This is just a test'

    body.append(header_node)
    body.append(text_node)
