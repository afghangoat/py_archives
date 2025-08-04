#Task 1
#float() változó
firstname="robi" #string
lastname="logi"
age = 7 #integer
job = "junior programmer"
country= "hungary"
isMarried= False
weight= 55.5
print(firstname)
print(age)
print(isMarried)
age=8
firstname="sanyi"
print(firstname)
print(age)
print(isMarried)
#Task 2
name=input("Mi a neved?:")
print("szia " + name + " !")
print("szia " , name , " !")
#Task 3
print(type(3))
print(type(True))
print(type(job))
print(type(50.5))
#Task 4
#int-->float
print(age)
print(float(age))
#int-->string
print(age)
print(str(age))
#print(job)
#print(int(job))
help("keywords")
#task 5
name1= "lakatos"
name2="sanyi"
age=7
print("Szia",name1,name2,"vagyok és",age,"éves!")
num1=float(input("1.szám?:"))
num2=float(input("2.szám?:"))
num3=float(num1+num2)
print(num1,"+",num2,"=",num3)
num3=float(num1-num2)
print(num1,"-",num2,"=",num3)
num3=float(num1/num2)
print(num1,"/",num2,"=",num3)
num3=float(num1*num2)
print(num1,"*",num2,"=",num3)
weirdthing="/\ "
print(weirdthing+weirdthing+weirdthing+weirdthing+weirdthing)
r=float(input("Enter a radius:"))
rk=float(r*2*3.14)
rT=float(r*r*3.14)
print(rk,rT)
igemult1=input("ige (T/1):")
igemult2=input("Múlt idejű ige (cselekvés)(T/1):")
igemult3=input("ige:")
igemult4=input("ige (E/1):")
targy1=input("Egy tárgy:")
targy3=input("Egy tárgy:")
targy2=input("Egy tárgy:")
epulet=input("Épület:")
szemely=input("Keresztnév:")
szemely2=input("Még egy keresztnév:")
print(f"""Ez vagyok én, {szemely}. Éppen {igemult2} a {targy1}emben és kitaláltam, hogy milyen jó ötlet lenne venni
egy {targy2}ot a(z) {epulet}ben. De közben elfelejtettem, hogy még nem fejeztem be a {targy3}-am elkészítését ezért
elkezdtem {igemult1}ezni. Eközben átjött {szemely2} és elkezdtett {igemult3}ni. Én erre elkzedtem {igemult4}ezni és
vége lett a napnak de nem vettem semmit.""")
