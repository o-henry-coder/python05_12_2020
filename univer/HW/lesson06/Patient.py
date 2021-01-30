class Patient:
    def __init__(self, id, full_name, address, phone, medical_id, diagnosis, patient_list = []):
        self.id = id
        self.full_name = full_name
        self.address = address
        self.phone = phone
        self.medical_id = medical_id
        self.diagnosis = diagnosis
        self.patient_list = patient_list

    def add_patients(self, patients):
        self.patient_list.append(patients)

    def get_diabetes_patients(self):
        diabetes_list = []
        for diagnosis in self.patient_list:
            if diagnosis[5] == 'diabetes':
                diabetes_list.append(diagnosis[1])
        return diabetes_list

    def get_pneumonia_patients(self):
        pneumonia_list = []
        for diagnosis in self.patient_list:
            if diagnosis[5] == 'pneumonia':
                pneumonia_list.append(diagnosis[1])
        return pneumonia_list

    def get_flu_patients(self):
        flu_list = []
        for diagnosis in self.patient_list:
            if diagnosis[5] == 'flu':
                flu_list.append(diagnosis[1])
        return flu_list

    def pat_with_medical_id(self):
        medical_list = []
        for card in self.patient_list:
            if card[4] in range(200, 500):
                medical_list.append(card[1])
        return medical_list

    def save_patients(self):
        with open("patients.txt", "w") as file_write:
            file_write.write(str(self.patient_list))

    def __str__(self) :
            return f"{self.id}, {self.full_name}, {self.address},{self.phone}, {self.medical_id},\
{self.diagnosis}, {self.patient_list}"

patient_list = Patient(65, 'Kulikova Maria Petrovna', 'Kharkiv', 868778758, 145, 'diabetes')
pt1 = 65, 'Kulikova Maria Petrovna', 'Kharkiv', 868778758, 676, 'diabetes'
pt2 = 98, 'Petrova Victoria Nickolaevna', 'Kyiv', 868778758, 432, 'pneumonia'
pt3 = 45, 'Sidorov Michail Vasilievich', 'Lviv', 868778758, 878, 'diabetes'
pt4 = 35, 'Gribova Natalia Valerievna', 'Vinnitsa', 868778758, 123, 'flu'
pt5 = 90, 'Ovchinnikov Taras Petrovich', 'Kharkiv', 868778758, 668, 'flu'
pt6 = 34, 'Avdeenko Maxim Victorovich', 'Lviv', 868778758, 234, 'pneumonia'
pt7 = 67, 'Herzhan Tetyana Nickolaevna', 'Lviv', 868778758, 767, 'flu'

patients = [pt1, pt2, pt3, pt4, pt5, pt6, pt7]
for patient in patients:
    patient_list.add_patients(patient)

print('patients with diabetes')
print(patient_list.get_diabetes_patients())

print('patients with pneumonia')
print(patient_list.get_pneumonia_patients())

print('patients with flu')
print(patient_list.get_flu_patients())

print('the patients which medical_id cards in interval betrween 200 and 500')
print(patient_list.pat_with_medical_id())

patient_list.save_patients()
