import json
from database import load_expenses, load_budgets

def show_budget():
    global expenses
    expenses = load_expenses()  
    budgets = load_budgets()        
    
    spent = {}
    
    for exp in expenses:
        category = exp["category"]  
        amount = float(exp["amount"])       
        
        
        spent[category] = spent.get(category, 0) + amount
    
    
    print("\n" + "="*50)
    print("        BUDGET REPORT")
    print("="*50 + "\n")
    
    for category in budgets:
        budget_amount = budgets[category]
        spent_amount = spent.get(category, 0)
        remaining = budget_amount - spent_amount
        
        
        if budget_amount > 0:
            percentage = (spent_amount / budget_amount) * 100
        else:
            percentage = 0
        
        
        print(f"Category: {category.title()}")
        print(f"  Budget:    Rs.{budget_amount}")
        print(f"  Spent:     Rs.{spent_amount}")
        print(f"  Remaining: Rs.{remaining}")
        print(f"  Usage:     {percentage:.1f}%")
        
        
        if spent_amount > budget_amount:
            print(f"OVER BUDGET by Rs.{abs(remaining)}!")
        elif percentage >= 80:
            print(f"Warning: {percentage:.0f}% used")
        else:
            print(f"Within budget")
        
        print("-" * 50)
    
    
    for category in spent:
        if category not in budgets:
            print(f"\n'{category}' has no budget set!")
            print(f"   Spent: Rs.{spent[category]}")

