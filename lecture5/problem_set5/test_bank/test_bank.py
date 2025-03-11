
from bank import value
import pytest

def test_int():
    with pytest.raises(ValueError):
        value(55)

def test_lower():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("What's up?") == "$100"

def test_upper():
    assert value("HELLO") == "$0"

def test_h():
    assert value("Hi") == "$20"
    assert value("Hey") == "$20"