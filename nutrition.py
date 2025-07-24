fruits = {"Apple":130,"Avocado":50,"Banana":110,"Grape":90,"apple":130,"pear":100,
          "Honeydew Melon":50,"Kiwifruit":90,"Lemon":15,"Lime":20,
          "Nectarine":60,"Orange":80,"Peach":60,"Pear":100,
          "Pineapple":50,"Plums":70,"Strawberries":50,"Sweet Cherries":100,"Tangerine":50,"Watermelon":80}

k = input("Item:")
if k in fruits.keys():
    print("Calories:",fruits[k])



