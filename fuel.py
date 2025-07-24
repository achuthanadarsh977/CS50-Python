

def main():
   fraction = input("Fraction:")
   percentage = convert(fraction)
   con = gauge(percentage)
   print(con)


def convert(fraction):

   while True:
     a,b = fraction.split("/")
     a = int(a)
     b = int(b)
     c = (a/b)
     if a < b and c <= 1:
       d = int(c * 100)
       return d

     elif a > b:
       raise ValueError("X is greater than Y")

     elif type(a) or type(b) == str:
       raise ValueError("X and/or Y is not an integer")

     elif b == 0:
       raise ZeroDivisionError("division by zero")




def gauge(percentage):

  if percentage >= 99:
    return "F"

  elif percentage <= 1:
    return "E"

  else:
    return str(percentage)+"%"





if __name__ == "__main__":
    main()
