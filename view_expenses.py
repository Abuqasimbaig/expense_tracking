from database import load_expenses, expenses
import os

def view_expenses():
    load_expenses()
    
    
    print(f"Current directory: {os.getcwd()}")
    print(f"Number of expenses loaded: {len(expenses)}")
    print(f"Expenses data: {expenses}")
    print("-" * 60)

    if not expenses:
        print("No Expenses found")
        return
    
    print("1- View All Expenses")
    print("2- Filter By Category")

    choice = input("Enter your choice: ")

    if choice == "2":
        category = input("Enter your category: ")
        filtered = []
        for exp in expenses:
            
            exp_category = exp.get("catagory") or exp.get("category", "")
            if exp_category == category:
                filtered.append(exp)
        
        if not filtered:
            print(f"No expenses found for category: {category}")
            return
    else:
        filtered = expenses

    total = 0

    for fill in filtered:
        
        category_value = fill.get("catagory") or fill.get("category", "Unknown")
        
        print(f"ID: {fill['unique_id']}")
        print(f"Category: {category_value}")
        print(f"Amount: ${float(fill['amount']):.2f}")
        print(f"Description: {fill['description']}")
        print(f"Date: {fill['today']}")
        

        total += float(fill['amount'])

    print(f"\n Total amount: ${total:.2f}")


