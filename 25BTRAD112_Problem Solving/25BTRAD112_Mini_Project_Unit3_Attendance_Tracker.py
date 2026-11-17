# Mini Project (Unit 3): Attendance Tracker
students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Attendance")
    print("3. Display Attendance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students[name] = []

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter attendance (P/A): ").upper()
            students[name].append(status)
        else:
            print("Student not found")

    elif choice == 3:
        for name, records in students.items():
            total = len(records)
            present = records.count("P")

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print(name, records)
            print("Attendance:", percentage, "%")

            if percentage < 75:
                print("Below 75% attendance")

    elif choice == 4:
        break

    else:
        print("Invalid choice")
