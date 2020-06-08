import pytest


from data_parser.data_types.xml import XML
from data_parser.exceptions import InvalidXMLError


def test_create_xml_with_opening_tag():
    xml_object = XML('<name>')
    assert xml_object.inner_value == ''
    assert xml_object.tag_name == 'name'
    assert xml_object.attributes == {}


def test_create_xml_with_ending_tag():
    with pytest.raises(InvalidXMLError):
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


def test_to_dict_value():
    xml_object = XML('<person name="Maria" age=19/>')
    expected_value = {
        'inner_value': '',
        'name': 'Maria',
        'age': 19
    }
    assert xml_object.to_dict() == expected_value

    xml_object._inner_value = 'It should not break'
    expected_value = {
        'inner_value': 'It should not break',
        'name': 'Maria',
        'age': 19
    }
    assert xml_object.to_dict() == expected_value
