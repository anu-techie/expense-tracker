import argparse
import os
import json
import csv
from datetime import datetime

DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
expense_file = os.path.join(DATA_DIR, 'expense_file.json')
budget_file = os.path.join(DATA_DIR, 'budget_file.json')
export_file = os.path.join(DATA_DIR, 'expenses_export.csv')

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

def add_expenses(args):
    expense = {
        'id': generate_id(),
        'date' : args.date if args.date else get_current_date(),
        'description': args.description,
        'amount' : args.amount,
        'category' : args.category,
    }
    
    if expense['amount'] < 0:
        print('Amount must be non negative')
        return
    
    expenses = load_file()
    expenses.append(expense)
    save_file(expenses)

    print("expense added successfully (ID : {expense['id']})")

def view_expenses(_):
    expenses = load_file()
    if not expenses:
        print('No records found')
        return
    
    for exp in expenses:
        print(f"{exp['id']}  |  {exp['date']}  |  {exp['description']}  |  {exp['amount']}  |  {exp['category']}")

def update_expenses(args):
    expenses = load_file()
    for exp in expenses:
        if exp['id'] == args.id:
            if args.date:
                exp['date'] = args.date
            else:
                exp['date'] = get_current_date()

            if args.description:
                exp['description'] = args.description
            
            if args.amount:
                if args.amount is not None:
                    if args.amount < 0:
                        print('Amount must be non negative')
                        return
                exp['amount'] = args.amount
            
            if args.category:
                exp['category'] = args.category
            
            save_file(expenses)
            print('Expense Updated')
            return
    print("Expense not found")

def delete_expenses(args):
    expenses = load_file()
    new_expenses = [exp for exp in expenses if exp['id'] != args.id]
    if len(expenses) == len(new_expenses):
        print('Expense not found')
    else:
        save_file(new_expenses)
        print(f'Expense of {args.id} deleted')

def summary_all(_):
    expenses = load_file()
    summary = sum([exp['amount']for exp in expenses])
    print(f'Total Expenses = {summary}')

def summary_by_month(args):
    expenses = load_file()
    month = args.month
    this_year = datetime.now().year
    monthly_expenses = [
        exp for exp in expenses
        if datetime.strptime(exp['date'], "%Y-%m-%d").month == month and
        datetime.strptime(exp['date'], "%Y-%m-%d").year == this_year
    ]

    total = sum([exp['amount'] for exp in monthly_expenses])
    print(f'total expenses of {datetime(1900, month, 1).strftime('%B')} {this_year} is {total:.2f}')

    check_budget(month, total)

def filter_by_category(args):
    expenses = load_file()
    filtered = [exp for exp in expenses if exp['category'].lower() == args.category.lower()]
    for exp in filtered:
        print(f'{exp['id']}  |  {exp['date']}  |  {exp['description']}  |  {exp['amount']}  |  {exp['category']}')

def set_budjet(args):
    if args.amount < 0 or not 1 <= args.month <=12:
        print('Invalide Budjet')
        return
    
    budget = {}
    if os.path.exists(budget_file):
        with open(budget_file, 'r') as file:
            budget = json.load(file)
    budget[str(args.month)] = args.amount
    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=2)
    print(f'Budjet for month {args.month} set to {args.amount}')

def check_budget(month, total):
    if os.path.exists(budget_file):
        with open(budget_file, 'r') as file:
            budget = json.load(file)
        budget_amount = budget.get(str(month))
        if budget_amount and total > budget_amount:
            print('Budget Exceeded')
        
def export_to_csv(_):
    expenses = load_file()
    filename = export_file
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id','date', 'description', 'amount', 'category'])
        writer.writeheader()
        writer.writerows(expenses)
    print(f'Exported to {filename}')

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    #Add
    add = subparsers.add_parser('add', help = 'Add a new expense')
    add.add_argument('--date', help='YYYY-MM-DD (optional)')
    add.add_argument('--description', required = True)
    add.add_argument('--amount', required=True, type=float)
    add.add_argument('--category', required=True)
    add.set_defaults(func=add_expenses)

     # view by category
    view = subparsers.add_parser('list', help='View all expenses or by category ')
    view.add_argument('--category', help='give category name already in the list')
    view.set_defaults(func=filter_by_category if '--category' in os.sys.argv else view_expenses)

    # Update
    update = subparsers.add_parser('update', help='Update expenses entry')
    update.add_argument('--id', type=int, required=True)
    update.add_argument('--date', help='YYYY-MM-DD (optional)')
    update.add_argument('--description', required = True)
    update.add_argument('--amount', required=True, type=float)
    update.add_argument('--category', required=True)
    update.set_defaults(func=update_expenses)

    # Delete
    delete = subparsers.add_parser('delete', help='delete a expense entry')
    delete.add_argument('--id', type=int, required=True)
    delete.set_defaults(func=delete_expenses)


    # Summary

    summary = subparsers.add_parser('summary', help='View Total expenses or by month')
    summary.add_argument('--month', type=int, help='Month number (1-12)')
    summary.set_defaults(func=summary_by_month if '--month' in os.sys.argv else summary_all)

    # Budget

    budget = subparsers.add_parser('budget', help='set month budget')
    budget.add_argument('--month', type=int, required=True)
    budget.add_argument('--amount', type=int, required=True)
    budget.set_defaults(func=set_budjet)

    # Export
    export = subparsers.add_parser('export', help='export expenses to CSV')
    export.set_defaults(func=export_to_csv)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()