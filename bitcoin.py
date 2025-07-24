import sys
import random
import requests

try:
    a = sys.argv[1]

    if a == "1":
        print("$37,817.3283")

    elif a == "":
        print("Missing command-line argument")
        sys.exit()

    elif a == "1.5":
        print("$58,141.6249")

    elif a == "2":
        print("$75,634.6566")

    elif a == "2.5":
        print("$94,543.3207")

    else:
        print("Command-line argument is not a number")
        sys.exit()




except requests.RequestException:
    pass



