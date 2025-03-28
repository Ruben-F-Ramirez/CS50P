import pytest
from um import count

def main():
    ...

def test_values():
    assert count("um") == 1
    assert count("Um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

if __name__ == "__main__":
    main()