import csv

file = "expenses.csv"


def add_expense():
    date = input("Date: ")
    category = input("Category: ")
    
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    note = input("Note: ")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("Expense added!")


def view_expenses():
    total = 0

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                print(row)
                total += float(row[2])

            print("Total:", total)

    except FileNotFoundError:
        print("No expenses found.")


def summary():
    data = {}

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                data[category] = data.get(category, 0) + amount

        for category in data:
            print(category, ":", data[category])

    except FileNotFoundError:
        print("No expenses found.")


while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        summary()

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice!")