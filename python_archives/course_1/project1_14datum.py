todaydate='2021-04-01'#input("Today? (yyyy-mm-dd)")
birthdate='2005-01-01'#input("Birth? (yyyy-mm-dd)")
daysOfMonths=[31,28,31,30,31,30,31,31,30,31,30,31]
days=0
datenow=todaydate.split("-")
born=birthdate.split("-")
for i in range(len(datenow)):
    datenow[i]=int(datenow[i])
for i in range(len(born)):
    born[i]=int(born[i])

while (not(born[0]==datenow[0] and born[1]==datenow[1] and born[2]==datenow[2])):
    if born[1]==2 and ((born[0] % 4 ==0 and born[0] % 100 !=0) or born[0] % 400 ==0):
        if born[2] < daysOfMonths[born[1]-1]+1:
            born[2]+=1
        else:
            born[1]+=1
            born[2]=1
    else:
        if born[2] < daysOfMonths[born[1]-1]:
            born[2]+=1
        else:
            if born[1]==12:
                born[0]+=1
                born[1]=1
                born[2]=1
            else:
                born[1] +=1
                born[2] = 1
    days+=1
print(f"Te {days} napos vagy!")
##feladatok
word_1 = "Auuy"
word_2 = "iYma"
dza= False
word3=[]
for i in range(len(word_1)):
    word3.append(word_1[i])
    dza = False

if word_2[i] in word3:
    dza = True
print(dza,"True = Anagramma.")
burgers = ["Spicy Pinata", "Cheesy Dream", "Vegan Fluffy", "Fatty Boom", "Tortuga", "Pork Pie"]
list333=[]
votes = [95061, 93439, 98563, 90478, 90915, 97334]
bestvote=1
bestvote2=""
bestvote3=0
for i in range(len(burgers)):
    bestvote3 += int(votes[i])
    if bestvote < votes[i]:
        bestvote=votes[i]
        bestvote2=burgers[i]
    list333.append(str(burgers[i])+"-"+str(votes[i]))
print(len(burgers)," közül lehetett választani.")
for i in range(len(burgers)):
    print(list333[i])
print(bestvote2," Nyert! és ",bestvote3, " szavazott!")