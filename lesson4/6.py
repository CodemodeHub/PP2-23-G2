class Person:
    def __init__(self, name, surname, weight):
        self.name = name
        self.surname = surname
        self.weight = weight
    def gravityForce(self):
        return self.weight * 9.8

class MoonStudent(Person):
    def __init__(self, name, surname, weight, s):
        super().__init__(name, surname, weight)
        self.s = s
    def gravityForce(self):
        # PREDPOLOZHIM CHTO NA LUNE 'g' V 3 raza menshe chem na zemle
        return super().gravityForce() / 3

    
p = Person("Yaslan","Ruchanov",75)
ms =  MoonStudent("Magzan", "Akhmadi", 80, "m1")
print(ms.name)
print(ms.gravityForce())