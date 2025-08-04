#List
#Task1
names = ["Józsi","Dezső","Szabolcs","Gergő","Zsombor","Kreatívnév"]
print(names)
print(type(names))
print(names[len(names)-1])
print(names[-1])
print(names[-2])
print(names[-6])
print(names[-len(names)])
#Task2
num1=len(names)
num2 = 0
while num1!=0:
    print(names[num2])
    num2+=1
    num1-=1
#Task3
nums=[]
i=1
while i<=50:
    nums.append(i)
    print(nums[i-1])
    i+=1
#Task4
insertlist= [1,3,2,8]
print(insertlist)
#insertlist.remove(8)
insertlist[3] = 10
insertlist.append(9)
print(insertlist)
insertlist.insert(0,1)
print(insertlist)
insertlist.insert(6,12)
print(insertlist)
girl_names=["Anne","Jenny","Sophie","Péter"]
boy_names=["George","John","Katie","Dezső"]
print(girl_names)
print(boy_names)
gn=girl_names[3]
bn=boy_names[2]
girl_names.pop(3)
boy_names.remove("Katie")
print(girl_names)
print(boy_names)
boy_names.insert(2,gn)
girl_names.insert(2,bn)
print(girl_names)
print(boy_names)
#task5
numlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd=[]
even=[]
num1=len(numlist)
num2=0
while num1!=0:
    if numlist[num2]%2 == 1:
        odd.append(numlist[num2])
    else:
        even.append(numlist[num2])
    num2+=1
    num1-=1
print(odd)
print(even)
#1. list,summája
#2. list, legyenek benne ismétlődő elemek. válasszunk egy elemet és számoluk meg a számát.
list3=[1,2,3,4,5,6,7,8,9,10]
num1=len(list3)
sum22=0
while num1!=0:
    sum22+=num1
    num1-=1
print("össz:",sum22)
list3=[1,2,2,2,2,3,4,5,5,6]
xnum=input(print("melyik elem lenne ez:"))
num1=len(list3)
num2=0
while num1!=0:
    if num1==xnum:
        xnum
    num1-=1
print("ennyi elem van:",num2)

