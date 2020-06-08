import json


class XML:
    _error_messages = {
        'ending_tag': (
            'You cannot create a XML object with an ending tag.'
        )
    }

    def __init__(self, tag):
        self._attributes = {}
        self._validate_tag(tag)
        self._process_tag(tag)
        self._inner_value = None

    def _validate_tag(self, tag):
        if tag.startswith('</'):
            raise ValueError(self._error_messages['ending_tag'])

    def _process_tag(self, tag):
        attribute_list = tag.replace('/', '')[1: -1].split(' ')
        self._tag_name = attribute_list.pop(0)
        for attribute in attribute_list:
            name, value = attribute.split('=')
            self._attributes[name] = json.loads(value)

    @property
    def inner_value(self):
        return self._inner_value

    @inner_value.setter
    def inner_value(self, value):
        self._inner_value = value

    @property
    def attributes(self):
        return self._attributes

    @property
    def tag_name(self):
        return self._tag_name
