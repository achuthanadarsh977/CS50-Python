salads ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Super quesadilla": 9.50,
    "tortilla salad": 8.00,
    "burrito": 7.50,
    "nachos": 11.00,
    "bowl": 8.50,
    "taco": 3.00,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



try:
 while True:
    item = input("Item:")
    if item in salads.keys():
             print(f"Total: ${salads[item]}0")
             for i in salads.keys():
                 i = input("Item:")
                 salads[item]+=salads[i]
                 print(f"Total: ${salads[item]}0")
             continue
    else:
        continue





except EOFError:
    pass










