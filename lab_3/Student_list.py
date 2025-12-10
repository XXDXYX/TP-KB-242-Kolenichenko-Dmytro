from Student import Student
class StudentList:
    
    def __init__(self):
        self.students = []

    def addNewElement(self):
        name = input("Pease enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        country = input("Please enter student country: ")
        new_student = Student(name, age, phone, country)
        insertPosition = 0
        for student in self.students:

            if name > student.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, new_student)
        print("New element has been added")
        return
    def deleteElement(self):
        name = input("Please enter name to be delated: ")
        deletePosition = -1
        for item in self.students:

            if name == item.name:
                deletePosition = self.students.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Dele position " + str(deletePosition))
            del self.students[deletePosition]
        return
    def updateElement(self):
        name = input("Please enter name to be updated: ")
        deletePosition = -1
        for item in self.students:

            if name == item.name:
                deletePosition = self.students.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            del self.students[deletePosition]
            name = input("Pease enter student name: ")
            phone = input("Please enter student phone: ")
            age = input("Please enter student age: ")
            country = input("Please enter student country: ")
            new_student = Student(name, age, phone, country)
  
            insertPosition = 0
            for student in self.students:
  
                if name > student.name:
                    insertPosition += 1
                else:
                    break
            self.students.insert(insertPosition, new_student)
            print("Element has been updated")
        return
    def showAllElements(self):
        for item in self.students:
            print("Name: " + item.name + ", Age: " + item.age + ", Phone: " + item.phone + ", Country: " + item.country)
        return