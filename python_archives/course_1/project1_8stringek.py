names=["A","B","C"]
print(names)
print(*names) # csak a lista értékét írja ki
print(*names,sep=",")
#for
for i in range(10):
    print(i)

for i in range(1,11):# 1-10-íg írja ki
    print(i)

for i in range(2,101,2):# 1-100-ig csak páros számok (kettesével lépve)
    print(i)

for i in names:#names lista elemeit írja ki.
    print(i)

for i in "Hello World!":
    print(i)

num=int(input("A szám szorzótáblája:"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")

encrypted_message="Wyh earne  eclaenp hIa nbtu?" #van ilyen is: Mdy,  nJaammee si sB oBnodn.
decrypted_message=""
for i in range(len(encrypted_message)):
    if i % 2==0:
        decrypted_message+=encrypted_message[i]
for i in range(len(encrypted_message)):
    if i % 2!=0:
        decrypted_message+=encrypted_message[i]
print(encrypted_message)
print(decrypted_message)

new_decrypted_message="My name is Bond, James Bond."
first_half=new_decrypted_message[:len(new_decrypted_message)//2]# a //-el a felét vesszük (az első felét)
second_half=new_decrypted_message[len(new_decrypted_message)//2:]
print(first_half)
print(second_half)

new_decrypted_message=""
for i in range(len(new_decrypted_message)//2):
    new_decrypted_message+=first_half[i]
    new_decrypted_message+=second_half[i]
print(new_decrypted_message)

list1=[]
for i in range(1,51):
    list1+=[i]
print(*list1)
list2=[]

for i in range(20,-8,-1):
    list2+=[i]
print(*list2)
#hf: lista nevekkel,adjunk meg egy nevet és nézzük meg , hogy az adott név szerepel-e a listában