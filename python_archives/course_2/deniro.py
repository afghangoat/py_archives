import pandas as pd
import matplotlib.pyplot as plt
import csv

def opencsv():
    csvfile=open("deniro.csv")
    data=csv.reader(csvfile,skipinitialspace=True)
    for row in data:
        print(", ".join(row))
    csvfile.close()
#opencsv()
def opencsvpandas():
    pd.set_option("display.max_rows",None)
    csvfile = pd.read_csv("deniro.csv",skipinitialspace=True)
    print(csvfile)

opencsvpandas()