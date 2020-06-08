class Node:
    def __init__(self, parent=None):
        self._parent = parent
        self._children = []
        self._value = None

    def add_child(self, child):
        self._children.append(child)
        child.set_parent(self)

    def set_parent(self, parent):
        self._parent = parent

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent
