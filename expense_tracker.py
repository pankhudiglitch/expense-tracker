while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = input("Amount: ")

        file = open("expenses.txt", "a")
        file.write(name + "," + amount + "\n")
        file.close()

        print("Expense added!")

    elif choice == "2":
        file = open("expenses.txt", "r")

        print("\nAll Expenses:")
        for line in file:
            print(line.strip())

        file.close()

    elif choice == "3":
        total = 0

        file = open("expenses.txt", "r")

        for line in file:
            data = line.strip().split(",")
            total += float(data[1])

        file.close()

        print("Total Spent =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")