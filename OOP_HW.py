# Creating Employee class with its attributes and methods

class Employee:
    
    # This is the constructor method that initializes the attributes when a new Employee object is created.
    def __init__(self,name,salary,email,phone):
        self.name=name
        self.salary=salary
        self.email=email
        self.phone=phone

    def Display_info(self):
        print("Name of employee is :",self.name)
        print("Salary of employee is :",self.salary)
        print("Email-id of employee is :",self.email)

# Creating the object of the class to access the attributes and methods
emp1=Employee("Manasi Jadhav",40000,"manasi2174@gmail.com",848367900)
emp1.Display_info()

emp2=Employee("Shrutika Padule",30000,"shruti@gmail.com",9890320710)
emp2.Display_info()


