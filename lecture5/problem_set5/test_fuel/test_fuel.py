
from fuel import convert, gauge

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_float():
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_big_num():
    with pytest.raises(ValueError):
        convert("4/3")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(45) == "45%"