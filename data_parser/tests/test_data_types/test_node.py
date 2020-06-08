from data_parser.data_types.node import Node


def test_create_empty_node():
    root = Node()

    assert root.value is None
    assert root.parent is None
    assert root.children == []


def test_create_node_with_values():
    root = Node()
    test_node = Node()

    root.add_child(test_node)
    root.value = dict()

    assert root.value == dict()
    assert root.children == [test_node]
    assert test_node.parent is root
