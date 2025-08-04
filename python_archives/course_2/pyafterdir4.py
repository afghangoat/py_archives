












#def osztofuggveny(x,y):
try:
    x = 1
    y = z
    print(f"{x/y}")
except ValueError:
    print("Valami hülyeséget kaptam a bemeneten!")
except TypeError:
    print("Valami hülyeséget kaptam a bemeneten!")
except ZeroDivisionError:
    print("Valami másik hülyeséget kaptam a bemeneten!")
except MemoryError:
    print("!")
except NameError:
    print("?!")
except SyntaxError:
    print("!??")
except SyntaxError:
    print("!??")
except:
    print("0-day exploit!")















#osztofuggveny(0,1)
myList = [4, 8, "paper", 15, "code", 16, " ", 23, 42]
szum=0
count=0
for i in range(len(myList)):
    try:
        szum+=myList[i]
        count+=1
    except ValueError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except TypeError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except MemoryError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except MemoryError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except ModuleNotFoundError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except NameError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except SyntaxError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except ArithmeticError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except AttributeError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except UnicodeError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except IndexError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except LookupError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except InterruptedError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except NotImplementedError:
        print(f"a lista {i}-edik eleme {type(i)}")
    except:
        print(f"a lista {i}-edik eleme {type(i)}")
print(f"Szumma: {szum}, {count} darab számmal")