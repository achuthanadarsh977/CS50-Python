from fuel import convert , gauge
import pytest








def test_convert():

    assert convert("1/4") == 25

    assert convert("1/2") == 50

    assert convert("3/4") == 75


def test_convert1():

    with pytest.raises(ValueError):
        assert convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")



def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"



