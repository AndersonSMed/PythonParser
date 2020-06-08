class XML:
    def __init__(self, tag):
        self._ending_tag = None
        if tag.startswith('</'):
            raise ValueError('You cannot create a XML object with an ending tag')
        self.tag_name = tag[1:-1].split(' ')[0]
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def ending_tag(self):
        return self._ending_tag