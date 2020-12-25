class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht_inches: int  = None):
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_year_of_birth(self):
        return self.__date_of_birth

    def get_summary(self):
        return f"Name: {self.__name} DOB:{self.__date_of_birth} Height:{self.__height if self.__height is not None else 'Invalid'}"
class Patient(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, patient_id: int):
        super().__init__(person_name,year_of_birth)
        self.email = email_id
        self.id = patient_id
    def get_summary(self):
        return f"Name: {self.get_name()}, Patient Email:{str(self.email)}, Patient ID:{self.get_year_of_birth()}"
    def __str__(self):
        return f"Name: {self.get_name()}, Patient Email:{str(self.email)}, Patient ID:{self.get_year_of_birth()}"
patient = Patient("Danial",1976, "sdffsf@yahoo.com", "ID:105")
print(patient)
patient = Patient("Petric", 1990, "fdsfw@gmail.com", "ID:209")
print(patient)



class Doctor(Person):
    def __init__(self, patient_name: str, year_of_birth: int, department: str):
        super().__init__(patient_name,year_of_birth);
        self.dept = department
    def get_summary(self):
        return f"{self.get_name()} is a Doctor"
new_hospital_list = [Person("Hade",1990),
                    Patient("Singe",2000,"fdfs@gmail.com","ER304"),
                    Doctor("Robert",1980,"DE")]

for doct in new_hospital_list:
    print(doct.get_summary())
