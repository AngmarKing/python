import time

zeit = time.localtime()

print("Datum: %d.%d.%d"%(zeit[2], zeit[1], zeit[0]))
print("Uhrzeit: %d:%d:%d"%(zeit[3], zeit[4], zeit[5]))

#print("Der Logarithmus von %d zur Basis %d ist %f."%(x, basis, ergebnis))
#def wuerfeln():
#    return random.randint(1, 6)


#print("Ergebnis:", wuerfeln() )
