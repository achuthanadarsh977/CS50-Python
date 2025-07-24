
import pytest
from numb3rs import validate

def main():
    test_range()
    test_format()



def test_format():

    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False


def test_range():

    assert validate(r'255.255.255.255') == True
    assert validate(r'512.512.512.512') == False
    assert validate(r'1.1.512.1') == False
    assert validate(r'1.1.1.275') == False


