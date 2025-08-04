print("Welcome","to","Logischool",sep=", ",end="\n-------------\n")
print("You are welcomed here!")

iinteg1 = 1
stringer = "32"
bobool = True
print(iinteg1,stringer,bobool)
print(int(iinteg1),str(stringer),bool(bobool))

var1 = 1267
print(bin(var1))
print(oct(var1))
print(hex(var1))
expint = 1e6
print(expint)
print("'Learning at Logischool was the decission of my life' - said the wise old man")

var1=input("Szám1:")
var2=input("Szám2:")
try:
    if var1 > var2:
        print("szám1 nagyobb")
    elif var2>var1:
        print("szám1 nagyobb")
    else:
        print("egyenlő")
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Error")
except TypeError:
    print("Error")
except ArithmeticError:
    print("Error")
except MemoryError:
    print("Not enough / no memory")
except ModuleNotFoundError:
    print("Error")
except RuntimeError:
    print("Process Error")
except TimeoutError:
    print("Timeout")
except ZeroDivisionError:
    print("Error")
except NameError:
    print("Error")
except SyntaxError:
    print("Error")
except RecursionError:
    print("Error")
except ReferenceError:
    print("Error")
except:
    print("Error")