class Person:
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname
    def getName(self):
        return self.name

class Teacher(Person):
    def __init__(self,name, surname, salary):
        super().__init__( name, surname)
        self.salary = salary
    def getSalary(self):
        return self.salary
    def setSalary(self, salary):
        self.salary = salary
    def toString(self):
        return print(f'{self.name} {self.surname} has salary: {self.salary}')

p = Person("Amina","Mamyrbekova")
p2 = Teacher("Yaslan", "Ruchanov", 5000000)
p2.setSalary(10000000)
# print(p2.getName())
p2.toString()
