import csv
import pandas as pd
pd.set_option('display.width',320)
pd.set_option('display.max_columns',320)
def openCSV():
    csvfile=open("oscar_age_female.csv",newline="")
    data=csv.reader(csvfile,delimiter=" ")
    for row in data:
        print(' '.join(row))
#openCSV()
def openwithpandas():
    csvfile=pd.read_csv("oscar_age_female.csv")
    print(csvfile.head(90))
def opencolumns():
    csvfile=pd.read_csv("oscar_age_female.csv",usecols=["Age","Name"])
    print(csvfile.head(10))
    summ=csvfile["Age"].sum()
    rows=len(csvfile["Age"])
    summ=round(summ/rows,2)
    print(summ)
def oldestwinners():
    csvfile=pd.read_csv("oscar_age_female.csv",usecols=["Age","Name"])
    max_age=max(csvfile["Age"])
    myrow=csvfile[csvfile["Age"]==max_age]
    print("Legidősebb:"+str(myrow.iloc[0,1]))
#oldestwinners()
def dataRow(row):
    csvfile = pd.read_csv("oscar_age_female.csv")
    myrow=csvfile.iloc[row]
    print(myrow)
#dataRow(5)
def fargo():
    csvfile=pd.read_csv("oscar_age_female.csv",usecols=["Year","Name"],skipinitialspace=True)
    mm = 0
    for i in csvfile["Age"]:
        if i == "Fargo":
            mm = csvfile["Age"].iloc(i)
    print(mm)
def vowelfreq():
    csvfile = pd.read_csv("oscar_age_female.csv",skipinitialspace=True)
    vowels=["A","E","I","U","O","a","e","i","u","o"]
    vowel=0
    for index,row in csvfile.iterrows():
        if row["Letter"] in vowels:
            vowel+=row["Percentage"]
    print(vowel)
vowelfreq()
