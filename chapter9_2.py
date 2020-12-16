#def formel (x):
#    wert = 2 * x * x + 4 * x + 9
#    return wert
#
#ergebnis = formel(4)
#print(ergebnis)

#def formel (x):
#    return 2 * x * x + 4 * x + 9
#print (formel(4))

#def formel (x):
#    wert1 = 2 * x * x + 4 * x + 9
#    wert2 = 3 * x * x + 2 * x - 7
#    return [wert1, wert2]
#
#ergebnisse = formel (4)
#print ("Ergebnis der ersten Formel:",ergebnisse[0])
#print ("Ergebnis der zweiten Formel:",ergebnisse[1])

def formel (x):
    if 2 * x * x + 4 * x + 9 > 50:
        return 2 * x * x + 4 * x + 9
    else:
        return 3 * x * x + 2 * x - 7

eingabe = eval(input("Geben Sie eine zahl ein: "))
print (formel(eingabe))