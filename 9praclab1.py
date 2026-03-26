class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_manager_data(self):
        self.get_data()
        self.department = input("Enter Department: ")

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("-------------------------")


# Main Program
managers = []

for i in range(10):
    print(f"\nEnter details of Manager {i+1}")
    m = Manager()
    m.get_manager_data()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display_manager()
