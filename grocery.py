food = {}
x = food.keys()
while True:
    try:
       lock= input().lower()
       if lock in food:
          food[lock]+=1

       else:
          food[lock]=1


    except EOFError:
       print()
       for i in sorted(x):
          print(food[i],i.upper())

       break

