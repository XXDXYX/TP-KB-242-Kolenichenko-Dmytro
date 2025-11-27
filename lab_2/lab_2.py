from sys import argv
import csv

def printAllList(student_list):
    for elem in student_list:
        strForPrint = "Student name is " + elem["name"] + ", Age is " + str(elem["age"]) + ", Phone is " + elem["phone"] + ", Country is " + elem["country"]
        print(strForPrint)
    return

def addNewElement(student_list):
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    country = input("Please enter student country: ")
    newItem = {"name": name, "phone": phone, "age": age, "country": country}
    # find insert position
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement(student_list):
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del student_list[deletePosition]
    return

def updateElement(student_list):
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del student_list[deletePosition]
        name = input("Pease enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        country = input("Please enter student country: ")
        newItem = {"name": name, "phone": phone, "age": age, "country": country}
        # find insert position
        insertPosition = 0
        for item in student_list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        student_list.insert(insertPosition, newItem)
        print("Element has been updated")
    return

def main():
    student_list = []
    if len(argv) > 1:
        with open(argv[1],'r') as file:
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                student_list.append({"name": lines['name'], "age": int(lines['age']), "phone": lines['phone'], "country": lines['country']})
    else:
        print("No input file specified")
        exit()
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(student_list)
                printAllList(student_list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(student_list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(student_list)
            case "P" | "p":
                print("List will be printed")
                printAllList(student_list)
            case "X" | "x":
                print("Your data will be saved. Exiting now.")
                break
            case _:
                print("Wrong chouse")
    with open(argv[1],'w', newline='') as file:
        fieldnames = ['name', 'age', 'phone', 'country']
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for elem in student_list:
            writer.writerow({'name': elem["name"], 'age': elem["age"], 'phone': elem["phone"], 'country': elem["country"]})

if __name__ == "__main__":
    main()