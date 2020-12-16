def personendaten (name = "unbekannt", wohnort = "unbekannt", alter = "unbekannt"):
    print ("Name: ", name)
    print ("Wohnort: ", wohnort)
    print ("Alter: ", alter)

personendaten()
personendaten("Herbert Müller")
personendaten("Herbert Müller", "Kassel")
personendaten("Herbert Müller", "Kassel", 51)
personendaten(wohnort = "Kassel")