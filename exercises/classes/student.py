class Student:

    def __init__(self):
        print("helelo")

    def describe_student(self):
        for attribute, value in self.__dict__.items():
                print(f"{attribute}: {value}")

    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def cohort_number(self):
        try:
            return self.__cohort_number # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}" # Note there are 2 underscores here
        except AttributeError:
            return 0

    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if isinstance(new_first_name, str):
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string')

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str):
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string')

    @age.setter # The setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer')

    @cohort_number.setter # The setter
    def cohort_number(self, cohort_number):
        if isinstance(cohort_number, int):
            self.__cohort_number = cohort_number
        else:
            raise TypeError('Please provide an integer')


mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39
print(mike.full_name)