# Project: Expense Tracker - Installment 2
# Author: Kristine L. Torre
# Description: Displays the expense tracker landing page and main menu.

print("=" * 40)
print("\t  EXPENSE TRACKER")
print("\tTrack your expenses!")
print("=" * 40)


print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name?  ")
print(f"Welcome, {name}! Let's log two expenses.")


item1 = input("\nFirst Expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))

print("-" * 40)
print("SUMMARY")
print("-" * 40)
print(f" - {item1}: \t${amount1:.1f}")
print(f" - {item2}: \t${amount2:.1f}")

total = amount1 + amount2
print(f"Total spent: \t${total:.1f}")
average = total / 2
print(f"Average spent: \t${average:.2f}")

print("-" * 40)
print("Made by: Kristine L. Torre | Installment 2")
