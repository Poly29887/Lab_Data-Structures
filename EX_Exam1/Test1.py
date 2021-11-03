print(" *** Wind classification ***")
inp = float(input("Enter wind speed (km/h) : "))
s="Wind classification is "
if inp<0:
    s="!!!Wrong value can't classify."
elif inp <= 51.99:
    s+="Breeze."
elif inp <= 55.99:
    s+="Depression."
elif inp <= 101.99:
    s+="Tropical Storm."
elif inp <= 208.99:
    s+="Typhoon."
else:
    s+="Super Typhoon."
print(s)