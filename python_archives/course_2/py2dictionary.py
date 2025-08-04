dictionary={"Cat":"Katze","Dog":"Hund","Horse":"Pferd"}
phonenumber={"Béla":7686563,"Sanyi":71238747}
empty=dict()
print(dictionary["Cat"])
words=["Cat","Lion","Monkey"]
for word in words:
    if word in dictionary:
        print(dictionary[word])
    else:
        print("Not found")
animals={
    "Dog":"Hund",
    "Cat":"Katze",
    "Horse":"Pferd",
}
for key in animals.keys():
    print(key,"->",animals[key])
print(animals.values())
for value in animals.values():
    print(value)
animals["cat"]="Katzen"
animals["Swan"]="Schwam"
del animals["Swan"]
animals.popitem()
soldiers={
    "Hassan":"Leader",
    "Abdullah":"Commander",
    "Omar":"Corporal",
}
soldiers["Hassan"]="Great Leader"
soldiers["Amir"]="Soldier"
del soldiers["Abdullah"]
print(soldiers)
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:10,6:60}
dict4={}
for d in (dict1,dict2,dict3):
    dict4.update(d)
print(dict4)
students={}
while True:
    name=input("Írd be a neved:")
    if name == "":
        break
    score = int(input("Pontoszámot kérek:"))
    if name not in students:
        students[name]=(score,)
    else:
        students[name]+=(score,)
for name in students.keys():
    add=0
    counter=0
    for score in students[name]:
        add+=score
        counter+=1
    print(name, ":",add/counter)
