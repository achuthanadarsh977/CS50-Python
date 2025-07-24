
y = input("Expression:")

x = float(y[0]) or float(y[1])
z = float(y[4]) or float(y[5])
y.split(",")
if y[2] == "+" or y[3] == "+":
    print(float(x+z))

elif y[2] == "-" or y[3] == "-":
    print(float(x-z))

elif y[2] == "*" or y[3] == "*":
    print(float(x*z))

elif y[2] == "/" or y[3] == "/":
    print(float(x/z))


else:
    print("None")



