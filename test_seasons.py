from seasons import check_date

def main():
    test_format()




def test_format():
    assert('January 1, 1999') == "None"
    assert('1998-7-3') == "None"
    assert('1998-07-03') == ("1998" , "07" , "03")


