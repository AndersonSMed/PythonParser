import pytest


from data_parser.data_types.xml import XML


def test_create_xml_with_opening_tag():
    xml_object = XML('<name>')
    assert xml_object.inner_value is None
    assert xml_object.tag_name == 'name'
    assert xml_object.attributes == {}


def test_create_xml_with_ending_tag():
    with pytest.raises(ValueError):
        XML('</name>')


def test_create_xml_with_attributes():
    xml_object = XML('<person name="Maria" age=19/>')
    expected_attributes = {
        'name': 'Maria',
        'age': 19
    }
    assert xml_object.attributes == expected_attributes

def test_set_value():
    xml_object = XML('<test>')
    xml_object.inner_value = 'testing'
    assert xml_object.inner_value == 'testing'
