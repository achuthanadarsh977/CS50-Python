def main():
    dollars = input("How much was the meal?")
    percent = input("What percentage would you like to tip? ")

    tip = float(dollars.strip("$")) * (float(percent.strip("%"))/100)
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    d = float(d.strip("$"))

def percent_to_float(p):
    p = float(p.strip("%"))/100


main()






