
from plates import is_valid

def test_length():
    assert is_valid("a") == False
    assert is_valid("aa") == True
    assert is_valid("aa1") == True
    assert is_valid("aabb12345") == False

def test_first_letters():
    assert is_valid("12aa34") == False
    assert is_valid("aabb12") == True

def test_last_nums():
    assert is_valid("aa12bb") == False
    assert is_valid("aabb01") == False
    assert is_valid("aabb12") == True
    assert is_valid("NRVOUS") == True

def test_punct():
    assert is_valid("aabb12") == True
    assert is_valid("aa,b12") == False
    assert is_valid("aa.,2") == False