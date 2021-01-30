class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self) :
        return self.__age

    @age.setter
    def age(self, value) :
        if 0 < value < 100 :
            self.__age = value
        else :
            self.__age = None

    def __str__(self):
        return f"{self.name}, {self.age}"

class Student(Human):
    def __init__(self, name, age, id_group):
        Human.__init__(self, name, age)
        self.id_group = id_group

    @property
    def id_group(self):
        return self.__id_group

    @id_group.setter
    def id_group(self, value):
        if value in range(1, 10):
            self.__id_group = value
        else:
            self.__id_group = None

    def study(self):
        print('studying')

    def __str__(self):
        return f"{self.name}, {self.age}, {self.id_group}"


class Doctor:
    def __init__(self, name, age, id_licence):
        Human.__init__(self, name, age)
        self.id_licence = id_licence

    def cure(self):
        print('curing')

    @property
    def age(self) :
        return self.__age

    @age.setter
    def age(self, value) :
        if 0 < value < 100 :
            self.__age = value
        else :
            self.__age = None

    @property
    def id_licence(self) :
        return self.__id_licence

    @id_licence.setter
    def id_licence(self, value) :
        if value in range(100000, 1000000000) :
            self.__id_licence = value
        else :
            self.__id_licence = None

    def __str__(self):
        return f"{self.name}, {self.age}, {self.id_licence}"

class Vet(Doctor):
    pass

class Fighter(Human):
    def __init__(self, name, age, power, defense):
        Human.__init__(self, name, age)
        self.power = power
        self.defense = defense
        
    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, value):
        if 0 < value <100:
            self.__power = value
        else:
            self.__power = 0    
    
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, value):
        if value in range(0,1000):
            self.__defense = value
        else:
            self.__defense = 0

    def fight(self, other_fighter):
        if self.defense - other_fighter.power > 0:
            print('we are winner')
        else:
            print('we are loser')

    def __str__(self):
        return f"{Human.__str__(self)}, {self.power}, {self.defense}"

class FighterDoc(Fighter, Doctor):
    pass
