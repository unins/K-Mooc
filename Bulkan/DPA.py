import time

print ("Enter your name")
name = input()

if name == "Parksungha":
    print ("Name %s Registered" %name)
    print ("Loading DPA Data Base")
    time.sleep (5)
    print ("Failed to connect to Data Base : Server offline")
else :
    print ("Can't Find Name %s in DPA Data Base" %name)
    print ("Access Denied")
