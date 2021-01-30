class Abiturient:
    def __init__(self, id, full_name, address, phone, marks = [], abit_list = []):
        self.id = id
        self.full_name = full_name
        self.address = address
        self.phone = phone
        self.marks = marks
        self.abit_list = abit_list
    def add(self, abiturients):
        self.abit_list.append(abiturients)

    def stud_with_f_marks(self):
        f_list = []
        for mark in self.abit_list:
            if 2 in mark[4]:
                f_list.append(mark[1])
        return f_list

    def save_abiturients(self):
        with open("abiturients.txt", "w") as file_write:
            file_write.write(str(self.abit_list))

    # def sum_marks(self):
    #     sum_list = []
    #     sum = 0
    #     for mark in self.abit_list:
    #         for i in mark[4]:
    #             sum +=i
    #             if sum > 14:
    #                 sum_list.append(mark[1])
    #                 sum_list.append(sum)
    #     return sum_list

    def __str__(self) :
            return f"{self.id}, {self.full_name}, {self.address},{self.phone}, {self.marks},\
    {self.abit_list}"

abit_list = Abiturient(65, 'Kulikova Maria Petrovna', 'Kharkiv', 868778758, [4,5,4,4])
ab1 = 65, 'Kulikova Maria Petrovna', 'Kharkiv', 868778758, [4,2,5,3]
ab2 = 98, 'Petrova Victoria Nickolaevna', 'Kyiv', 868778758, [3,5,5,5]
ab3 = 45, 'Sidorov Michail Vasilievich', 'Lviv', 868778758, [5,5,5,4]
ab4 = 35, 'Gribova Natalia Valerievna', 'Vinnitsa', 868778758, [3,2,4,4]
ab5 = 90, 'Ovchinnikov Taras Petrovich', 'Kharkiv', 868778758, [5,5,4,5]
ab6 = 34, 'Avdeenko Maxim Victorovich', 'Lviv', 868778758, [3,2,3,5]
ab7 = 67, 'Herzhan Tetyana Nickolaevna', 'Lviv', 868778758, [4,4,4,5]

abiturients = [ab1, ab2, ab3, ab4, ab5, ab6, ab7]
for abiturient in abiturients :
    abit_list.add(abiturient)
print(abiturients)
print(abit_list)

print('students that have got F marks')
print(abit_list.stud_with_f_marks())
abit_list.save_abiturients()

# print(abit_list.sum_marks())



