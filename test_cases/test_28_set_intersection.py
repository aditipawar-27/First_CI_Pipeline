import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_basic_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_empty_sets():
    assert set_intersection(set(), set()) == set()


def test_one_empty_set():
    assert set_intersection({1, 2, 3}, set()) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_string_elements():
    assert set_intersection({"a", "b"}, {"b", "c"}) == {"b"}
