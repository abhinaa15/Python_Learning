'''
def add(*args):
    total=0
    for i in args:
        total+=i
        print(total)

add(34,12)
add(9,12,46)
'''
'''
def greet(**kwargs):
    print(f"Hello {kwargs["name"]} you are {kwargs["age"]}years old")

greet(name="Aswin",age=24,place='Kottayam')
'''

'''
def add(*args):
    total=0
    for i in args:
        total+=i
    return total
add(34,12)
'''
'''
def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print("Factorial of 5 is : ",fact(5))
'''


def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print("factorial of 3 is : ",fact(3))






