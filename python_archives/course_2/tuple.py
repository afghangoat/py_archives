import random
empty_tupple=()
tuple1=(1,2,3,4)
tuple2=(True,"Hassan",2,[1,2,3],tuple1)
tuple3=(4,5,6)
print(tuple2)
tuple4=(1)
print(type(tuple4))
tuple5=tuple((1,2,3,4))

list1=[1,2,3]
print(type(list1))
tuple6=tuple(list1)
print(type(tuple6))

#
list1=[1,2,3]
tuple1=(1,2,3)
list1.append(4)
list1.pop(3)
list1.insert(1,10)
list1[2]=20
# del tuple1
#szeletelés
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
print(list1[0:2],tuple1[0:2])
print(list1[3:],tuple1[3:])
print(list1[-3:-1],tuple1[-3:-1])
#hasonlítás
tuple1=(1,2,3)
tuple2=(1,4,5)
print(tuple1==tuple2)
#tuple1=tuple(random.randint(1,10))for i in range(5))
#elemek szorzása
print(tuple1)
for i in range(len(tuple1)):
    print(i*3)

tup1=("asd",1,None)
lis1=[1,"wut",tup1]

tup1=(1,1,1,1,1,2,2,2,2,2,2,3,3,3,1,1,1,2,3)
print(tup1.count(2))
print(random.randint(1,10))