import json
from database import load_expenses, load_budgets

def show_budget():
    global expenses
    # ✅ Step 1: Data load karo (functions call karo)
    expenses = load_expenses()  # List
    budgets = load_budgets()    # Dict
    
    # ✅ Step 2: Spent calculate karo
    spent = {}
    
    for exp in expenses:
        category = exp["category"]  # ✅ exp se nikalo
        amount = float(exp["amount"])       # ✅ exp se amount
        
        # Add to spent
        spent[category] = spent.get(category, 0) + amount
    
    # ✅ Step 3: Budget vs Spent compare karo
    print("\n" + "="*50)
    print("        BUDGET REPORT")
    print("="*50 + "\n")
    
    for category in budgets:
        budget_amount = budgets[category]
        spent_amount = spent.get(category, 0)
        remaining = budget_amount - spent_amount
        
        # Percentage calculate karo
        if budget_amount > 0:
            percentage = (spent_amount / budget_amount) * 100
        else:
            percentage = 0
        
        # Display karo
        print(f"Category: {category.title()}")
        print(f"  Budget:    Rs.{budget_amount}")
        print(f"  Spent:     Rs.{spent_amount}")
        print(f"  Remaining: Rs.{remaining}")
        print(f"  Usage:     {percentage:.1f}%")
        
        # ✅ Step 4: Warning dikha do agar over budget
        if spent_amount > budget_amount:
            print(f"  🚨 OVER BUDGET by Rs.{abs(remaining)}!")
        elif percentage >= 80:
            print(f"  ⚠️  Warning: {percentage:.0f}% used")
        else:
            print(f"  ✅ Within budget")
        
        print("-" * 50)
    
    # ✅ Extra: Categories jinki budget nahi set
    for category in spent:
        if category not in budgets:
            print(f"\n⚠️  '{category}' has no budget set!")
            print(f"   Spent: Rs.{spent[category]}")

