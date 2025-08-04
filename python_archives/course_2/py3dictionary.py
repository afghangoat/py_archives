dictionary={'data1':1,'data2':2,'data3':3,'data4':4,'data5':5}
result=1
result3=1
result4=1
result2=1
for value in dictionary.values():
    result=result*value
for key in dictionary.keys():
    result2 = result2*dictionary[key]
for key,value in dictionary.items():
    result3 = result3*value
for key in dictionary:
    result4 = result4*dictionary[key]

print("max érték:", max(dictionary.values()),"min érték:",min(dictionary.values()))
#task2
d={'1':["a","b"],'2':["c","d"]}
a,b=d.values()
for i in a:
    for j in b:
        print(i+j)
test_results={'Fizika':80,'Matematika':90,'Kémia':86}
keys=list[test_results]
del test_results['Matematika']
test_results['Algebra']=65
people={}
#while True:
#    person=input("Mi a neve:")
#    if person == "":
#        break
#    else:
#        person_list=[]
#        age=int(input("milyen idős:"))
#        gender=input("Neme:")
#        job=input("foglakozás:")
#for person in people.keys():
#    print(person,"->",people(person))
dictionary={'a':1,'b':2,'c':3,'d':4,'e':5}
for key in dictionary.keys():
    print(key,"->",dictionary[key])
for key,value in dictionary.items():
    print(dictionary[key],"->",value)
dictionary={3:1,54:2,43:3,43:4,34:5}
for key in dictionary.values():
    if dictionary[key] % 2 ==0:
     print(key,"->",dictionary[key])
dictionary={}
for i in range(1,11):
    dictionary[i] = i*i
print(dictionary)
