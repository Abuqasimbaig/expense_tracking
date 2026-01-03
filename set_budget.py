import json
from database import load_budgets, save_budgets 

CATEGORIES = ['Food', 'Shopping', 'Bills', 'Entertainment', 'Other']

def set_budget():
    try:
        
        budgets = load_budgets()  
        
        
        print("\n📋 Available Categories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        
        choice = int(input("\n Select category (1-5): "))
        
        
        if choice < 1 or choice > len(CATEGORIES):
            print("Invalid choice!")
            return
        
        category = CATEGORIES[choice - 1]


        amount = float(input(f"Enter budget amount for {category}: Rs."))
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        
        budgets[category] = amount  

        save_budgets(budgets)

        print(f"\n Budget set successfully!")
        print(f"   Category: {category}")
        print(f"   Amount: Rs.{amount}")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except IndexError:
        print("Invalid category selection!")
    except Exception as e:
        print(f"Error: {e}")


set_budget()

