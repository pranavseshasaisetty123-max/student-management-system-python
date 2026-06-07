students = []

students = []

try:

    file = open("student_management.txt", "r")

    for line in file:

        line = line.strip()

        data = line.split(",")

        students.append(
            [
                data[0],
                float(data[1])
            ]
        )

    file.close()

except FileNotFoundError:

    pass
print(students)
def add_student():

    name = input("Enter student name: ")

    marks = float(input("Enter marks: "))

    students.append([name, marks])

    print("Student added successfully!")
def view_students():

    print("\nStudent Records")

    for student in students:

        print(
            student[0],
            "-",
            student[1]
        )
def search_student():

    name = input("Enter student name: ")

    found = False

    for student in students:

        if student[0].lower() == name.lower():

            print(
                "\nStudent Found"
            )

            print(
                student[0],
                "-",
                student[1]
            )

            found = True

    if not found:
        print("Student not found")

def find_topper():

    if len(students) == 0:
        print("No students available")
        return

    topper = students[0]

    for student in students:

        if student[1] > topper[1]:
            topper = student

    print("\nTopper")
    print(topper[0], "-", topper[1])

def show_average():
    if len(students) == 0:
        print("No students available")
        return
    total =0
    for student in students:
        total+=student[1]
    average=(total)/(len(students))
    print("Average:",average)

def show_top_3():

    if len(students) == 0:
        print("No students available")
        return

    sorted_students = students.copy()

    sorted_students.sort(
        key=lambda student: student[1],
        reverse=True
    )

    print("\nTop 3 Students")

    for student in sorted_students[:3]:
        print(student[0], "-", student[1])

while True:

    print("\nStudent Management System")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Average")
    print("6. Top 3 Students")
    print("7. Save Marks")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        show_average()

    elif choice == "6":
        show_top_3()

    elif choice == "7":
        file = open("student_management.txt","w")
        for student in students:
            file.write(f"{student[0]},{student[1]}\n")

        file.close()

        print("Marks saved successfully!")
    elif choice == "8":
        print("Goodbye!")
        break

