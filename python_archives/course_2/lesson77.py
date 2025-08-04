print(6|14)
print(6^14)
print(~14)
print(14>>2)
def aritmetictobitwise(n):
    n<<=1
    print(n)
    n<<=3



aritmetictobitwise(2)
def comparsion(n):
    if n % 2 ==0:
        print("yes")
    if n & 1 == 0:
        print("yes")