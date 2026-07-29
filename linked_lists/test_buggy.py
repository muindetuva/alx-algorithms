import importlib
import sys

from buggy_linked_list import Node, LinkedList


def select_implementation():
    global Node, LinkedList
    module_name = sys.argv[1] if len(sys.argv) > 1 else "buggy_linked_list"
    module = importlib.import_module(module_name)
    Node = module.Node
    LinkedList = module.LinkedList
    return module_name


def make_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list


def test_append():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.to_list() == ["A", "B", "C"]
    assert linked_list.tail.data == "C"


def test_prepend():
    linked_list = make_list(["B", "C"])
    linked_list.prepend("A")
    assert linked_list.to_list() == ["A", "B", "C"]
    assert linked_list.tail.data == "C"


def test_insert_at_middle():
    linked_list = make_list(["A", "C"])
    linked_list.insert_at(1, "B")
    assert linked_list.to_list() == ["A", "B", "C"]


def test_insert_at_head():
    linked_list = make_list(["B"])
    linked_list.insert_at(0, "A")
    assert linked_list.to_list() == ["A", "B"]


def test_insert_at_tail():
    linked_list = make_list(["A"])
    linked_list.insert_at(1, "B")
    linked_list.append("C")
    assert linked_list.to_list() == ["A", "B", "C"]


def test_delete_middle():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.delete("B") is True
    assert linked_list.to_list() == ["A", "C"]


def test_delete_head():
    linked_list = make_list(["A", "B"])
    assert linked_list.delete("A") is True
    assert linked_list.to_list() == ["B"]
    assert linked_list.head is linked_list.tail


def test_delete_tail():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.delete("C") is True
    assert linked_list.to_list() == ["A", "B"]
    linked_list.append("D")
    assert linked_list.to_list() == ["A", "B", "D"]
    assert linked_list.tail.data == "D"


def test_delete_only_node():
    linked_list = make_list(["A"])
    assert linked_list.delete("A") is True
    assert linked_list.to_list() == []
    assert linked_list.head is None
    assert linked_list.tail is None


def test_delete_at():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.delete_at(1) == "B"
    assert linked_list.delete_at(1) == "C"
    assert linked_list.to_list() == ["A"]
    assert linked_list.tail.data == "A"


def test_reverse():
    linked_list = make_list(["A", "B", "C"])
    linked_list.reverse()
    assert linked_list.to_list() == ["C", "B", "A"]
    assert linked_list.head.data == "C"
    assert linked_list.tail.data == "A"


def test_reverse_then_append():
    linked_list = make_list(["A", "B", "C"])
    linked_list.reverse()
    linked_list.append("D")
    assert linked_list.to_list() == ["C", "B", "A", "D"]


def test_length():
    linked_list = LinkedList()
    assert linked_list.length() == 0
    linked_list.append("A")
    linked_list.append("B")
    assert linked_list.length() == 2


def test_search():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.search("B") == 1
    assert linked_list.search("Z") == -1


def test_has_cycle():
    linked_list = make_list(["A", "B", "C"])
    assert linked_list.has_cycle() is False
    linked_list.tail.next = linked_list.head
    assert linked_list.has_cycle() is True
    linked_list.tail.next = None


TESTS = [
    test_append,
    test_prepend,
    test_insert_at_middle,
    test_insert_at_head,
    test_insert_at_tail,
    test_delete_middle,
    test_delete_head,
    test_delete_tail,
    test_delete_only_node,
    test_delete_at,
    test_reverse,
    test_reverse_then_append,
    test_length,
    test_search,
    test_has_cycle,
]


def main():
    module_name = select_implementation()
    failures = []
    print(f"Running tests on {module_name}.py...\n")

    for test in TESTS:
        try:
            test()
            print(f"{test.__name__}: PASSED")
        except Exception as error:
            failures.append(test.__name__)
            print(f"{test.__name__}: FAILED — {error}")

    if failures:
        names = ", ".join(failures)
        raise AssertionError(f"Failed tests: {names}")
    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
