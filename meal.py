def main():
     time = input("What time is it?")
     seconds = convert(time)

     if 7<=seconds<=8:
          print("breakfast time")

     elif 12<=seconds<=13:
          print("lunch time")

     elif 18<=seconds<=19:
          print("dinner time")

     else:
          print(" ")

def convert(time):
     z = time.split(":")
     hours = int(z[0])
     minutes = int(z[1])
     clock = hours + (minutes/60)
     return clock

if __name__ == "__main__":
    main()





