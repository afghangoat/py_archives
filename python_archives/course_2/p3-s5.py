print("\n\n\n\n\n\n\n\n\n\n\n")
def ret2chars(msg):
    if (len(msg) < 2):
        return 0
    else:
        return msg[0]+msg[1]+msg[-1]+msg[-2]

#print(ret2chars("Alma"))

def rep2chars(msg):
    h = msg[0]
    return msg.replace(h, "$")

#print(rep2chars("alllal"))

def ismetchars(msg):
    h = False
    logger = 0
    for i in range(0,len(msg)):
        if msg[i] == msg[i-1]:
            h = True
            logger = i
    print("A",logger,"-edik karakter az.")
    return h

#print(ismetchars("Allah"))

def listmatrix(matrix):
    mml = []
    for l in matrix:
        for ll in l:
            mml.append(ll)
    return mml

#print(listmatrix([[1,2,3],[1,2,3]]))












def tupdel(tup,what):
    lup = list(tup)
    lup.remove(what)
    return tuple(lup)

#print(tupdel((1,2,3,4,5),3))











def dictsort(d,n):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=n))

print(dictsort({6: 2, 3: 4, 4: 8, 2: 1, 9: 0},True))












lstidkwhich = [1,2,3,4,5,5,1,413,44,5,3,41,1,3]

def listiterate(lst):
    return "wut"
