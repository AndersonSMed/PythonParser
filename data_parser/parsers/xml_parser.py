from data_parser.parsers.base_parser import BaseParser


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
        for char in self._raw_data:
            if char == '\n':
                continue
            temp_string = '{}{}'.format(temp_string, char)
            if self._is_a_tag(temp_string):
                xml = XML(temp_string)
                if xml.ending_tag:
                    mapping.pop()
                else:
                    mapping.append(xml.tag_name)
                    temp_dict
                temp_string = ''

    def _is_a_tag(self, string):
        return string.endswith('>') and (string.startswith('<')
                                         or string.startswith('</'))

    def _get_output(self, mapped_output):
        pass