import pytest

from working import convert


def test_convert_time():
    assert convert("9 AM to 5 PM") == "0900 to 1700"
    assert convert("9:00 AM to 5 PM") == "0900 to 1700"
    assert convert("9:00 AM to 5:00 PM") == "0900 to 1700"
    assert convert("9 AM to 5:00 PM") == "0900 to 1700"
    assert convert("9:50 AM to 5 PM") == "0950 to 1700"
    assert convert("9 AM to 5:23 PM") == "0900 to 1723"

def test_valerror():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:80 PM")

    
