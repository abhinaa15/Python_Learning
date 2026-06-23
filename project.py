students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Find Highest Mark")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        mark = int(input("Enter Mark: "))
        students.append([name, mark])
        print("students added")

