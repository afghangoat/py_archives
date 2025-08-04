import random
#sorting
list1=["Alice","Bob","Ahmed","Józsi","Dezső","Géza","János","Tomi","Márió"]
list2=[123.42,153.1,313.2,42.1,421.1,165.30,68.27,88.8,88.1]
for i in range(len(list2)-1):
    for j in range(i+1,len(list2)):
        if list2[i]>list2[j]:
            list2[i],list2[j]=list2[j],list2[i]
            list1[i], list1[j] = list1[j], list1[i]
print(list2)
print(list1)
list1=["Alice","Bob","Ahmed","Józsi","Dezső","Géza","János","Tomi","Márió"]
list2=[123.42,153.1,313.2,42.1,421.1,165.30,68.27,88.8,88.1]
for i in range(len(list2)):
    for j in range(len(list2)-1):
        if list2[j]>list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list2)
print(list1)
list2.sort()
print(list2)

rndlist=random.sample(range(1,100),10)
print(rndlist)
rndlist.sort()
print(rndlist)
#feladatok
rlist1=random.sample(range(1,100),10)
rlist2=random.sample(range(1,100),10)
rlist3={}
rlist3=rlist1+rlist2
print(rlist3)
#2
rlist2=random.sample(range(1,100),10)
tmp2=0
for i in range(len(rlist2)):
    tmp2+=rlist2[i]
print(int(tmp2))
#3
rlist1=random.sample(range(1,100),10)
rlist2=random.sample(range(1,100),10)
for i in range(len(rlist1)):
    if rlist1[i] not in rlist2:
        rlist2.append(rlist1[i])

for i in range(len(rlist2)):
    if rlist2[i] not in rlist1:
        rlist1.append(rlist2[i])
rlist1.sort()
rlist2.sort()
print(rlist1)
print(rlist1)
#4
rlist1=random.sample(range(1,100),10)
rla=False
for i in range(len(rlist1)):
    for j in range(i+1):
        if rlist1[i]>rlist1[j]:
            rla=True

if rla ==True:
    print("Nincs növekvő sorrendbe!")
else:
    print("Növekvő sorrendbe van!")
#5
items = ["apple", "book", "bread", "cheese", "chicken", "curry sauce","doughnut", "toilet roll", "socks", "toothpaste"]
prices = [1500, 1000, 700, 1600, 1900, 600, 800, 999, 500, 550]
list4=[]
for i in range(len(prices)):
    if prices[i] < 1000:
        list4.append(items[i])
print(list4)
#6
fib=2
for i in range(100):
    fib+=fib + 1
print(fib)
#7
payment = 0
hp1sk1="Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense."
for i in range(len(hp1sk1)):
    payment+=2
print("Betűnként:"+str(payment))
payment=12*(hp1sk1.count(" ")-1)
print("Szavanként:"+str(payment))
#8
name = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
age = [26, 31, 35, 41, 58, 30, 46, 61, 25]
gender = ["male", "female", "male", "female", "female", "male", "male", "male", "female"]
job = ["web developer", "marketing director", "content creator", "human resources", "CEO", "software developer", "public relations manager", "tester", "sales representative"]
salary = [1500, 1500, 1400, 1300, 1400, 1500, 1400, 1300, 1500]
for i in range(len(name)-1):
    for j in range(i+1,len(name)):
        if name[i]>name[j]:
            name[i],name[j]=name[j],name[i]
            age[i], age[j] = age[j], age[i]
            gender[i], gender[j] = gender[j], gender[i]
            job[i], job[j] = job[j], job[i]
            salary[i], salary[j] = salary[j], salary[i]
print(name)
print(age)
print(gender)
print(job)
print(salary)