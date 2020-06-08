class XML:
    def __init__(self, tag):
        self._ending_tag = tag.startswith('</')
        if self._ending_tag:
            formatted_tag = tag[2:-2]
        else:
            formatted_tag = tag[1:-2]
        self.tag_name = formatted_tag.split(' ')[0]
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def set_value(self, new_value):
        self._value = new_value