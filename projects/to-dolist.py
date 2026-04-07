tasks = []

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
