name="logirobi"
age=8
print("Szia, " + name + " vagyok, " + str(age) + " éves!")
print("Szia, %s vagyok,  %d  éves!" %(name,age))
# %s,%d {var}
#HF

#ossz=int(print("1"))
#if ossz==2:
#    print("Remek! Nem vagy hülye!")
#else:
#    print("Remek! Hülye vagy!")
kor=int(input(print("Mi az életkorod?")))
if kor>18:
    print("Felnőtt vagy!")
elif kor<18:
    print("Gyerek vagy!")
elif kor==18:
    print("Pont 18 vagy!")
#Task5
a1=int(input(print("1.szám?")))
a2=int(input(print("2.szám?")))
if a1>a2:
    print("1. szám nagyobb")
elif a1<a2:
    print("2. szám nagyobb")
elif a1==a2:
    print("Egyenlőek a számok")
#jelszó, 8 char,1 szám, 1 nagy betű
password=str(input(print("Password:")))
if password.__len__()>=8:
    print("ez nagyobb 8 karakternél.")