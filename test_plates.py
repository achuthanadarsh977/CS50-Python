from plates import is_valid




def test_numbersinbetween():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_min_and_max_characters():
    assert is_valid("OUTATIME") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("AA") == True
    assert is_valid("H") == False



def test_two_characters():
    assert is_valid("AA") == True
    assert is_valid("2A") == False
    assert is_valid("33") == False
    assert is_valid("A3") == False







