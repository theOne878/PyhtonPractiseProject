#!/usr/bin/env python3
"""
Comprehensive Test Examples for Python Practice Project

This file demonstrates all the functionality of both the Calculator and Expense Tracker modules.
It serves as both documentation and testing for all public APIs.
"""

import os
import sys
from datetime import datetime

# Import our modules
from Calculator import Calculator, save_to_csv, read_csv
from Expense_tracker import (
    load_expenses, display_expenses, count_expenses, total_spent,
    most_common_category, total_per_month, most_expensive_month, average_expense
)

def test_calculator_basic_operations():
    """Test basic calculator operations"""
    print("=== Testing Basic Calculator Operations ===")
    
    calc = Calculator()
    
    # Test addition
    calc.add(10, 20, 30)
    print(f"Addition result: {calc.result}")
    
    # Test subtraction
    calc.subtract(15)
    print(f"Subtraction result: {calc.result}")
    
    # Test multiplication
    calc.multiply(2, 3)
    print(f"Multiplication result: {calc.result}")
    
    # Test division
    calc.divide(3)
    print(f"Division result: {calc.result}")
    
    print("✅ Basic calculator operations completed\n")

def test_calculator_error_handling():
    """Test calculator error handling"""
    print("=== Testing Calculator Error Handling ===")
    
    calc = Calculator()
    calc.add(10)
    
    # Test division by zero
    try:
        calc.divide(0)
        print("❌ Should have raised ValueError")
    except ValueError as e:
        print(f"✅ Correctly caught division by zero: {e}")
    
    print("✅ Calculator error handling completed\n")

def test_expense_tracker_basic():
    """Test basic expense tracker functionality"""
    print("=== Testing Basic Expense Tracker ===")
    
    # Load expenses
    expenses = load_expenses('expenses.csv')
    print(f"Loaded {len(expenses)} expenses")
    
    # Display expenses
    display_expenses(expenses)
    
    # Basic statistics
    total_count = count_expenses(expenses)
    total_amount = total_spent(expenses)
    avg_amount = average_expense(expenses)
    
    print(f"Total expenses: {total_count}")
    print(f"Total spent: ${total_amount:.2f}")
    print(f"Average expense: ${avg_amount:.2f}")
    
    print("✅ Basic expense tracker completed\n")

def test_expense_tracker_advanced():
    """Test advanced expense tracker functionality"""
    print("=== Testing Advanced Expense Tracker ===")
    
    expenses = load_expenses('expenses.csv')
    
    # Most common category
    category, count = most_common_category(expenses)
    print(f"Most common category: {category} ({count} entries)")
    
    # Monthly analysis
    monthly_totals = total_per_month(expenses)
    print("\nMonthly spending:")
    for month, total in sorted(monthly_totals.items()):
        print(f"  {month}: ${total:.2f}")
    
    # Most expensive month
    most_exp_month, most_exp_total = most_expensive_month(monthly_totals)
    print(f"\nMost expensive month: {most_exp_month} (${most_exp_total:.2f})")
    
    print("✅ Advanced expense tracker completed\n")

def test_custom_analysis():
    """Test custom expense analysis"""
    print("=== Testing Custom Expense Analysis ===")
    
    expenses = load_expenses('expenses.csv')
    
    # Category analysis
    from collections import defaultdict
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense['Category']] += expense['Amount']
    
    print("Spending by category:")
    for category, total in sorted(category_totals.items()):
        percentage = (total / sum(category_totals.values())) * 100
        print(f"  {category}: ${total:.2f} ({percentage:.1f}%)")
    
    # Day of week analysis
    day_totals = defaultdict(float)
    for expense in expenses:
        day = expense['Date'].strftime('%A')
        day_totals[day] += expense['Amount']
    
    print("\nSpending by day of week:")
    for day, total in sorted(day_totals.items()):
        print(f"  {day}: ${total:.2f}")
    
    print("✅ Custom analysis completed\n")

def test_combined_functionality():
    """Test combined calculator and expense tracker"""
    print("=== Testing Combined Functionality ===")
    
    # Load expenses
    expenses = load_expenses('expenses.csv')
    total_expenses = total_spent(expenses)
    
    # Use calculator for financial planning
    calc = Calculator()
    
    # Calculate savings potential
    income = 3000
    calc.add(income)
    calc.subtract(total_expenses)
    
    savings_potential = calc.result
    savings_percentage = (savings_potential / income) * 100
    
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Potential Savings: ${savings_potential:.2f}")
    print(f"Savings Rate: {savings_percentage:.1f}%")
    
    # Budget analysis
    monthly_budget = 1000
    budget_remaining = monthly_budget - total_expenses
    budget_percentage = (total_expenses / monthly_budget) * 100
    
    print(f"\nBudget Analysis:")
    print(f"Monthly Budget: ${monthly_budget:.2f}")
    print(f"Budget Used: {budget_percentage:.1f}%")
    
    if budget_remaining < 0:
        print("⚠️  Over budget!")
    elif budget_percentage > 80:
        print("⚠️  Close to budget limit")
    else:
        print("✅ Within budget")
    
    print("✅ Combined functionality completed\n")

def test_file_operations():
    """Test file operations"""
    print("=== Testing File Operations ===")
    
    # Test CSV reading
    print("Reading calculator history:")
    read_csv('Calculations.csv')
    
    # Test CSV writing
    test_data = [["Test Entry"], [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]]
    save_to_csv(test_data, 'test_output.csv')
    print("✅ Test data written to test_output.csv")
    
    # Clean up test file
    if os.path.exists('test_output.csv'):
        os.remove('test_output.csv')
        print("✅ Test file cleaned up")
    
    print("✅ File operations completed\n")

def test_performance_metrics():
    """Test performance and metrics"""
    print("=== Testing Performance Metrics ===")
    
    expenses = load_expenses('expenses.csv')
    
    # Calculate various metrics
    total_expenses = total_spent(expenses)
    avg_expense = average_expense(expenses)
    expense_count = count_expenses(expenses)
    
    # Calculate efficiency metrics
    if expense_count > 0:
        efficiency_score = (total_expenses / expense_count) / avg_expense
        print(f"Efficiency Score: {efficiency_score:.2f}")
    
    # Spending patterns
    categories = [e['Category'] for e in expenses]
    unique_categories = len(set(categories))
    print(f"Unique categories: {unique_categories}")
    
    # Date range
    dates = [e['Date'] for e in expenses]
    if dates:
        date_range = max(dates) - min(dates)
        print(f"Date range: {date_range.days} days")
    
    print("✅ Performance metrics completed\n")

def run_all_tests():
    """Run all test functions"""
    print("🚀 Starting Comprehensive API Tests\n")
    
    try:
        test_calculator_basic_operations()
        test_calculator_error_handling()
        test_expense_tracker_basic()
        test_expense_tracker_advanced()
        test_custom_analysis()
        test_combined_functionality()
        test_file_operations()
        test_performance_metrics()
        
        print("🎉 All tests completed successfully!")
        print("\n📋 Summary:")
        print("- Calculator: Basic operations, error handling")
        print("- Expense Tracker: Loading, analysis, statistics")
        print("- Combined: Financial planning, budget analysis")
        print("- File Operations: CSV reading/writing")
        print("- Performance: Metrics and efficiency calculations")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    # Check if expenses.csv exists
    if not os.path.exists('expenses.csv'):
        print("❌ expenses.csv not found. Please ensure the file exists.")
        sys.exit(1)
    
    # Run all tests
    success = run_all_tests()
    
    if success:
        print("\n✅ All APIs are working correctly!")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")
        sys.exit(1)