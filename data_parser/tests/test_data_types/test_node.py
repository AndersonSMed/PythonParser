from data_parser.data_types.node import Node


def test_create_empty_node():
    root = Node()

    assert root.value is None
    assert root.parent is None
    assert root.children == []