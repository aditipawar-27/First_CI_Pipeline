import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_basic_sum():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([9]) == 9


def test_negative_numbers():
    assert sum_of_list([-1, -2, 3]) == 0


def test_float_numbers():
    assert sum_of_list([1.5, 2.5]) == 4.0
