print("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: ")
wert = input()

if (len(wert) > 1 ):
    print("too big")
elif (wert == ""):
    print("not in 0-9")
else:
    print("yes")
    