

try:
    number = int(input("Enter a number: "))
    print(1/ number)

except ZeroDivisionError:
    print("You cant devide by zero. Idiot")
except ValueError:
    print("Enter only number digits please")
except Exception:                                           #used to catch all possible exceptions. its however too broad, hence its consider a bad practice.
    print("kindly enter a valid digit greater than 0")
finally:                                                    #it always execute. used to go cleanups
    print("do some clean up please")