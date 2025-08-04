#ciklus
number=1
sum=0
#while 1:
#    print(number)
#    number+=1
#while number<=10:
#    print(number)
#    sum += number
#    number+=1
#print(sum)
count=0
num=567523742
while num!=0:
    num//=10
    count+=1
print(count)
#számkitaláló
num=42
guessnum=int(input("Hány számot szertnél?"))
guess=0
while guessnum!=0 and guess!=num:
    guess=int(input("Tippelj:"))
    if guess>num :
        print("kisebb")
    elif guess<num:
        print("nagyobb")
    guessnum-=1
if guess==num:
    print("remek, jól tippeltél.")
else:
    print("Hát... béna voltál... :/")
count=int(input("hanyadik-ig írja ki a fibonacci számokat?:"))
num1=0
num2=1
num4=0
num5=0
num6=0
print("Fibonacci Sorozat:")
while count!=0:
    num4+=num1
    if num5%2!=0:
        num5+=num1
    else:
        num6+=num1
    print(str(num1))
    temp=num1+num2
    num1=num2
    num2=temp
    count-=1
#hf1
print("össz:",num4,"páros:",num6,"páratlan:",num5)
#hf2
#írasd ki 1-100-ig a prímszámokat
number=2
primeNumber=0
i=1
while number<=100:
    i=1
    primeNumber=0
    while i<=number:
        if number%i==0:
            primeNumber+=1
        i+=1
    if primeNumber==2:
        print(number)
    number+=1
