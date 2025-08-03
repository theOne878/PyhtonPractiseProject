# Python Practice Project

A collection of Python practice projects demonstrating basic programming concepts and data analysis.

## Projects

### 1. Personal Expense Tracker
- **File**: `Expense_tracker.py`
- **Features**:
  - Read expenses from CSV files
  - Calculate totals by category
  - Generate monthly reports
  - Analyze spending patterns
  - Track budget and savings

### 2. Simple Calculator with History
- **File**: `Calculator.py`
- **Features**:
  - Basic mathematical operations (add, subtract, multiply, divide)
  - Save calculation history to CSV file
  - Load and display previous sessions
  - Error handling for division by zero

## Documentation

### 📚 Comprehensive Documentation
- **[API Documentation](API_DOCUMENTATION.md)** - Complete reference for all public APIs, functions, and components
- **[Usage Guide](USAGE_GUIDE.md)** - Step-by-step instructions and practical examples
- **[Test Examples](test_examples.py)** - Comprehensive test suite demonstrating all functionality

### 📖 Quick Start

#### Calculator Usage
```python
from Calculator import Calculator

calc = Calculator()
calc.add(10, 20, 30)      # Result: 60
calc.subtract(15)          # Result: 45
calc.multiply(2, 3)        # Result: 270
calc.divide(3)             # Result: 90
```

#### Expense Tracker Usage
```python
from Expense_tracker import load_expenses, total_spent

expenses = load_expenses('expenses.csv')
total = total_spent(expenses)
print(f"Total spent: ${total:.2f}")
```

## File Structure
```
project/
├── Calculator.py              # Calculator with history
├── Expense_tracker.py         # Expense analysis tool
├── expenses.csv              # Sample expense data
├── API_DOCUMENTATION.md      # Complete API reference
├── USAGE_GUIDE.md           # Practical usage guide
├── test_examples.py         # Comprehensive test suite
└── README.md                # This file
```

## Features

### Calculator Module
- ✅ Basic arithmetic operations
- ✅ Calculation history persistence
- ✅ Error handling (division by zero)
- ✅ CSV file storage
- ✅ Session management

### Expense Tracker Module
- ✅ CSV data loading and parsing
- ✅ Expense categorization and analysis
- ✅ Monthly spending reports
- ✅ Category-based statistics
- ✅ Budget tracking capabilities
- ✅ Spending pattern analysis

## Getting Started

1. **Prerequisites**: Python 3.6 or higher
2. **Dependencies**: Built-in modules only (`csv`, `datetime`, `collections`)
3. **Data Format**: See `expenses.csv` for expected format

## Running Tests

Execute the comprehensive test suite:
```bash
python test_examples.py
```

This will test all public APIs and demonstrate functionality.

## API Reference

### Calculator Class
- `__init__()` - Initialize calculator and setup CSV file
- `add(*args)` - Add multiple numbers
- `subtract(*args)` - Subtract multiple numbers
- `multiply(*args)` - Multiply by multiple numbers
- `divide(*args)` - Divide by multiple numbers

### Expense Tracker Functions
- `load_expenses(file_path)` - Load expense data from CSV
- `display_expenses(expenses)` - Display formatted expense list
- `count_expenses(expenses)` - Count total expenses
- `total_spent(expenses)` - Calculate total amount spent
- `most_common_category(expenses)` - Find most frequent category
- `total_per_month(expenses)` - Calculate monthly totals
- `most_expensive_month(month_totals)` - Find highest spending month
- `average_expense(expenses)` - Calculate average expense amount

## Examples

### Financial Planning
```python
from Calculator import Calculator
from Expense_tracker import load_expenses, total_spent

# Load expenses and calculate savings
expenses = load_expenses('expenses.csv')
total_expenses = total_spent(expenses)

calc = Calculator()
income = 3000
calc.add(income)
calc.subtract(total_expenses)

savings = calc.result
print(f"Monthly savings: ${savings:.2f}")
```

### Budget Analysis
```python
from Expense_tracker import load_expenses, total_spent

expenses = load_expenses('expenses.csv')
total = total_spent(expenses)
budget = 1000

if total > budget:
    print("⚠️  Over budget!")
else:
    print("✅ Within budget")
```

## Error Handling

- **Division by Zero**: Calculator raises `ValueError`
- **File Not Found**: Expense tracker assumes proper CSV format
- **Data Validation**: Automatic type conversion with error handling

## Performance Notes

- All operations are O(n) where n is the number of expenses/calculations
- Calculator maintains state through session
- Expense tracker loads all data into memory
- CSV files provide persistent storage

## Contributing

Feel free to extend the functionality:
- Add new mathematical operations to Calculator
- Implement additional expense analysis features
- Create new data visualization capabilities
- Add unit tests for specific functions

## License

This is a practice project for educational purposes.
