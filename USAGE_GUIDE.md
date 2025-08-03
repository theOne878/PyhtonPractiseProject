# Usage Guide

This guide provides practical examples and step-by-step instructions for using the Python Practice Project modules.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Calculator Module Usage](#calculator-module-usage)
3. [Expense Tracker Module Usage](#expense-tracker-module-usage)
4. [Advanced Examples](#advanced-examples)
5. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Required modules: `csv`, `datetime`, `collections`

### File Structure
```
project/
├── Calculator.py
├── Expense_tracker.py
├── expenses.csv
├── API_DOCUMENTATION.md
├── USAGE_GUIDE.md
└── README.md
```

---

## Calculator Module Usage

### Basic Calculator Operations

#### 1. Initialize Calculator
```python
from Calculator import Calculator

# Create a new calculator instance
calc = Calculator()
```

#### 2. Perform Basic Calculations
```python
# Addition
calc.add(10, 20, 30)  # Result: 60

# Subtraction
calc.subtract(15)      # Result: 45

# Multiplication
calc.multiply(2, 3)    # Result: 270

# Division
calc.divide(3)         # Result: 90
```

#### 3. View Calculation History
```python
from Calculator import read_csv

# Display all previous calculations
read_csv('Calculations.csv')
```

### Advanced Calculator Examples

#### Example 1: Complex Calculation Chain
```python
from Calculator import Calculator

calc = Calculator()

# Start with addition
calc.add(100, 50)           # 150

# Subtract some values
calc.subtract(25, 10)       # 115

# Multiply by factors
calc.multiply(2, 1.5)       # 345

# Divide to get final result
calc.divide(3)              # 115.0

print("Final result:", calc.result)
```

#### Example 2: Financial Calculations
```python
from Calculator import Calculator

calc = Calculator()

# Calculate monthly budget
monthly_income = 3000
rent = 1200
utilities = 200
groceries = 400
entertainment = 300

calc.add(monthly_income)                    # 3000
calc.subtract(rent, utilities)              # 1600
calc.subtract(groceries, entertainment)     # 900

remaining_budget = calc.result
print(f"Remaining budget: ${remaining_budget:.2f}")
```

#### Example 3: Scientific Calculations
```python
from Calculator import Calculator

calc = Calculator()

# Calculate area of a circle (π * r²)
radius = 5
pi = 3.14159

calc.add(radius)           # 5
calc.multiply(radius)      # 25
calc.multiply(pi)          # 78.53975

area = calc.result
print(f"Circle area: {area:.2f}")
```

---

## Expense Tracker Module Usage

### Basic Expense Analysis

#### 1. Load and Display Expenses
```python
from Expense_tracker import load_expenses, display_expenses

# Load expense data
expenses = load_expenses('expenses.csv')

# Display all expenses
display_expenses(expenses)
```

#### 2. Basic Statistics
```python
from Expense_tracker import (
    count_expenses, total_spent, average_expense,
    most_common_category
)

# Get basic statistics
total_count = count_expenses(expenses)
total_amount = total_spent(expenses)
avg_amount = average_expense(expenses)
category, count = most_common_category(expenses)

print(f"Total expenses: {total_count}")
print(f"Total spent: ${total_amount:.2f}")
print(f"Average expense: ${avg_amount:.2f}")
print(f"Most common category: {category} ({count} entries)")
```

#### 3. Monthly Analysis
```python
from Expense_tracker import total_per_month, most_expensive_month

# Get monthly totals
monthly_totals = total_per_month(expenses)

# Display monthly breakdown
print("\nMonthly Spending:")
for month, total in sorted(monthly_totals.items()):
    print(f"  {month}: ${total:.2f}")

# Find most expensive month
most_exp_month, most_exp_total = most_expensive_month(monthly_totals)
print(f"\nMost expensive month: {most_exp_month} (${most_exp_total:.2f})")
```

### Advanced Expense Analysis

#### Example 1: Category Analysis
```python
from Expense_tracker import load_expenses
from collections import defaultdict

expenses = load_expenses('expenses.csv')

# Analyze spending by category
category_totals = defaultdict(float)
for expense in expenses:
    category_totals[expense['Category']] += expense['Amount']

print("Spending by Category:")
for category, total in sorted(category_totals.items()):
    percentage = (total / sum(category_totals.values())) * 100
    print(f"  {category}: ${total:.2f} ({percentage:.1f}%)")
```

#### Example 2: Daily Spending Patterns
```python
from Expense_tracker import load_expenses
from collections import defaultdict

expenses = load_expenses('expenses.csv')

# Analyze spending by day of week
day_totals = defaultdict(float)
for expense in expenses:
    day = expense['Date'].strftime('%A')
    day_totals[day] += expense['Amount']

print("Spending by Day of Week:")
for day, total in sorted(day_totals.items()):
    print(f"  {day}: ${total:.2f}")
```

#### Example 3: Budget Tracking
```python
from Expense_tracker import load_expenses, total_spent

expenses = load_expenses('expenses.csv')

# Set monthly budget
monthly_budget = 1000
total_spent_amount = total_spent(expenses)

# Calculate budget status
budget_remaining = monthly_budget - total_spent_amount
budget_percentage = (total_spent_amount / monthly_budget) * 100

print(f"Monthly Budget: ${monthly_budget:.2f}")
print(f"Total Spent: ${total_spent_amount:.2f}")
print(f"Remaining: ${budget_remaining:.2f}")
print(f"Budget Used: {budget_percentage:.1f}%")

if budget_remaining < 0:
    print("⚠️  Over budget!")
elif budget_percentage > 80:
    print("⚠️  Close to budget limit")
else:
    print("✅ Within budget")
```

---

## Advanced Examples

### Example 1: Combined Calculator and Expense Analysis
```python
from Calculator import Calculator
from Expense_tracker import load_expenses, total_spent

# Load expenses
expenses = load_expenses('expenses.csv')
total_expenses = total_spent(expenses)

# Use calculator for financial planning
calc = Calculator()

# Calculate savings potential
income = 3000
calc.add(income)                    # 3000
calc.subtract(total_expenses)       # Remaining after expenses

savings_potential = calc.result
savings_percentage = (savings_potential / income) * 100

print(f"Monthly Income: ${income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Potential Savings: ${savings_potential:.2f}")
print(f"Savings Rate: {savings_percentage:.1f}%")
```

### Example 2: Expense Forecasting
```python
from Expense_tracker import load_expenses, average_expense
from Calculator import Calculator

expenses = load_expenses('expenses.csv')
avg_expense = average_expense(expenses)

# Use calculator for forecasting
calc = Calculator()

# Calculate projected annual spending
days_in_month = 30
months_in_year = 12

calc.add(avg_expense)              # Average daily expense
calc.multiply(days_in_month)       # Monthly projection
calc.multiply(months_in_year)      # Annual projection

annual_projection = calc.result

print(f"Average daily expense: ${avg_expense:.2f}")
print(f"Projected annual spending: ${annual_projection:.2f}")
```

### Example 3: Custom Expense Reports
```python
from Expense_tracker import load_expenses
from datetime import datetime, timedelta

expenses = load_expenses('expenses.csv')

def generate_custom_report(expenses, days_back=7):
    """Generate a custom expense report for the last N days"""
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    recent_expenses = [
        e for e in expenses 
        if e['Date'] >= cutoff_date
    ]
    
    if not recent_expenses:
        print(f"No expenses found in the last {days_back} days")
        return
    
    total = sum(e['Amount'] for e in recent_expenses)
    categories = {}
    
    for expense in recent_expenses:
        cat = expense['Category']
        categories[cat] = categories.get(cat, 0) + expense['Amount']
    
    print(f"\n=== Last {days_back} Days Report ===")
    print(f"Total spent: ${total:.2f}")
    print(f"Number of expenses: {len(recent_expenses)}")
    print("\nBy Category:")
    for category, amount in sorted(categories.items()):
        print(f"  {category}: ${amount:.2f}")

# Generate reports
generate_custom_report(expenses, 7)   # Last week
generate_custom_report(expenses, 30)  # Last month
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. File Not Found Errors
**Problem:** `FileNotFoundError` when loading expenses.csv
```python
# Solution: Create the file with proper format
import csv

with open('expenses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Amount', 'Category', 'Description'])
    writer.writerow(['2023-01-15', '25.50', 'Food', 'Lunch'])
```

#### 2. Division by Zero
**Problem:** `ValueError` when dividing by zero
```python
# Solution: Check for zero before division
try:
    calc.divide(0)
except ValueError as e:
    print(f"Error: {e}")
```

#### 3. Date Format Issues
**Problem:** `ValueError` when parsing dates
```python
# Solution: Ensure dates are in YYYY-MM-DD format
# Correct: 2023-01-15
# Incorrect: 01/15/2023 or 15-01-2023
```

#### 4. Data Type Issues
**Problem:** `ValueError` when converting amounts
```python
# Solution: Ensure amounts are numeric
# Correct: 25.50
# Incorrect: $25.50 or "25.50"
```

### Performance Tips

1. **Large Datasets**: For large expense files, consider processing in chunks
2. **Memory Usage**: The expense tracker loads all data into memory
3. **File I/O**: Calculator operations write to CSV on each calculation

### Best Practices

1. **Data Validation**: Always validate input data before processing
2. **Error Handling**: Use try-catch blocks for file operations
3. **Backup Data**: Keep backups of your expense data
4. **Regular Maintenance**: Clean up old calculation history files periodically

---

## Quick Reference

### Calculator Quick Commands
```python
calc = Calculator()
calc.add(10, 20)        # Add numbers
calc.subtract(5)         # Subtract
calc.multiply(2, 3)      # Multiply
calc.divide(4)           # Divide
read_csv('Calculations.csv')  # View history
```

### Expense Tracker Quick Commands
```python
expenses = load_expenses('expenses.csv')
display_expenses(expenses)                    # Show all
total_spent(expenses)                         # Get total
most_common_category(expenses)                # Top category
total_per_month(expenses)                     # Monthly totals
```