import pytest

from working import convert


def main():
    test_convert_time()
    test_valerror()

def test_convert_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:50 AM to 5 PM") == "09:50 to 17:00"
    assert convert("9 AM to 5:23 PM") == "09:00 to 17:23"

def test_valerror():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:80 PM")

    
if __name__ == "__main__":
    main()