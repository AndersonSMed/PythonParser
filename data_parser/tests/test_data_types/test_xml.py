from data_parser.data_types.xml import XML


def test_create_empty_xml():
    xml_object = XML('<name>')

    assert xml_object.value is None
    assert xml_object.tag_name == 'name'
    assert not xml_object.ending_tag
