class Auto:
    """
    Erstellt das Objekt Auto
    """
    def __init__(self, ma, mo, bj, pr):
        """
        Initialisiert ein neues Objekt Auto
        """

        self.__Marke = ma
        self.__Modell = mo
        self.__Baujahr = bj
        self.__Preis = pr 


    def getMarke(self):
        """
        Gibt die Marke des Autos zurück.
        """
        return self.__Marke

    def getModell(self):
        """
        Gibt die Marke des Autos zurück.
        """
        return self.__Modell

    def getBaujahr(self):
        """
        Gibt die Marke des Autos zurück.
        """
        return self.__Baujahr

    def getPreis(self):
        """
        Gibt die Marke des Autos zurück.
        """
        return self.__Preis

    def setPreis(self, preis_neu):
        """
        Ändert den Preis des Autos
        """
        if abs(self.__Preis - preis_neu) < self.__Preis * 0.05:
            self.__Preis = preis_neu
        else:
            print ("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis"%preis_neu + "festgelegt werden?(ja/nein)")
            if bestaetigung == "ja":
                self.__Preis = preis_neu


auto1 = Auto("VW","Golf",2001,5000)
auto2 = Auto("Peugeot","508sw",2019,15000)
auto3 = Auto("BMW","440i",2020,40000)

wert = eval(input("Geben Sie den neuen Preis ein: "))
auto1.setPreis(wert)

print("Neuer Preis:",auto1.getPreis())