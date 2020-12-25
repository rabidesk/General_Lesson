# class Person:
#     def __init__(self, person_name: str, year_of_birth: int, ht_inches: int  = None):
#         self.__name = person_name
#         self.__date_of_birth = year_of_birth
#         self.__height = ht_inches
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def get_year_of_birth(self):
#         return self.__date_of_birth
#
#     def get_height(self):
#         return self.__height
#
#     def get_summary(self):  # get summary for exection
#         # pass
#         return f"Name: {self.__name} DOB:{self.__date_of_birth} Height:{self.__height if self.__height is not None else 'Invalid'}"
# class Patient(Person):
#     def __init__(self, person_name: str, year_of_birth: int, email_id: str, patient_id: int, patient_height: int):
#         super().__init__(person_name,year_of_birth)
#         self.email = email_id
#         self.id = patient_id
#         self.height = patient_height
#     def get_summary(self):
#         return f"Name: {self.get_name()}, Patient Email:{str(self.email)}, Year of Birth:{self.get_year_of_birth()}, Height:{self.height}"
#     def __str__(self):
#         return f"Name: {self.get_name()}, Patient Email:{str(self.email)}, Year of Birth:{self.get_year_of_birth()}, Height:{self.height}"
# patient = Patient("Danial",1976, "sdffsf@yahoo.com", "ID:105", 44)
# print(patient)
# patient = Patient("Petric", 1990, "fdsfw@gmail.com", "ID:209", 53)
# print(patient)
#
# class Doctor(Person):
#     def __init__(self,Doctor_name: int, year_of_birth: int, Department: str):
#         super().__init__(Doctor_name, year_of_birth)
#         self.dept= Department
#
#     def get_summary(self):
#         return f"Doctor Name:{self.get_name()}, Doctor DOB:{self.get_year_of_birth()}, Doctor Rank:{self.dept}"
#
# new_hostpital_list = [Person("Hadi",1990),
#                       Patient("Singe", 1999, "fdsf@gmail.com",12, 55),
#                       Doctor("Robert", 1979, "Dental")]
#
# for doct in new_hostpital_list:
#     print(doct.get_summary())
#
class NormalClass:
    pass
abc= NormalClass()
abc.age=50
abc.name = "Mark"
print(abc.age)
print(abc.name)

