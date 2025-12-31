import json
from database import load_budgets, save_budgets 

CATEGORIES = ['Food', 'Shopping', 'Bills', 'Entertainment', 'Other']

def set_budget():
    try:
        # ✅ Step 1: Existing budgets load karo
        budgets = load_budgets()  # Dict milegi: {"Food": 5000}
        
        # ✅ Step 2: Category select karo
        print("\n📋 Available Categories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        
        choice = int(input("\nSelect category (1-5): "))
        
        # ✅ Validate choice
        if choice < 1 or choice > len(CATEGORIES):
            print("❌ Invalid choice!")
            return
        
        category = CATEGORIES[choice - 1]
        
        # ✅ Step 3: Amount input (convert to float)
        amount = float(input(f"Enter budget amount for {category}: Rs."))
        
        # ✅ Step 4: Validate amount
        if amount <= 0:
            print("❌ Amount must be greater than 0")
            return
        
        # ✅ Step 5: Budget dictionary mein store
        budgets[category] = amount  # {"Food": 5000, "Transport": 2000}
        
        # ✅ Step 6: Save karo
        save_budgets(budgets)
        
        # ✅ Step 7: Success message
        print(f"\n✅ Budget set successfully!")
        print(f"   Category: {category}")
        print(f"   Amount: Rs.{amount}")
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
    except IndexError:
        print("❌ Invalid category selection!")
    except Exception as e:
        print(f"❌ Error: {e}")


set_budget()

