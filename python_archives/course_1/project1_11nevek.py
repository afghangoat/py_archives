list=[]
for i in range(1,11):
    for j in range(i):
        list.append(i)
    print(*list)
    list=[]

list1=["Szabó ","Vágó ","Kovács ","Antal ","Ahl "]
list2=["Bob","Jani","Jenő","Szabolcs","Gábor"]
for i in range(5):
    for j in range(5):
        print(list1[j]+list2[i])

for k in range(1300,2100):
    if k%7 == 0 and k%4 == 0:
        print(k)

list4=["Bob","Jani","Jenő","Szabolcs","Gábor"]
tmp=0
for i in range(5):

    for j in range(tmp,5):
        if list4[i] != list4[j] and list4[j] != list4[i]:
            print(list4[i]+" és "+list4[j])
    tmp+=1
