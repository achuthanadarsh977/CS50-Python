from calculator import square



def main():
    test_square()


def test_square():
      try:
            assert square(2) == 4

      except AssertionError:
            print("2 squared is not 4")

      try:
            assert square(-3) == 9

      except AssertionError:
            print("-3 squared is not 9")

      try:
            assert square(-5) == 25

      except AssertionError:
            print("-5 squared is not 25")





if __name__ == "__main__":
        main()

