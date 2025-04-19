#Static methods = A method that belongs to a class rather than any object from that class(instance)
# #                Usually used for general utility functions
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility fucntions that do not need access to class data


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return (f"{self.name} is a {self.position}")  # Instance method

    @staticmethod
#Static method = belongs to a Class Employee, not to a object, created from that class

    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions #zde vracíme zda POSITION je IN VALID_POSITIONS listu, TRUE nebo FALSE


employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Cigan"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

