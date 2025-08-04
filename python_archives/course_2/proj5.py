import random
# jövedelem <8360 arany = jöv*0.18-560
# jöv > 85430 = (14900+(jöv-85430))*0.27
incomes = [
[10000, 100000, 65489, 223344, 987654],
[84536, 987631, 758569, 98536, 436656],
[64538, 525329, 966494, 421412, 98655],
[865947, 924456, 214532, 126975, 5456],
]
def taxcalculator(income):
    if income <= 85430:
        tax = income * 0.18 - 560
        if tax < 0:
            zax=0
    else:
        tax = (14900+(income-85430))*0.27
    return round(tax,0)
print(taxcalculator(42077))
taxes=[]
for money in incomes:
    for per_person in money:
        tax=taxcalculator(per_person)
        taxes.append(tax)
for i in range(len(taxes)):
    print("A fizetendő adó:",i+1,":",taxes[i])
#Task2 List comprehension
def listcomprehension():
    list1=[]
    #hagyományos
    for i in range(4,76):
        list1.append(i)

    list2=[x for x in range(4,76) if x%2==0]
    print(list2)

listcomprehension()
#Task3
def matrixcomprehension():
    #0...9
    matrix = [[i for i in range(10)] for j in range(10)]
    print(matrix)
    matrix2 = [[random.randrange(5, 11) for i in range(10)] for j in range(10)]
    print(matrix2)
    matrix3 = [[j for i in range(10)] for j in range(10)]
    print(matrix3)
    matrix4 = [[i^4+j for i in range(10)] for j in range(3)]
    print(matrix4)
matrixcomprehension()
#Task4
def cubes():
    cube1=[]
    for building in range(3):
        list2=[]
        for floor in range(3):
            list1=[]
            for room in range(3):
                list1.append(random.randint(0,1))
            list2.append(list1)
        cube1.append(list2)
    print(cube1)
    cube2 = [[[random.randint(0,1) for a in range(3)] for i in range(3)] for j in range(3)]
    print(cube2)
    print(cube2[2][1][3])
cubes()