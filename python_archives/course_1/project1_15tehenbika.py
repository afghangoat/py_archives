print(f"""I wandered lonely as a cloud
That floats on high o’er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
    Beside the lake, beneath the trees,
    Fluttering and dancing in the breeze.""")
#2
#A kúp térfogata: (Alapkör terület* kúp magasság)/3
alap=int(input("Alap:?"))
magas=int(input("Magasság:?"))
egyenlo=(int(alap)*int(magas))/3
print(egyenlo," A térfogat")
#3
valt1=int(input("1:?"))
valt2=int(input("2:?"))
#----
tmp=valt1
valt1=valt2
valt2=valt1
#----
valt1, valt2 = valt2, valt1
#4
list1=[]
for i in range(1):
    valt3 = int(input("A num:?"))
    list1.append(valt3)

print(list1,sep=",")
#5

list_1 = [4, 8, 15, 16, 23, 42]
par=[]
part=[]
for i in range(len(list_1)):
    if list_1[i] %2 == 0:
        par.append(list_1[i])
    else:
        part.append(list_1[i])

print(par,"<-- páros")
print(part,"<-- páratlan")
#6
items = ["strawberry", "grape", "apple", "orange", "watermelon", "banana", "lemon", "avocado", "other"]
popularity = [15, 17, 16, 10, 9, 18, 7, 5, 3]
mostpop=0
mostpo2=""
for i in range(len(popularity)):
    if popularity[i] >= 0:
        mostpop=popularity[i]
        mostpo2=items[i]
print(mostpo2)
#7
numbers = [61, 70, 12, 34, 76, 94, 26, 93, 10, 1, 90, 71, 32, 89, 97, 41, 95, 6, 18, 20, 73, 46, 21, 31, 72, 22]
print(numbers)
numberss=[]
tru=True
while tru==True:
    if numbers[i] % 7 == 0:
        numbers[i]+=1
    else:
        numberss.append(numbers[i])
        tru=False
print(numbers)
print(numberss)
#8
mondat="Egyszer majd a hitetlenek vére fogja mosni a partot, mondta Hassan."
count=0
for i in range(len(mondat)):

    if str(mondat[i]) == "a" or mondat[i] == "á" or mondat[i] == "e" or mondat[i] == "é" or mondat[i] == "i" or mondat[i] == "í" or mondat[i] == "o" or mondat[i] == "ó" or mondat[i] == "u" or mondat[i] == "ú" or mondat[i] == "ű" or mondat[i] == "ü":
        count+=1

print(count)
#9
int1=int(input("Szám:"))
int2=0
for i in range(int1):
    int2+=(i*1)
print(int2)
print(int1," szer adtunk össze.")
#10
#10.Cows and bulls/master mind
#A játékban van egy előre megadott négy jegyű szám, amit nem ismerünk. A feladatunk, hogy kitaláljuk ezt a számot úgy, hogy mi is tippelünk egy négyjegyű számot, amiről a program elmondja, hogy a számjegyek közül mennyi van benne és jó helyen (cows), illetve mennyi van benne, de rossz helyen (bulls)(nyilván ha ez a kettő nem adja ki a négyet, akkor van olyan szám a tippünkben, ami nem szerepel a kitalálandó számban.).
prenum="6843"
numyour=0
bads=0
good=0
while prenum != numyour:
    bads = 0
    good = 0
    numyour = str(input("Tippelj:"))
    for i in range(4):
        if list(prenum[i]) == list(numyour[i]):
            good +=1
        if list(numyour[i]) in prenum:
            bads +=1
    print(good," <-Cows")
    print(bads, " <-Bulls")
print("Nyertél!")