from bank import value

def main():
    test_bank1()

    test_bank2()

    test_bank3()






def test_bank1():
      assert value("hello, world") == 0
      assert value("  hello  ") == 0
      assert value("HELLO") == 0

def test_bank2():
     assert value("hi") == 20
     assert value("heck even") == 20


def test_bank3():
     assert value("What's up?") == 100
     assert value("good morning") == 100
     assert value("cs50") == 100



if __name__ == "__main__":
    main()
