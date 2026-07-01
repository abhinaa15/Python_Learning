'''
class students:
    institute="OneTeam"

    def get_details(self,n,p):
        self.name=n
        self.place=p

stud1=students()
stud2=students()

stud1.get_details("Abhina","Kollam")
stud2.get_details("Nandhu","Kochi")

print(stud1.name)
print(stud2.name)
'''

'''
class students:
    institute="OneTeam"

    def get_details(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"Hello {self.name} you are from {self.place}")

stud1=students()
stud2=students()

stud1.get_details("Abhina","Kollam")
stud2.get_details("Nandhu","Kochi")

stud1.display()
stud2.display()
'''
'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
s1=student("Abhina",20)
s1.display() 
'''

class students:
    institute="OneTeam"

    def __init__(self,n,p):
        self.name=n 
        self.place=p
    def display(self):
        print(f"Hello {self.name} you are from {self.place}")

class pythonstudents(students):
    def __init__(self,c,n,p):
        self.cource=c
        super().__init__(n,p)

pstd1=pythonstudents("python fullstack","Abhina","kollam")
pstd1.display()


