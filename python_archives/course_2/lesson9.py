def openFile():
    f=open("pythontxt.txt","r",encoding="utf-8")
    print(f.read())
    f.close()
#openFile()

def openFileChars():
    f = open("pythontxt.txt", "r", encoding="utf-8")
    print(f.read(6))
    f.seek(0)
    print(f.read(6))
    f.close()


#openFileChars()
def ketszazlineserikdontdoitagain():
    f = open("pythontxt.txt", "r", encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        print(line,end="")
    f.close

def ketszazlineserikdontdoitagain2():
    f = open("pythontxt.txt", "r", encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        print(line[2:4],end="")
    f.close

#ketszazlineserikdontdoitagain2()
def wizard_harry():
    with open("pythontxt.txt") as f:
        if "Harry" in f.read():
            print("van")
        else:
            print("nincs")
    f.close()
wizard_harry()

#cfile("mywritefile")

def cfile(filename):
    f=open(filename+".txt","w+")
    for i in range(1,11):
        f.write(str(i))
        f.write(" ")
    f.seek(0)
    print(f.read())
    f.close()

#cfile("test")
#appenfile
def appendfile():
    f=open("test.txt","a+")
    f.write("\nnewline")
    f.seek(0)
    print(f.read())
    f.close()
appendfile()
