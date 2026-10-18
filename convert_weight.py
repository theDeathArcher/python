weight = float(input("Weight: "))
unit = str(input("(K)g or (L)bs: ")).lower()

if unit == "k":
    print("Weight in Lbs: " + str(weight * 2.204623))
elif unit == "l":
    print("Weight in Kg: " + str(weight * 0.4535924))
else:
    print("You need to give unit as either lower case or upper case 'k' or 'l'!")