import random
def creatematrix():
    matrix_1 = [
         [0,1,2],
         [3,4,5],
         [6,7,8],
         [9,10,11],
         [12,13,14],
         [15,16,17]
                ]
    for i in range(len(matrix_1)):
        print(*matrix_1[i])
creatematrix()
def creatematrix2():
    matrix2 = []
    for i in range(5):
        temp_list=[]
        for j in range(4):
            temp_list.append(random.randrange(1,11))
        matrix2.append(temp_list)
    for i in range(len(matrix2)):
        print(*matrix2[i])
creatematrix2()
data = ["shirt number", "name", "age", "height", "weight"]
team = [[1, "Nora", 24, 176, 62],
[4, "Noemie", 25, 180, 67],
[13, "Emily", 22, 178, 60],
[42, "Lisa", 23, 179, 63],
[99, "Greta", 27, 176, 81]]
print("\n",*team[0][1],"\n",*team[1][1],"\n",*team[2][1],"\n",*team[3][1],"\n",*team[4][1])
def modifymatrix():
    matrix = [
        [1, True, 3, 'd', 5],
        [45.4, 2, 9, 'b', 6],
        [99, 22, 'a', 4, 'g'],
        [5, 12, 3, 'k', 'e'],
        [0, 21, 35, False, 56],
    ]
    print("Elötte: ")
    for i in range(len(matrix)):
        print(*matrix[i])
    row = -1
    while row < 0 or row > 4:
        row = int(input("Adj meg egy sor értéket:"))
    col = -1
    while col < 0 or col > 4:
        col = int(input("Adj meg egy col értéket:"))
    change_to= int(input("Mire változzon:"))
    change_type = str(input("Milyentipus:"))
    if change_type == "str":
        change_to = str(change_to)
    if change_type== "bool":
        change_to = bool(change_to)
    if change_type== "int":
        change_to = int(change_to)
    else:
        print("nem jó!")
    matrix[row][col]=change_to
    print(matrix)


modifymatrix()
def creatematrix5(k,n):
    matrix2 = []
    for i in range(k):
        temp_list=[]
        for j in range(n):
            temp_list.append(random.randrange(1,11))
        matrix2.append(temp_list)
    for i in range(len(matrix2)):
        print(*matrix2[i])
    for j in range(len(matrix2)-1):
        for i in range(len(matrix2) - 1):
            if matrix2[i] >= matrix2[i+1]:
                 tmp = matrix2[i+1]
                 matrix2[i+1] = matrix2[i]
                 matrix2[i] = tmp
    print(matrix2)

creatematrix5(6,4)