
from twttr import shorten
import pytest

def test_int():
    with pytest.raises(TypeError):
        shorten(55)

def test_cap():
    assert shorten("HEllo") == "Hll"

def test_vowel():
    assert shorten("aeiou") == ""