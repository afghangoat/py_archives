#list=[]
#for i in range(10):
#    j = int(input(print("NUMber")))
#    list.append(j)
#evens=[]
#odds=[]
#for i in range(len(list)):
#    if list[i]%2 == 0 :
#        evens.append(list[i])
#    else:
#        odds.append(list[i])
#print("odds:",odds,"evens:",evens)
#
nums = [1, 2, 3, 4, 5, 6, 5, 4, 5, 6, 1, 0, 1, 3]
nums2 = []
for i in nums:
    if i not in nums2:
        nums2.append(i)
print(nums2)

nnums2 = set(nums)
print(nnums2)
lista=[1,2,3,4,5]
lista2=["fkwkallti","dbsidbia","fwejfiwjef","ewifjw","grsg"]
szam=42
szoveg="Mr Krabs"
lista.extend(lista2)
print(lista)

mindenfele = ["Tunyacsáp", True, "", [], -2,0,123,False,420,None,"yikes"]
numbers = []
for i in range(len(mindenfele)):
    if type(mindenfele[i]) is int:
        numbers.append(i)
print(numbers)
#szakadek
random_numbers = [12, 33, 39, 83, 75, 28, 79, 52, 34, 57, 95, 40, 73, 13, 24, 26, 93, 68, 48, 45, 10, 87, 37, 20, 85, 99, 98, 92, 81, 43,  9, 31, 91, 67, 46, 66, 25, 76,  7, 61, 15, 63, 41, 71, 19, 22, 62, 35, 90, 97, 30, 78, 60,  2, 50,  1, 42, 94, 51, 96, 69, 77, 58, 47, 53, 54, 70,  3, 84, 14, 86, 56, 89,  8,  5, 38, 44, 18, 88, 23, 65, 74, 16, 82, 64, 100, 27, 59, 29, 72, 17, 55, 49, 21, 80, 11, 36, 6, 4, 32]
lk= min(random_numbers)
ln= max(random_numbers)
szakadek= abs(random_numbers.index(ln) - random_numbers.index(lk))
print(szakadek)