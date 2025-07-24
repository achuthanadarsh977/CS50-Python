import inflect


p = inflect.engine()




while True:

    try:
       name = input("Name:")
       continue

    except:

        if name == "Liesl":
            print("Adieu, adieu, to Liesl")
            break

        elif name == "Friedrich":
             print("Adieu, adieu, to Liesl and Friedrich")
             break

        elif  name == "Louisa":
              print("Adieu, adieu, to Liesl, Friedrich, and Louisa")
              break

        elif name == "Kurt":
            print("Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt")
            break

        elif name == "Brigitta":
            print("Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta")
            break

        elif name == "Marta":
            print("Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta and Marta")
            break

        elif name == "Gretl":
            print("Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl")
            break



        else:
             continue
