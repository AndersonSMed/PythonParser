from data_parser.parsers.base_parser import BaseParser
from data_parser.data_types.node import Node
from data_parser.data_types.xml import XML


class XMLParser(BaseParser):
    _enabled_outputs = ['dict']
    _output_mapper = {
        'dict': dict
    }

    def _data_to_internal_format(self):
        root = Node()
        parent = None
        grandpa = None
        temp_string = ''

    def _is_a_tag(self, string):
        return string.endswith('>') and (string.startswith('<')
                                         or string.startswith('</'))

    def _get_output(self, mapped_output):
        pass