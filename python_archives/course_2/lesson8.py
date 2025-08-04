#
tup1=(1,2,3)
tup2=(3,4,5)
tup3=(1,4,5)
print(tup1)
print(tup2)
print(tup3)
tup1, tup2, tup3 = tup3, tup2, tup1
print(tup1)
print(tup2)
print(tup3)
tup1=(1,2,3,4)
print(tup1)
list_tup=list(tup1)
list_tup.insert(2,"Logischool")
tup1=tuple(list_tup)
print(tup1)
tup1=tup1[:1]+(33,)+tup1[1:]
tup1=tup1[:5]+(33,)+tup1[5:]
print(tup1)

"""
tup1 = ((1, 2, 3), (3, 4), (10, 20, 60), (3, 4, 5))
for i in range(len(tup1)):
    k = 0
    kk = 0
    for j in range(len(tup1[i])):
        k += tup1[i][j]
    kk = k/len(tup1)
    print(kk)
#input tub1,tup2
list1=[]
list2=[]
for i in range(5):
    list1.append(int(input("1. elemei: ")))
for i in range(5):
    list2.append(int(input("2. elemei: ")))
tup1=tuple(list1)
tup2=tuple(list2)
tup3=sorted(tup1)
tup4=sorted(tup2)
print(tup1,tup2,tup3,tup4)
if tup3 == tup4:
    print("ugyanazok.")
if tup3 != tup4:
    print("nem ugyanazok.")
    """
testlist1=[(6,7),(2,3),(7,6),(9,8),(10,2)]
symetric=[]
for i in testlist1:
    temp=i[::-1]
    if temp not in symetric:
        if temp in testlist1:
            symetric.append(i)
if len(symetric) != 0:
    print("Vannak symetrikus értékek:",symetric)
else:
    print("Nincsenek symetrikus értékek:")

test_tuple=("g","f","h")
start=test_tuple[0]
items=[]
for i in test_tuple[1:]:
    item=(start,i)
    items.append(item)
items=tuple(items)
print(items)
testlist=[(3,4),(78,76),(2,3),(9,8),(19,23)]
tup=(17,23)
K=1
Min_dif=999999
result_index= 0
for i in range(len(testlist)):
    difference=abs(tup[i][K]-tup[K])
    if difference<Min_dif:
        result_index=i
        mind_dif = difference
print(str(testlist[result_index]))
#5db szám bekérése, pontszám. létrehozunk ezekből egy tuple-t aminek tuple-k az elemei, 1. tup a név, 2. a jegy
list1=[]
for i in range(5):
    list1.append(int(input("elem: ")))
    list1.append(int(input("diák: ")))

for i in range(len(list1)):
    k = 0
    ig = 0
    im = 9999999
    kk = 0
     if type(list1[i]) == int:
         if ig <= list1[i]:
             ig = list1[i]
          if im >= list1[i]:
            im = list1[i]
         k += list1[i]
    if type(list1[i]) == int:
        kk = k/len(list1)
tup1=tuple(list1)
print(tup1)
#HF: Adott egy tuple, amely egy bináris szám számjegyeit tartalmazza. Írjunk programot, amely kiadja a tízes számrendszer-beli alakot. (bitwise operators)