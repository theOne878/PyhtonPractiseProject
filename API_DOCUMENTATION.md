# Python Practice Project - API Documentation

## Overview
This project contains two main modules for educational Python programming:
1. **Calculator** - A calculator with persistent history
2. **Expense Tracker** - A personal expense management system

---

## Calculator Module (`Calculator.py`)

### Class: `Calculator`

A calculator class that performs basic arithmetic operations and automatically saves results to a CSV file.

#### Constructor
```python
Calculator()
```

**Description:** Initializes a new calculator instance and creates/opens a CSV file for storing calculation history.

**File Created:** `Calculations.csv` - Contains timestamped calculation results

**Example:**
```python
from Calculator import Calculator

calc = Calculator()
# Output: Calculator initialized. Ready for calculations.
# Output: Previous results saved in Calculations.csv
```

#### Methods

##### `add(*args)`
**Description:** Adds multiple numbers to the current result and saves to CSV.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to add

**Returns:** None (modifies `self.result`)

**Example:**
```python
calc = Calculator()
calc.add(5, 10, 3)  # Adds 5 + 10 + 3 = 18 to result
calc.add(2)         # Adds 2 to current result
```

##### `subtract(*args)`
**Description:** Subtracts multiple numbers from the current result and saves to CSV.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to subtract

**Returns:** None (modifies `self.result`)

**Example:**
```python
calc = Calculator()
calc.add(20)        # result = 20
calc.subtract(5, 3) # result = 20 - 5 - 3 = 12
```

##### `multiply(*args)`
**Description:** Multiplies the current result by multiple numbers and saves to CSV.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to multiply

**Returns:** None (modifies `self.result`)

**Note:** If result is 0, it's automatically set to 1 before multiplication.

**Example:**
```python
calc = Calculator()
calc.add(5)           # result = 5
calc.multiply(2, 3)   # result = 5 * 2 * 3 = 30
```

##### `divide(*args)`
**Description:** Divides the current result by multiple numbers and saves to CSV.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to divide by

**Returns:** None (modifies `self.result`)

**Raises:** `ValueError` if any argument is zero

**Example:**
```python
calc = Calculator()
calc.add(100)       # result = 100
calc.divide(2, 5)   # result = 100 / 2 / 5 = 10

# Error handling
try:
    calc.divide(0)
except ValueError as e:
    print(e)  # "Cannot divide by zero"
```

#### Attributes

##### `result`
**Type:** `float` or `int`
**Description:** Stores the current calculation result
**Initial Value:** `0`

**Example:**
```python
calc = Calculator()
calc.add(15)
print(calc.result)  # Output: 15
```

### Utility Functions

#### `save_to_csv(data, file_path)`
**Description:** Saves calculation data to a CSV file.

**Parameters:**
- `data` (list): List of rows to write to CSV
- `file_path` (str): Path to the CSV file

**Example:**
```python
from Calculator import save_to_csv

data = [["Operation", "Result"], ["Addition", 25]]
save_to_csv(data, "my_calculations.csv")
```

#### `read_csv(file_path)`
**Description:** Reads and prints all rows from a CSV file.

**Parameters:**
- `file_path` (str): Path to the CSV file to read

**Example:**
```python
from Calculator import read_csv

read_csv("Calculations.csv")
# Outputs all rows from the file
```

### Complete Usage Example

```python
from Calculator import Calculator, read_csv

# Create calculator instance
calc = Calculator()

# Perform calculations
calc.add(10, 5)      # result = 15
calc.subtract(3)     # result = 12
calc.multiply(2)     # result = 24
calc.divide(4)       # result = 6

print(f"Final result: {calc.result}")  # Final result: 6.0

# View calculation history
read_csv("Calculations.csv")
```

---

## Expense Tracker Module (`Expense_tracker.py`)

### Data Structure
The expense tracker works with CSV files containing the following columns:
- `Date` (YYYY-MM-DD format)
- `Amount` (numeric)
- `Category` (string)
- `Description` (string)

### Functions

#### `load_expenses(file_path)`
**Description:** Loads expense data from a CSV file and converts data types.

**Parameters:**
- `file_path` (str): Path to the CSV file containing expense data

**Returns:** `list[dict]` - List of expense dictionaries with converted data types

**Data Conversions:**
- `Amount`: Converted to `float`
- `Date`: Converted to `datetime` object

**Example:**
```python
from Expense_tracker import load_expenses

expenses = load_expenses("expenses.csv")
# Returns: [
#   {
#     'Date': datetime(2024, 1, 15),
#     'Amount': 25.99,
#     'Category': 'Food',
#     'Description': 'Lunch at restaurant'
#   },
#   ...
# ]
```

#### `display_expenses(expenses)`
**Description:** Prints all expenses in a formatted table.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** None (prints to console)

**Example:**
```python
from Expense_tracker import load_expenses, display_expenses

expenses = load_expenses("expenses.csv")
display_expenses(expenses)
# Output:
# === All Expenses ===
# 2024-01-15 - $25.99 - Food - Lunch at restaurant
# 2024-01-16 - $12.50 - Transport - Bus fare
```

#### `count_expenses(expenses)`
**Description:** Returns the total number of expense entries.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** `int` - Number of expenses

**Example:**
```python
from Expense_tracker import load_expenses, count_expenses

expenses = load_expenses("expenses.csv")
total = count_expenses(expenses)
print(f"Total expenses: {total}")  # Total expenses: 25
```

#### `total_spent(expenses)`
**Description:** Calculates the total amount spent across all expenses.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** `float` - Total amount spent

