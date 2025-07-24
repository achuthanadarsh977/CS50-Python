import sys
import csv


def main():

    check_split()
    try:

        with open(sys.argv[1]) as file:
            print(file.read())


    except FileNotFoundError:
        sys.exit("File does not exist")









def check_split():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file  ")








if __name__ == "__main__":
    main()
