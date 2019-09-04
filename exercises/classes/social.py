import datetime
# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
class Patient():

    def __init__(self, soc="", date=datetime.date.today(), acc_num="0", first_name="", last_name="", address=""):
        self.soc = soc
        self.date = date
        self.acc_num = acc_num
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.full_name = f"{first_name} {last_name}"

    @property # The getter
    def first_name(self):
        try:
            return "" # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def last_name(self):
        try:
            return "" # Note there are 2 underscores here
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

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}."

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"