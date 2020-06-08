import pytest


from data_parser.data_types.xml import XML


@pytest.fixture
def xml_object():
    return XML('<test>')


def test_create_xml_with_opening_tag():
    xml_object = XML('<name>')
    assert xml_object.value is None
    assert xml_object.tag_name == 'name'
    assert xml_object.ending_tag is None


def test_create_xml_with_ending_tag():
    with pytest.raises(ValueError):
        XML('</name>')


def test_set_value(xml_object):
    xml_object.value = 'testing'
    assert xml_object.value == 'testing'
