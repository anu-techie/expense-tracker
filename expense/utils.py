import os
import json
from datetime import datetime

DATA_DIR = 'data'
expense_file = os.path.join(DATA_DIR, 'expense_file.json')
budget_file = os.path.join(DATA_DIR, 'budget_file.json')
export_file = os.path.join(DATA_DIR, 'expenses_export.csv')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_file():
    if not os.path.exists(expense_file):
        return []
    with open(expense_file, 'r') as f:
        return json.load(f)
    
def save_file(expense):
    with open(expense_file, 'w') as f:
        json.dump(expense, f, indent=2)

def get_current_date():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def generate_id():
    expenses = load_file()
    id = max([exp['id'] for exp in expenses], default=0)+1
    return id

def load_budget():
    if os.path.exists(budget_file):
        with open(budget_file, 'r') as file:
            budget = json.load(file)
            return budget

def save_budget(budget):
    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=2)
