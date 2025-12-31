import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "material.json")

expenses = []
budgets = {}  # ✅ budgets (plural)

# ------------------------
# Generic save function
# ------------------------
def _save_data(data, filename):
    """
    Internal helper function to save data to JSON.
    Returns True if success, False if error.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4, default=str)
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False

# ------------------------
# Load expenses
# ------------------------
def load_expenses():
    global expenses

    try:
        with open(EXPENSES_FILE, "r") as file:
            data = json.load(file)
            expenses.clear()
            expenses.extend(data.get("expenses", []))
    except FileNotFoundError:
        expenses.clear()
    except json.JSONDecodeError as e:
        print(f"DEBUG: JSON decode error: {e}")
        expenses.clear()
    except Exception as e:
        print(f"DEBUG: Unexpected error: {e}")
        expenses.clear()

    return expenses
# ------------------------
# Save expenses
# ------------------------
def save_expenses():
    load_budgets()  # keep budgets safe

    data = {
        "expenses": expenses,
        "budgets": budgets
    }

    return _save_data(data, EXPENSES_FILE)

# ------------------------
# Load budgets
# ------------------------
def load_budgets():
    global budgets

    try:
        with open(EXPENSES_FILE, "r") as f:
            data = json.load(f)
            budgets.clear()
            budgets.update(data.get("budgets", {}))
    except FileNotFoundError:
        budgets.clear()
    except json.JSONDecodeError as e:
        print(f"DEBUG: JSON decode error in budgets: {e}")
        budgets.clear()
    except Exception as e:
        print(f"DEBUG: Error loading budgets: {e}")
        budgets.clear()

    return budgets

# ------------------------
# Save budgets
# ------------------------
def save_budgets(budget_data):
    global budgets
    budgets = budget_data
    
    # Load latest expenses to avoid overwriting
    load_expenses()
    
    data = {
        "expenses": expenses,
        "budgets": budgets
    }
    
    success = _save_data(data, EXPENSES_FILE)
    if not success:
        print("Failed to save budgets.")
    return success
