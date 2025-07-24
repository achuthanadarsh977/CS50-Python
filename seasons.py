from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth = input("Date of birth:")
    try:
        year,month,day = check_date(birth)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year),int(month),int(day))
    date_today = date.today()
    diff =  date_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    r = p.number_to_words(total_minutes,andword="")
    print(r.capitalize(),"minutes")


def check_date(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birth):
        year,month,day = birth.split("-")
        return year,month,day




if __name__ == "__main__":
    main()
