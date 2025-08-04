import math
import random
import matplotlib.pyplot as plt
def piechart(size,ls):
    plt.pie(size,labels=ls,autopct='%.2f%%')
    plt.show()
n = int(input("Hány játékot szeretsz?"))
list1 = []
list2 = []
data = []
db = 0
s = 0
for i in range(n):
    game_name = (input("Mi a játék neve?"))
    likes = int(input("Mennyire szereted 10-1?"))
    db += likes
    list1.append(game_name)
    list2.append(likes)
for i in range(n):
    s=list2[i]/db*100
    s=round(s,1)
    data.append(s)#

piechart(data,list1)
#BMI = ( tömeg / (magasság)^2),
t = int(input("tömeg?"))
m = int(input("magasság?"))
bmi1=0
def bmi(t,m):
    bmi1=(t/ math.pow(m,2))
    print(bmi1)
bmi(t,m)
#2. Az óra első felében generáltunk egy véletlen számokból álló listát. A feladat az, hogy ebből készítsünk egy diagrammot, amely megmutatja, hogy melyik szám hány százalékban fordult elő a listában.