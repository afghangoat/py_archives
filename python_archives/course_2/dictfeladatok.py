mylist = [1,2,3,4,5,6,7,8,9,10]
def deloddlist(n):
    for i in range(len(n)):
        if i % 2 != 0:
            n.remove(i)
    return n

mylist=deloddlist(mylist)
print(mylist)










def printnums(n):
    for i in range(0,n+1):
        print(i)
    return n
printnums(100)