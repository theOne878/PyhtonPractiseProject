# Python Practice Project
### *Practice Projects:*
1. *Personal Expense Tracker*
   - Read expenses from CSV
   - Calculate totals by category
   - Generate monthly reports
   
2. *Simple Calculator with History*
   - Basic math operations
   - Save calculation history to file
   - Load previous sessions

## 📚 Documentation

- **[📚 Documentation Index](DOCUMENTATION_INDEX.md)** - Start here! Complete guide to all documentation
- **[📋 API Documentation](API_DOCUMENTATION.md)** - Comprehensive documentation for all public APIs, functions, and components
- **[⚡ Quick Reference](QUICK_REFERENCE.md)** - Quick lookup guide for function signatures and common usage patterns
- **[🛠️ Examples](examples.py)** - Practical examples demonstrating all APIs with real-world usage scenarios

## 🚀 Quick Start

1. **Calculator Usage:**
   ```python
   from Calculator import Calculator
   calc = Calculator()
   calc.add(10, 5)
   calc.multiply(2)
   print(calc.result)  # Output: 30
   ```

2. **Expense Tracker Usage:**
   ```python
   from Expense_tracker import load_expenses, total_spent
   expenses = load_expenses("sample_expenses.csv")
   total = total_spent(expenses)
   print(f"Total spent: ${total:.2f}")
   ```

3. **Run Examples:**
   ```bash
   python examples.py
   ```

## 📁 Files

- `Calculator.py` - Calculator module with persistent history
- `Expense_tracker.py` - Expense analysis and reporting module  
- `sample_expenses.csv` - Sample expense data for testing
- `examples.py` - Comprehensive usage examples
