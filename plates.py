


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def denmark(s):
    l = []
    for i in s:
        if i.isdigit():
            l.append(i)

def is_valid(s):
   d=0
   if (2<=len(s)<=6) and (s.isalnum()):
         if s[0:2].isalpha():
             if s.isalpha():
                 return True
             else:
                 for i in range(len(s)):
                     if s[i].isdigit():
                         d=i
                         break
                 if (s[d]=='0'):
                     return False
                 else:
                     for i in range(d,len(s)):
                         if (s[i].isalpha()):
                             return False
                     else:
                         return True







if __name__ == "__main__":
      main()
