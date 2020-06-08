from data_parser.tests import utils
from data_parser.parsers.xml_parser import XMLParser


class TestXmlParser:
    def _get_xml_object(self, file_path):
        file = utils.read_file(file_path)
        return XMLParser(file)

    def test_process_data(self):
        file_path = 'data_parser/tests/fixtures/names.xml'
        xml_object = self._get_xml_object(file_path)
        processed_data = xml_object.process_data('dict')
        expected_result = {
            'people': {
                'inner': [
                    {
                        'name': {
                            'inner': [
                                'Marry'
                            ]
                        }
                    },
                    {
                        'name': {
                            'inner': [
                                'John'
                            ]
                        }
                    },
                    {
                        'name': {
                            'inner': [
                                'Joseph'
                            ]
                        }
                    }
                ]
            }
        }

        assert processed_data == expected_result
