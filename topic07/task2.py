class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student name={self.name}, age={self.age}"

list_of_students = [
    Student("Alice", 20),
    Student("Bob", 22),
    Student("Charlie", 19),
    Student("Diana", 21)]

sorted_students = sorted(list_of_students, key=lambda student: student.name)

for student in sorted_students:
    print(student)

    