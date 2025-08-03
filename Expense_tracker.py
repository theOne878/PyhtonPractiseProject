import csv
from collections import defaultdict, Counter
from datetime import datetime

file_path = 'expenses.csv'

# Load data
def load_expenses(file_path):
    expenses = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Amount'] = float(row['Amount'])  # convert amount
            row['Date'] = datetime.strptime(row['Date'], "%Y-%m-%d")
            expenses.append(row)
    return expenses

# Display all expenses
def display_expenses(expenses):
    print("\n=== All Expenses ===")
    for e in expenses:
        print(f"{e['Date'].date()} - ${e['Amount']:.2f} - {e['Category']} - {e['Description']}")
    print()

# Count total expenses
def count_expenses(expenses):
    return len(expenses)

# Total amount spent
def total_spent(expenses):
    return sum(e['Amount'] for e in expenses)

# Most frequent category
def most_common_category(expenses):
    categories = [e['Category'] for e in expenses]
    counter = Counter(categories)
    return counter.most_common(1)[0]  # (Category, Count)

# Total spent per month
def total_per_month(expenses):
    month_totals = defaultdict(float)
    for e in expenses:
        month = e['Date'].strftime("%Y-%m")
        month_totals[month] += e['Amount']
    return month_totals

# Month with highest spending
def most_expensive_month(month_totals):
    return max(month_totals.items(), key=lambda x: x[1])  # (Month, Total)

# Average expense
def average_expense(expenses):
    if not expenses:
        return 0
    return total_spent(expenses) / len(expenses)

if __name__ == "__main__":
    # Main logic
    try:
        expenses = load_expenses(file_path)

        display_expenses(expenses)
        print(f"🧾 Total number of expenses: {count_expenses(expenses)}")
        print(f"💸 Total amount spent: ${total_spent(expenses):.2f}")

        category, count = most_common_category(expenses)
        print(f"📊 Most frequent category: {category} ({count} entries)")

        month_totals = total_per_month(expenses)
        print("\n🗓️ Total spent per month:")
        for month, total in sorted(month_totals.items()):
            print(f"  {month}: ${total:.2f}")

        most_exp_month, most_exp_total = most_expensive_month(month_totals)
        print(f"\n💥 Most expensive month: {most_exp_month} (${most_exp_total:.2f})")

        print(f"📉 Average expense amount: ${average_expense(expenses):.2f}")
    
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found!")
        print("💡 Create an 'expenses.csv' file with the following format:")
        print("Date,Amount,Category,Description")
        print("2024-01-15,25.99,Food,Lunch")
    except Exception as e:
        print(f"❌ Error: {e}")