**Example:**
```python
from Expense_tracker import load_expenses, total_spent

expenses = load_expenses("expenses.csv")
total = total_spent(expenses)
print(f"Total spent: ${total:.2f}")  # Total spent: $1,234.56
```

#### `most_common_category(expenses)`
**Description:** Finds the category with the most expense entries.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** `tuple` - (category_name, count)

**Example:**
```python
from Expense_tracker import load_expenses, most_common_category

expenses = load_expenses("expenses.csv")
category, count = most_common_category(expenses)
print(f"Most frequent: {category} ({count} times)")
# Most frequent: Food (15 times)
```

#### `total_per_month(expenses)`
**Description:** Calculates total spending for each month.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** `defaultdict(float)` - Dictionary with month keys (YYYY-MM) and total values

**Example:**
```python
from Expense_tracker import load_expenses, total_per_month

expenses = load_expenses("expenses.csv")
monthly_totals = total_per_month(expenses)
for month, total in monthly_totals.items():
    print(f"{month}: ${total:.2f}")
# 2024-01: $456.78
# 2024-02: $523.45
```

#### `most_expensive_month(month_totals)`
**Description:** Finds the month with the highest total spending.

**Parameters:**
- `month_totals` (dict): Dictionary from `total_per_month()` function

**Returns:** `tuple` - (month, total_amount)

**Example:**
```python
from Expense_tracker import load_expenses, total_per_month, most_expensive_month

expenses = load_expenses("expenses.csv")
monthly_totals = total_per_month(expenses)
month, amount = most_expensive_month(monthly_totals)
print(f"Highest spending: {month} (${amount:.2f})")
# Highest spending: 2024-03 ($789.12)
```

#### `average_expense(expenses)`
**Description:** Calculates the average amount per expense.

**Parameters:**
- `expenses` (list): List of expense dictionaries

**Returns:** `float` - Average expense amount (0 if no expenses)

**Example:**
```python
from Expense_tracker import load_expenses, average_expense

expenses = load_expenses("expenses.csv")
avg = average_expense(expenses)
print(f"Average expense: ${avg:.2f}")  # Average expense: $45.67
```

### Complete Usage Example

```python
from Expense_tracker import (
    load_expenses, display_expenses, count_expenses, total_spent,
    most_common_category, total_per_month, most_expensive_month, average_expense
)

# Load expenses from CSV file
expenses = load_expenses("expenses.csv")

# Display all expenses
display_expenses(expenses)

# Basic statistics
print(f"Total expenses: {count_expenses(expenses)}")
print(f"Total spent: ${total_spent(expenses):.2f}")
print(f"Average expense: ${average_expense(expenses):.2f}")

# Category analysis
category, count = most_common_category(expenses)
print(f"Most frequent category: {category} ({count} entries)")

# Monthly analysis
monthly_totals = total_per_month(expenses)
print("\nMonthly spending:")
for month, total in sorted(monthly_totals.items()):
    print(f"  {month}: ${total:.2f}")

# Find highest spending month
month, amount = most_expensive_month(monthly_totals)
print(f"\nHighest spending month: {month} (${amount:.2f})")
```

### CSV File Format

Create an `expenses.csv` file with the following format:

```csv
Date,Amount,Category,Description
2024-01-15,25.99,Food,Lunch at restaurant
2024-01-16,12.50,Transport,Bus fare
2024-01-17,89.99,Shopping,New shoes
2024-01-18,5.99,Food,Coffee
2024-01-20,150.00,Utilities,Electricity bill
```

**Column Requirements:**
- `Date`: Use YYYY-MM-DD format
- `Amount`: Numeric values (decimals allowed)
- `Category`: Any string (e.g., Food, Transport, Shopping, Utilities)
- `Description`: Any string describing the expense

---

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- Standard library modules: `csv`, `time`, `datetime`, `collections`

### Running the Modules

#### Calculator
```python
# Run directly
python Calculator.py

# Or import and use
from Calculator import Calculator
calc = Calculator()
calc.add(10, 5)
```

#### Expense Tracker
```python
# First, create an expenses.csv file with your data
# Then run:
python Expense_tracker.py

# Or import specific functions
from Expense_tracker import load_expenses, total_spent
expenses = load_expenses("expenses.csv")
total = total_spent(expenses)
```

### File Structure
```
project/
├── Calculator.py           # Calculator module
├── Expense_tracker.py      # Expense tracker module
├── README.md              # Project overview
├── API_DOCUMENTATION.md   # This documentation
├── Calculations.csv       # Auto-generated calculator history
└── expenses.csv          # User-created expense data
```

---

## Error Handling

### Calculator Module
- **Division by Zero**: Raises `ValueError` with message "Cannot divide by zero"
- **File Access**: Handles `FileExistsError` when CSV file already exists

### Expense Tracker Module
- **File Not Found**: Will raise `FileNotFoundError` if CSV file doesn't exist
- **Invalid Date Format**: Will raise `ValueError` if date format is incorrect
- **Invalid Amount**: Will raise `ValueError` if amount cannot be converted to float
- **Empty Expense List**: `average_expense()` returns 0 for empty lists

### Best Practices
1. Always create the CSV file before using expense tracker functions
2. Use proper date format (YYYY-MM-DD) in expense data
3. Handle exceptions when calling functions that might fail
4. Validate input data before processing

---

## Contributing

To extend this project:
1. Follow Python naming conventions (PEP 8)
2. Add docstrings to new functions
3. Include error handling for edge cases
4. Update this documentation for new features
5. Add unit tests for new functionality