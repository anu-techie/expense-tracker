import argparse
import os
from expense.core import(
    add_expenses, view_expenses, filter_by_category,
    update_expenses, delete_expenses, summary_all,
    summary_by_month, set_budget, export_to_csv
)

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
    budget.set_defaults(func=set_budget)

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