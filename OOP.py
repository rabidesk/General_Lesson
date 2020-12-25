class Person:
    def __init__(self, person_name:str, year_of_birth:int, ht_inches: int =None ):
        self.__name  = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches

    def get_year_of_birth(self):
        return self.__date_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry, This student absent")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string
    def get_summary(self):
       # pass
       return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height:{self.__height if self.__height is not None else 'Invalid'}"

person_list =   [Person("Johne", 1980),
                Person("David", 1993,65),
                Person("Ssue", 2020, 80),
                Person("Ben", 1945),
                Person("Karlos", 1900, 72)]

class Student(Person):
    def __init__(self, person_name:str, year_of_birth:int, email_id: str, student_id:str):
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"

# __str__ and __repr__ both can be used for overwright.
    def __str__(self):  # Program need to know how to convert string bkz many datatype is there.
        return self.get_summary()   # (Also can be used for return as it's used for same statement)
       #return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"

    def __repr__(self):  # Overwrite representing and return the same
        #return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"
        return self.get_summary()   # (Also can be used for return as it's used for same statement)

student = Student("Studnt Name", 2000, "email.yahoo.com", "G:12456325")
print(student)
student.set_name("Rabiul")
print(student)

class Teacher(Person):
    def __init__(self,person_name:str, year_of_birth: int, department: str):
        super().__init__(person_name, year_of_birth)
        self.dept = department
    def get_summary(self):
        return f"{self.get_name()} is a teacher"

new_person_list = [
    Person("Ronaldo",986),
    Student("Messy", 2000, "mail.yahoo.com", "stid"),
    Teacher("Dunga", 1980, "Tid")
]
# To eterate above list we can do for loop
for p in new_person_list:
    print(p.get_summary())

class PlainClass:
    pass
abc = PlainClass()
abc.age = 20
abc.name = "Movie"

print(abc.age)