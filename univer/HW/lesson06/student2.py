class Student:

    def __init__(self, fac, course, group, stud_list = []):
        self.stud_list = stud_list
        self.group = group
        self.course = course
        self.fac = fac
        # self.mark = mark
        # self.phone = phone
        # self.addr = addr
        # self.birth = birth
        # self.id = id
        # self.name = name

    def add(self, students):
        self.stud_list.append(students)

    def __str__(self):
        return repr(self.stud_list)
    def get_group(self):
        for groups in self.stud_list:
            if groups[2] == '316d':
                print(groups[0])
    # def get_group(self):
    #     groups = self.stud_list[0]
    #         if groups == '316d':
    #             print(groups)

    # def __str__(self):
    #     return f"{self.id}, {self.name}, {self.birth}"

stud_list = Student('geology', '2nd', '212c')
stud2 = 'politology', '1st', '112b'
stud1 = 'psychology', '3rd', '316d'
stud_list.add(stud1)
stud_list.add(stud2)
stud3 = ('history', '3rd', '316d')
stud_list.add(stud3)

print(stud_list)
print(stud_list.get_group())

students = [stud1, stud2, stud3]
print(students)
    # old_human = humans[0]
for student in students:
        if student[2] == '316d':
            print(student[0])




    # fighters = []
    # for human in humans:
    #     if isinstance(human,Fighter):
    #         fighters.append(human)
    # print(fighters)
    #
    # for fight in fighters:
    #     print(fight)

