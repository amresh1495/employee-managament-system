import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return f"Department: {self.name}"


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            return True
        return False

    def display_departments(self):
        for department in self.departments.values():
            print(department)

    def save_to_file(self, filename):
        data = {
            "departments": {name: [emp.__dict__ for emp in dept.employees] for name, dept in self.departments.items()}
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        for department_name, employees in data["departments"].items():
            department = Department(department_name)
            for emp_data in employees:
                employee = Employee(**emp_data)
                department.add_employee(employee)
            self.add_department(department)


def display_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display All Departments")
    print("7. Save to File")
    print("8. Load from File")
    print("9. Exit")


def main():
    company = Company()

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")

            employee = Employee(name, emp_id, title, department_name)

            if department_name not in company.departments:
                print("Error: Department does not exist. Please add the department first.")
            else:
                company.departments[department_name].add_employee(employee)

        elif choice == '2':
            emp_id = input("Enter employee ID to remove: ")

            removed = False
            for department in company.departments.values():
                if department.remove_employee(emp_id):
                    removed = True
                    print(f"Employee with ID {emp_id} removed successfully.")
                    break

            if not removed:
                print(f"Error: Employee with ID {emp_id} not found.")

        elif choice == '3':
            department_name = input("Enter department name to display: ")

            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Error: Department does not exist.")

        elif choice == '4':
            department_name = input("Enter department name to add: ")
            department = Department(department_name)
            company.add_department(department)
            print(f"Department {department_name} added successfully.")

        elif choice == '5':
            department_name = input("Enter department name to remove: ")

            if company.remove_department(department_name):
                print(f"Department {department_name} removed successfully.")
            else:
                print(f"Error: Department {department_name} not found.")

        elif choice == '6':
            company.display_departments()

        elif choice == '7':
            filename = input("Enter filename to save data: ")
            company.save_to_file(filename)
            print(f"Data saved to {filename} successfully.")

        elif choice == '8':
            filename = input("Enter filename to load data from: ")
            company.load_from_file(filename)
            print(f"Data loaded from {filename} successfully.")

        elif choice == '9':
            print("Exiting Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
