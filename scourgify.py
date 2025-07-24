import sys
import csv



def main():

    check_command()
    scout = []

    try:
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                spill = row["name"].split(",")
                scout.append({'first':spill[1].lstrip(),"last":spill[0],"house":row["house"]})




    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})

        for row in scout:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})









def check_command():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit(f"Could not read {sys.argv[1]}")











if __name__ == "__main__":
    main()
