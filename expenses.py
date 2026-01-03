import time
from datetime import date
from database import load_expenses, save_expenses, expenses

def add_expenses():
    load_expenses()
    
    try:
        category = input("Enter your category: ").strip()
        if not category:
            print("Category cannot be empty!")
            return
        
        amount_input = input("Add Expenses: ").strip()
        amount = float(amount_input)
        
        if amount <= 0:
            print("Amount must be greater than zero!")
            return
        
        description = input("Enter Description: ").strip()
        today = date.today()
        unique_id = int(time.time())
        
        new_expense = {
            "category": category,
            "amount": amount,
            "description": description,
            "today": today.isoformat(),
            "unique_id": unique_id,
        }
        
        expenses.append(new_expense)
        save_expenses()
        print("Expense added successfully!")
        print(f"Category: {category}")
        print(f"Amount: ${amount:.2f}")
        
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")

