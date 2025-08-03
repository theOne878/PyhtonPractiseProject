# API Documentation

This document provides comprehensive documentation for all public APIs, functions, and components in the Python Practice Project.

## Table of Contents

1. [Calculator Module](#calculator-module)
2. [Expense Tracker Module](#expense-tracker-module)
3. [Global Functions](#global-functions)

---

## Calculator Module

### Class: `Calculator`

A calculator class that performs basic mathematical operations and maintains calculation history in a CSV file.

#### Constructor

```python
def __init__(self)
```

**Description:** Initializes a new Calculator instance and sets up the CSV file for storing calculation history.

**Parameters:** None

**Returns:** None

**Side Effects:**
- Creates a new CSV file named `Calculations.csv` if it doesn't exist
- Writes header information including timestamp
- If file already exists, prints a message and continues

**Example:**
```python
calculator = Calculator()
```

#### Methods

##### `add(*args)`

**Description:** Adds multiple numbers to the current result.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to add

**Returns:** None

**Side Effects:**
- Updates the internal `result` attribute
- Saves the calculation result to CSV file

**Example:**
```python
calculator = Calculator()
calculator.add(5, 10, 15)  # result = 30
```

##### `subtract(*args)`

**Description:** Subtracts multiple numbers from the current result.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to subtract

**Returns:** None

**Side Effects:**
- Updates the internal `result` attribute
- Saves the calculation result to CSV file

**Example:**
```python
calculator = Calculator()
calculator.subtract(10, 3)  # result = -13 (assuming previous result was 0)
```

##### `multiply(*args)`

**Description:** Multiplies the current result by multiple numbers.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to multiply

**Returns:** None

**Side Effects:**
- Updates the internal `result` attribute
- If result is 0, sets it to 1 before multiplication
- Saves the calculation result to CSV file

**Example:**
```python
calculator = Calculator()
calculator.multiply(2, 4, 7)  # result = 56
```

##### `divide(*args)`

**Description:** Divides the current result by multiple numbers.

**Parameters:**
- `*args` (numbers): Variable number of numeric arguments to divide by

**Returns:** None

**Raises:**
- `ValueError`: If any argument is zero (division by zero)

**Side Effects:**
- Updates the internal `result` attribute
- Saves the calculation result to CSV file

**Example:**
```python
calculator = Calculator()
calculator.divide(2)  # result = 28 (assuming previous result was 56)
```

---

## Expense Tracker Module

### Functions

#### `load_expenses(file_path)`

**Description:** Loads expense data from a CSV file and converts it to a list of dictionaries.

**Parameters:**
- `file_path` (str): Path to the CSV file containing expense data

**Returns:** `list[dict]` - List of expense dictionaries with keys: 'Date', 'Amount', 'Category', 'Description'

**Data Format:**
- Expected CSV columns: Date, Amount, Category, Description
- Date format: "YYYY-MM-DD"
- Amount: Converted to float
- Date: Converted to datetime object

**Example:**
```python
expenses = load_expenses('expenses.csv')
# Returns: [{'Date': datetime(2023, 1, 15), 'Amount': 25.50, 'Category': 'Food', 'Description': 'Lunch'}]
```

#### `display_expenses(expenses)`

**Description:** Prints all expenses in a formatted table to the console.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** None

**Output Format:**
```
=== All Expenses ===
2023-01-15 - $25.50 - Food - Lunch
2023-01-16 - $45.00 - Transportation - Gas
```

**Example:**
```python
display_expenses(expenses)
```

#### `count_expenses(expenses)`

**Description:** Returns the total number of expenses.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** `int` - Total count of expenses

**Example:**
```python
total_count = count_expenses(expenses)
print(f"Total expenses: {total_count}")
```

#### `total_spent(expenses)`

**Description:** Calculates the total amount spent across all expenses.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** `float` - Total amount spent

**Example:**
```python
total = total_spent(expenses)
print(f"Total spent: ${total:.2f}")
```

#### `most_common_category(expenses)`

**Description:** Finds the most frequently occurring expense category.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** `tuple` - (category_name, count) of the most common category

**Example:**
```python
category, count = most_common_category(expenses)
print(f"Most common category: {category} ({count} entries)")
```

#### `total_per_month(expenses)`

**Description:** Calculates total spending for each month.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** `defaultdict` - Dictionary with month keys (YYYY-MM format) and total amounts as values

**Example:**
```python
monthly_totals = total_per_month(expenses)
for month, total in monthly_totals.items():
    print(f"{month}: ${total:.2f}")
```

#### `most_expensive_month(month_totals)`

**Description:** Finds the month with the highest total spending.

**Parameters:**
- `month_totals` (defaultdict): Dictionary of monthly totals from `total_per_month()`

**Returns:** `tuple` - (month, total_amount) of the most expensive month

**Example:**
```python
monthly_totals = total_per_month(expenses)
most_exp_month, most_exp_total = most_expensive_month(monthly_totals)
print(f"Most expensive month: {most_exp_month} (${most_exp_total:.2f})")
```

#### `average_expense(expenses)`

**Description:** Calculates the average amount per expense.

**Parameters:**
- `expenses` (list[dict]): List of expense dictionaries

**Returns:** `float` - Average expense amount (0 if no expenses)

**Example:**
```python
avg = average_expense(expenses)
print(f"Average expense: ${avg:.2f}")
```

---

## Global Functions

### `save_to_csv(data, file_path)`

**Description:** Saves data to a CSV file in append mode.

**Parameters:**
- `data` (list): List of rows to write to CSV
- `file_path` (str): Path to the CSV file

**Returns:** None

**Side Effects:**
- Opens file in append mode ('a')
- Writes each row from the data list

**Example:**
```python
data = [["Result for addition: "], [25]]
save_to_csv(data, 'Calculations.csv')
```

### `read_csv(file_path)`

**Description:** Reads and prints all rows from a CSV file.

**Parameters:**
- `file_path` (str): Path to the CSV file to read

**Returns:** None

**Side Effects:**
- Prints each row to console

**Example:**
```python
read_csv('Calculations.csv')
```

---

## File Formats

### Calculations.csv
Stores calculator operation history with the following format:
```
Calculation Results
Timestamp: 2023-12-01 10:30:45

Result for addition: 
30

Result for subtraction: 
-13
```

### expenses.csv
Expected format for expense data:
```csv
Date,Amount,Category,Description
2023-01-15,25.50,Food,Lunch
2023-01-16,45.00,Transportation,Gas
2023-01-17,120.00,Shopping,Groceries
```

---

## Usage Examples

### Calculator Usage
```python
from Calculator import Calculator

# Initialize calculator
calc = Calculator()

# Perform calculations
calc.add(10, 20, 30)      # Result: 60
calc.subtract(15)          # Result: 45
calc.multiply(2, 3)        # Result: 270
calc.divide(3)             # Result: 90

# View history
read_csv('Calculations.csv')
```

### Expense Tracker Usage
```python
from Expense_tracker import load_expenses, display_expenses, total_spent

# Load and analyze expenses
expenses = load_expenses('expenses.csv')
display_expenses(expenses)

# Get summary statistics
total = total_spent(expenses)
print(f"Total spent: ${total:.2f}")

# Monthly analysis
monthly_totals = total_per_month(expenses)
for month, total in sorted(monthly_totals.items()):
    print(f"{month}: ${total:.2f}")
```

---

## Error Handling

### Calculator Module
- **Division by Zero**: `ValueError` is raised when attempting to divide by zero
- **File Operations**: Gracefully handles existing files during initialization

### Expense Tracker Module
- **File Not Found**: Assumes expenses.csv exists with proper format
- **Data Conversion**: Converts amounts to float and dates to datetime objects
- **Empty Data**: Returns 0 for average calculation when no expenses exist

---

## Dependencies

### Required Python Modules
- `csv`: For CSV file operations
- `time`: For timestamp operations
- `datetime`: For date/time handling
- `collections.defaultdict`: For monthly totals calculation
- `collections.Counter`: For category frequency counting

### External Files
- `Calculations.csv`: Stores calculator history
- `expenses.csv`: Stores expense data (must exist with proper format)

---

## Notes

1. **Calculator State**: The Calculator class maintains state through the `result` attribute
2. **File Persistence**: Both modules save data to CSV files for persistence
3. **Data Validation**: Limited validation is performed; ensure proper data formats
4. **Error Recovery**: Calculator continues operation even if file operations fail
5. **Performance**: All operations are O(n) where n is the number of expenses/calculations