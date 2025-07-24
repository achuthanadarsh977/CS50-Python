from validator_collection import validators, checkers, errors

def main():
    ema = input("What's your email address?")
    try:
        emailisValid = validators.email(ema)
        print("Valid")


    except:
        print("Invalid")





if __name__ == "__main__":
    main()
