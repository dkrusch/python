import datetime

class Employee:

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def describe_employee(self):
        for attribute, value in self.__dict__.items():
                print(f"{attribute}: {value}")

class Company:

    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = []

    def add_employees(self, *employees):
        print(f"{employees}")
        for employee in employees:
            print(f"{employee}")
            self.employees.append(employee)

    def describe_company(self):
        print(f"{self.name} is in the {self.industry_type} industry and has the following employees:")
        for employee in self.employees:
            print(f"    * {employee.name}")

cool_company = Company("Cool Inc.", "Cool Street", "Coolers")
bad_company = Company("Bad Company", "Bad Street", "Batteries")
bob = Employee("Bob Bobob", "Cooler Maker", datetime.datetime.now())
mob = Employee("Mob Mobob", "Cooler Tester", datetime.datetime.now())
gog = Employee("Gog Magog", "Battery Maker", datetime.datetime.now())
cob = Employee("Cob Cobob", "Battery Tester", datetime.datetime.now())
gary = Employee("Gary Gary", "Manager", datetime.datetime.now())
# cool_company.add_employees(bob)
cool_company.add_employees(mob)
cool_company.add_employees(bob)
bad_company.add_employees(gog)
bad_company.add_employees(cob)
bad_company.add_employees(gary)
mob.describe_employee()
bob.describe_employee()
cool_company.describe_company()
bad_company.describe_company()
