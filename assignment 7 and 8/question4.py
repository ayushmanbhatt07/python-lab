# Create a class "Employee" with attributes name and salary. Implement overloaded operators +
# and - to combine and compare employees based on their salaries.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"