
from numb3rs import validate
import pytest

def test_int():
    with pytest.raises(ValueError):
        validate("cat")
