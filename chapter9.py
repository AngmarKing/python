def begruessung (name, zahl):
    print ("Herzlich Willkommen,", name, "!")
    print("Die eingegebene zahl lautet", zahl)

eingabe1 = input("Geben Sie bitte Ihren Namen ein: ")
eingabe2 = eval(input("Geben Sie eine Zahl ein: "))
begruessung(eingabe1, eingabe2)