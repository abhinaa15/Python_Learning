'''
try:
    a,b=12,0
    print(a/b)
except:
    print("you cannot divide by zero")
print("program executed") 
'''

try:
    a,b=12,3
    print(a/b)
except ZeroDivisionError:
    print("you cannot divided by zero")
except TypeError:
    print("can divided only by integer")
except NameError:
    print("please provide values for a and b")
except Exception as e:
    print("error occured,e")
else:
    print("program is executed without error")
finally:
    print("program executed")