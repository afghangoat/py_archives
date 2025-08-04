
#def recursive_centaur():
#    print("Recursive centaur: half a horse, half a ", end='')
#    recursive_centaur()
#recursive_centaur()
def counter(num):
    print(num)
    if num > 0:
        counter(num-1)
intnum1 = 0
num2 = 0
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
def fib(i,n):
    if i !=0:
        return n + fib(i-1,n+1)
    else:
        return n
print(fib(5,1))
list [1,2,3,4,51,1,4,63,1,5,6]
def sum(list):
    if len(list) == 1:
        return list[0]
    return list[0] + sum(list[1:])
#print(sum(range(1-12)))








ii = 0
def hatvany(i,j):
    if j != 1:
        return i * hatvany(i,j-1)
print(hatvany(10,5))
#[19:00] Logiscool Zugló Teams 4
#   Írjatok egy rekurzív függvényt ami két paraméterben megadott szám legnagyobb közös osztóját (LNKO) adja vissza!

