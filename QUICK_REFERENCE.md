# Quick Reference Guide

## Calculator Module

### Class Methods
```python
calc = Calculator()                    # Initialize calculator
calc.add(*args)                        # Add numbers: calc.add(1, 2, 3)
calc.subtract(*args)                   # Subtract: calc.subtract(5, 2)
calc.multiply(*args)                   # Multiply: calc.multiply(2, 3, 4)
calc.divide(*args)                     # Divide: calc.divide(2, 5)
print(calc.result)                     # Access current result
```

### Utility Functions
```python
save_to_csv(data, file_path)           # Save data to CSV
read_csv(file_path)                    # Read and print CSV contents
```

## Expense Tracker Module

### Core Functions
```python
expenses = load_expenses("expenses.csv")              # Load expense data
display_expenses(expenses)                            # Print all expenses
count = count_expenses(expenses)                      # Get expense count
total = total_spent(expenses)                         # Get total amount
avg = average_expense(expenses)                       # Get average amount
```

### Analysis Functions
```python
category, count = most_common_category(expenses)      # Most frequent category
monthly_totals = total_per_month(expenses)           # Monthly spending breakdown
month, amount = most_expensive_month(monthly_totals) # Highest spending month
```

## Common Usage Patterns

### Calculator Chain Operations
```python
calc = Calculator()
calc.add(100).subtract(25).multiply(2).divide(5)     # Note: Methods don't return self
# Instead use:
calc.add(100)
calc.subtract(25)  
calc.multiply(2)
calc.divide(5)
print(calc.result)  # 30.0
```

### Expense Analysis Workflow
```python
# Load and analyze expenses
expenses = load_expenses("expenses.csv")
print(f"Total: ${total_spent(expenses):.2f}")
print(f"Average: ${average_expense(expenses):.2f}")

# Monthly breakdown
monthly = total_per_month(expenses)
for month, total in sorted(monthly.items()):
    print(f"{month}: ${total:.2f}")
```

## CSV File Formats

### Calculator Output (`Calculations.csv`)
```csv
Calculation Results
Timestamp: 2024-01-20 10:30:45

Result for addition: 
15
Result for subtraction: 
12
```

### Expense Input (`expenses.csv`)
```csv
Date,Amount,Category,Description
2024-01-15,25.99,Food,Lunch
2024-01-16,12.50,Transport,Bus fare
```

## Import Statements
```python
# Calculator
from Calculator import Calculator, save_to_csv, read_csv

# Expense Tracker (import all functions)
from Expense_tracker import (
    load_expenses, display_expenses, count_expenses, total_spent,
    most_common_category, total_per_month, most_expensive_month, average_expense
)

# Or import specific functions
from Expense_tracker import load_expenses, total_spent
```