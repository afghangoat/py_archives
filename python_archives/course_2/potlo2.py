def write():
    f = open("file.txt","w+",encoding="utf-8")
    print("Ide mit kéne rakni?",file=f)
    f.seek(0)
    f.close()

#write()

def append():
    f=open("file.txt","a+",encoding="utf-8")
    print("Ide mit kéne rakni?", file=f)
    f.seek(0)
    for line in f.readlines():
        print(line)
    f.close()

#append()

def append3(h):
    f=open("file.txt","a+",encoding="utf-8")
    for line in f.readlines():
        if line == h:
            line = ""
    print(f.read())
    f.close()


#append2("e")
def cooklist():
    list1 = ["Bread\n","Milk\n","Cheese\n","Apple\n"]
    f=open("file.txt","w+",encoding="utf-8")
    f.writelines(list1)
    f.seek(0)
    print(f.read())

def files():
    names = open("file.txt","r",encoding="utf-8")
    pairs= {}
