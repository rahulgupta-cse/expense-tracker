 #Imports the CSV module to read from and write to CSV files
import csv
from datetime import datetime # Imports the datetime class to work with dates and times

expenses = []

file_name = "expenses.csv"

# Create file with header if not exists
try:
    with open(file_name, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Name", "Category", "Amount"])
except FileExistsError:
    pass

while True:
    print("\n-------------------------------")
    print("Available Options to Perform: ")
    print("-------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("\nEnter choice: ")

    #For adding of expenses in file 
    if choice == "1":
        name = input("Enter expense name: ")
        category = input("Enter category (Food/Travel/Sports/etc): ")
        amount = float(input("Enter amount: "))

        date = datetime.now().strftime("%Y-%m-%d")

        expenses.append((date, name, category, amount))

        # Save to CSV file
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, name, category, amount])

        print("Expense added successfully!")
    #To see the expenses details 
    elif choice == "2":
        print("\n" + "-"*70)
        print("                        PRODUCTS DETAILS")
        print("-"*70)
        print(f"{'Name':<20}{'Date':<15}{'Category':<20}{'Price':>5}")
        print("-"*70)

        total = 0

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                date, name, category, amount = row

                print(f"{name:<20}{date:<15}{category:<20}₹{float(amount):>8.1f}")
                total += float(amount)

        print("-"*70)
        print(f"{'Total Expense:':<55}₹  {total:.1f}")
        print("-"*70)

    #DELETE EXPENSE
    elif choice == "3":
        delete_name = input("Enter expense name to delete: ").lower()

        rows = []
        found = False

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row[1].lower() != delete_name:
                    rows.append(row)
                else:
                    found = True

        # Rewrite file without deleted record
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

        if found:
            print("-----------------------------")
            print("Expense deleted successfully!")
            print("-----------------------------")
        else:
            print("-----------------------------")
            print(" Expense not found!")
            print("-----------------------------")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")