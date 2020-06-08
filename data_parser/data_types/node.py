class Node:
    def __init__(self, parent=None):
        self._parent = parent
        self._children = []
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def set_value(self, new_value):
        self._value = new_value

    @property
    def children(self):
        return self._children

    def add_child(self, child):
        self._children.append(child)

    @property
    def parent(self):
        return self._parent
