import csv
from datetime import datetime
from .utils import (load_file, save_file, get_current_date, generate_id, load_budget, save_budget,  export_file)

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

    print(f"expense added successfully (ID : {expense['id']})")

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
    print(f'Total Expenses = {summary: .2f}')

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
    print(f'total expenses of {datetime(1900, month, 1).strftime("%B")} {this_year} is {total:.2f}')

    budget_amount = load_budget().get(str(month))
    if budget_amount and total > budget_amount:
        print('Budget Exceeded')

def filter_by_category(args):
    expenses = load_file()
    filtered = [exp for exp in expenses if exp['category'].lower() == args.category.lower()]
    for exp in filtered:
        print(f'{exp['id']}  |  {exp['date']}  |  {exp['description']}  |  {exp['amount']}  |  {exp['category']}')

def set_budget(args):
    if args.amount < 0 or not 1 <= args.month <=12:
        print('Invalide Budjet')
        return
    
    budget = load_budget()
    budget[str(args.month)] = args.amount
    save_budget(budget)
    print(f'Budget for month {args.month} set to {args.amount}')

def export_to_csv(_):
    expenses = load_file()
    with open(export_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id','date', 'description', 'amount', 'category'])
        writer.writeheader()
        writer.writerows(expenses)
    print(f'Exported to {export_file}')
