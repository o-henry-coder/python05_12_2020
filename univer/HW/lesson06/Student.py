class Student:

    def __init__(self, name, id, fac, course, group, mark, phone, addr, birth, stud_list = []):
        self.stud_list = stud_list
        self.group = group
        self.course = course
        self.fac = fac
        self.mark = mark
        self.phone = phone
        self.addr = addr
        self.birth = birth
        self.id = id
        self.name = name

    def add(self, students):
        self.stud_list.append(students)

    def get_ling_fac(self):
        ling_fac_list = []
        for fac in self.stud_list:
            if fac[2] == 'linguistics':
                ling_fac_list.append(fac[0])
        return ling_fac_list
    def get_math_fac(self):
        ling_math_list = []
        for fac in self.stud_list :
            if fac[2] == 'mathematics':
                ling_math_list.append(fac[0])
        return ling_math_list
    def get_1st_year_stud(self):
        st_year_list = []
        for course in self.stud_list:
            if course[3] == '1st':
                st_year_list.append(course[0])
        return st_year_list
    def get_2nd_year_stud(self):
        nd_year_list = []
        for course in self.stud_list:
            if course[3] == '2nd':
                nd_year_list.append(course[0])
        return nd_year_list
    def get_3rd_year_stud(self):
        rd_year_list = []
        for course in self.stud_list:
            if course[3] == '3rd':
                rd_year_list.append(course[0])
        return rd_year_list
    def get_stud_birth(self):
        birth_list = []
        for birth in self.stud_list:
            if birth[8] > 1993:
                birth_list.append(birth[0])
        return birth_list

    def get_avg_mark(self):
        choice = str(input('enter group'))
        mark_list = []
        stud_group_list = []
        for mark in self.stud_list:
            if mark[4] == choice:
                mark_list.append(mark[5])
                sum = 0
                for i in mark_list:
                    sum += i
                    avg = sum / len(mark_list)
                    if avg >= 4:
                        stud_group_list.append(mark[0])
        return stud_group_list

    def save_students(self):
        with open("students.txt", "w") as file_write:
            file_write.write(str(self.stud_list))

    def __str__(self):
        return f"{self.name}, {self.id}, {self.fac},{self.course}, {self.group}, {self.mark}, {self.phone},\
{self.addr}, {self.birth}, {self.stud_list}"

stud_list = Student('Becky Sharp', 768, 'linguistics', '3rd', '313c', 5, 586879527, 'NY', 1994)
stud1 = 'Bob Jones', 213, 'linguistics', '3rd', '313c', 4, 586849527, 'NY', 1993
stud2 = 'Tom Robbins', 755, 'mathematics', '2nd', '212c', 4, 768876687, 'NY', 1995
stud3 = 'John Simmons', 821, 'linguistics', '2nd', '213c', 3, 676853907, 'NY', 1995
stud4 = 'Bill Spears', 678, 'mathematics', '1st', '112c', 5, 667575439, 'NY', 1996
stud5 = 'Kolin Krivi', 557, 'mathematics', '2nd', '212c', 4, 784394868, 'NY', 1995
stud6 = 'Felicity Jones', 344, 'mathematics', '2nd', '212c', 5, 685495043, 'NY', 1994

# print(stud_list)
# print(stud_list.get_group())

students = [stud1, stud2, stud3, stud4, stud5, stud6]
for student in students:
    stud_list.add(student)
print(stud_list)
print('the students of linguistics faculty')
print(stud_list.get_ling_fac())
print('the students of mathematics faculty')
print(stud_list.get_math_fac())
print('the students of the 1st course')
print(stud_list.get_1st_year_stud())
print('the students of the 2nd course')
print(stud_list.get_2nd_year_stud())
print('the students of the 3rd course')
print(stud_list.get_3rd_year_stud())
print('the students that were born after 1993')
print(stud_list.get_stud_birth())
print(stud_list.get_avg_mark())
stud_list.save_students()


