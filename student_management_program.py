students = []

while True:
    print("Student Management System \n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        student = {}

        student["ID"] = input("Enter ID: ")
        student["Name"] = input("Enter Name: ")
        student["Age"] = input("Enter Age: ")
        student["Course"] = input("Enter Course: ")
        student["Marks"] = input("Enter Marks: ")

        students.append(student)
        print("Student Added Successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No student found.")
        else:
            for student in students:
                print(student)

    # Search Student
    elif choice == "3":
        sid = input("Enter Student ID: ")

        found = False

        for student in students:
            if student["ID"] == sid:
                print(student)
                found = True

        if found == False:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        sid = input("Enter Student ID: ")

        found = False

        for student in students:
            if student["ID"] == sid:
                student["Name"] = input("New Name: ")
                student["Age"] = input("New Age: ")
                student["Course"] = input("New Course: ")
                student["Marks"] = input("New Marks: ")
                print("Student Updated!")
                found = True

        if found == False:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        sid = input("Enter Student ID: ")

        found = False

        for student in students:
            if student["ID"] == sid:
                students.remove(student)
                print("Student Deleted!")
                found = True
                break

        if found == False:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")