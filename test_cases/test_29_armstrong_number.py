import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) is True


def test_not_armstrong_number():
    assert is_armstrong(123) is False


def test_zero():
    assert is_armstrong(0) is True


def test_single_digit():
    assert is_armstrong(5) is True


def test_negative_number():
    assert is_armstrong(-153) is False


def test_four_digit_armstrong():
    assert is_armstrong(9474) is True


def test_four_digit_not_armstrong():
    assert is_armstrong(9475) is False
