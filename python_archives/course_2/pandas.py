import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

def read_data():
    lib=pd.read_csv("library2.csv")
    print(lib["Identifier"].is_unique)
    lib.drop(["Edition Statement"],axis=1)
    print(lib.head(5))
#read_data()
def adata(index):
    lib = pd.read_csv("library2.csv")
    print(lib["Identifier"].is_unique)
    lib = lib.set_index("Identifier")
    print(lib.loc(index))
#adata(3)
def colclear():
    lib = pd.read_csv("library2.csv")
    lib = lib.set_index("Identifier")
    print(lib.loc[1982:,"Date of Publication"].head(20))
    extr=lib["Date of Publication"].str.extract(r'^(\d{4})',expand=False)
    lib["Date of Publication"]=pd.to_numeric(extr)
#colclear()
def colclear2():
    lib = pd.read_csv("library2.csv")
    lib = lib.set_index("Identifier")
    print(lib.loc[1982:, "Place of Publication"].head(10))