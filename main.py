import os
from database import load_expenses, save_expenses, load_budgets, save_budgets
from view_budget import show_budget
from expenses import add_expenses
from set_budget import set_budget
from view_budget import show_budget
from view_expenses import view_expenses

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        print("       EXPENSE TRACKER MENU")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Check Budget Status")
        print("9. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            show_budget()
        elif choice == '9':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
        input("\nPress Enter to continue...")
        clear_screen()
        
if __name__ == "__main__":
    clear_screen()
    main_menu()
