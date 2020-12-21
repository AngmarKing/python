import time

zeit = time.localtime()

print("Datum: %d.%d.%d"%(zeit[2], zeit[1], zeit[0]))
print("Uhrzeit: %d:%d:%d"%(zeit[3], zeit[4], zeit[5]))
