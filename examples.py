#!/usr/bin/env python3
"""
Example usage scripts for Calculator and Expense Tracker modules.
This file demonstrates all public APIs with practical examples.
"""

def calculator_examples():
    """Demonstrate Calculator class usage with various scenarios."""
    print("=" * 50)
    print("CALCULATOR EXAMPLES")
    print("=" * 50)
    
    # Import the Calculator class
    from Calculator import Calculator, read_csv
    
    # Example 1: Basic calculator operations
    print("\n1. Basic Calculator Operations:")
    calc = Calculator()
    
    # Chain of operations
    calc.add(50, 25)          # result = 75
    print(f"After adding 50 + 25: {calc.result}")
    
    calc.subtract(10, 5)      # result = 75 - 10 - 5 = 60
    print(f"After subtracting 10 and 5: {calc.result}")
    
    calc.multiply(2)          # result = 60 * 2 = 120
    print(f"After multiplying by 2: {calc.result}")
    
    calc.divide(4)            # result = 120 / 4 = 30
    print(f"After dividing by 4: {calc.result}")
    
    # Example 2: Multiple arguments
    print("\n2. Multiple Arguments:")
    calc2 = Calculator()
    calc2.add(10, 20, 30, 40)  # 100
    print(f"Adding multiple numbers (10+20+30+40): {calc2.result}")
    
    # Example 3: Error handling
    print("\n3. Error Handling:")
    calc3 = Calculator()
    calc3.add(100)
    try:
        calc3.divide(5, 0, 2)  # This will raise an error
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print(f"Result unchanged after error: {calc3.result}")
    
    # Example 4: Reading calculation history
    print("\n4. Reading Calculation History:")
    print("Recent calculations from CSV:")
    try:
        read_csv("Calculations.csv")
    except FileNotFoundError:
        print("No calculation history found.")


def expense_tracker_examples():
    """Demonstrate Expense Tracker functions with sample data."""
    print("\n" + "=" * 50)
    print("EXPENSE TRACKER EXAMPLES")
    print("=" * 50)
    
    # Import expense tracker functions
    from Expense_tracker import (
        load_expenses, display_expenses, count_expenses, total_spent,
        most_common_category, total_per_month, most_expensive_month, average_expense
    )
    
    try:
        # Load expenses from sample file
        expenses = load_expenses("sample_expenses.csv")
        
        # Example 1: Basic expense information
        print("\n1. Basic Expense Statistics:")
        print(f"📊 Total number of expenses: {count_expenses(expenses)}")
        print(f"💰 Total amount spent: ${total_spent(expenses):.2f}")
        print(f"📈 Average expense: ${average_expense(expenses):.2f}")
        
        # Example 2: Category analysis
        print("\n2. Category Analysis:")
        category, count = most_common_category(expenses)
        print(f"🏆 Most frequent category: {category} ({count} transactions)")
        
        # Example 3: Monthly breakdown
        print("\n3. Monthly Spending Breakdown:")
        monthly_totals = total_per_month(expenses)
        print("📅 Monthly totals:")
        for month, total in sorted(monthly_totals.items()):
            print(f"   {month}: ${total:.2f}")
        
        # Find the most expensive month
        most_exp_month, most_exp_total = most_expensive_month(monthly_totals)
        print(f"\n💥 Highest spending month: {most_exp_month} (${most_exp_total:.2f})")
        
        # Example 4: Display first 5 expenses
        print("\n4. Sample Expense Entries (first 5):")
        sample_expenses = expenses[:5]  # First 5 expenses
        for i, expense in enumerate(sample_expenses, 1):
            print(f"   {i}. {expense['Date'].strftime('%Y-%m-%d')} - "
                  f"${expense['Amount']:.2f} - {expense['Category']} - "
                  f"{expense['Description']}")
        
        # Example 5: Category-specific analysis
        print("\n5. Category-Specific Analysis:")
        categories = {}
        for expense in expenses:
            cat = expense['Category']
            if cat not in categories:
                categories[cat] = {'count': 0, 'total': 0}
            categories[cat]['count'] += 1
            categories[cat]['total'] += expense['Amount']
        
        print("📋 Spending by category:")
        for category, data in sorted(categories.items(), 
                                   key=lambda x: x[1]['total'], reverse=True):
            avg_per_transaction = data['total'] / data['count']
            print(f"   {category}: ${data['total']:.2f} "
                  f"({data['count']} transactions, "
                  f"avg: ${avg_per_transaction:.2f})")
                  
    except FileNotFoundError:
        print("❌ Sample expenses file not found!")
        print("💡 Create a 'sample_expenses.csv' file or use 'expenses.csv'")
        print("   with the following format:")
        print("   Date,Amount,Category,Description")
        print("   2024-01-15,25.99,Food,Lunch")


def advanced_examples():
    """Show advanced usage patterns and integration examples."""
    print("\n" + "=" * 50)
    print("ADVANCED USAGE EXAMPLES")
    print("=" * 50)
    
    # Example 1: Custom expense analysis
    print("\n1. Custom Expense Analysis Functions:")
    
    def analyze_spending_trends(expenses):
        """Custom function to analyze spending trends."""
        from collections import defaultdict
        
        daily_spending = defaultdict(float)
        for expense in expenses:
            day = expense['Date'].strftime('%Y-%m-%d')
            daily_spending[day] += expense['Amount']
        
        # Find highest and lowest spending days
        if daily_spending:
            max_day = max(daily_spending.items(), key=lambda x: x[1])
            min_day = min(daily_spending.items(), key=lambda x: x[1])
            
            print(f"   📈 Highest spending day: {max_day[0]} (${max_day[1]:.2f})")
            print(f"   📉 Lowest spending day: {min_day[0]} (${min_day[1]:.2f})")
            
            # Calculate average daily spending
            avg_daily = sum(daily_spending.values()) / len(daily_spending)
            print(f"   📊 Average daily spending: ${avg_daily:.2f}")
    
    # Example 2: Calculator with expense integration
    print("\n2. Calculator + Expense Integration:")
    
    def calculate_monthly_budget(expenses, target_savings=500):
        """Calculate if monthly spending fits within budget."""
        from Calculator import Calculator
        from Expense_tracker import total_per_month
        
        calc = Calculator()
        monthly_totals = total_per_month(expenses)
        
        print(f"   🎯 Target monthly savings: ${target_savings}")
        print("   💰 Budget analysis by month:")
        
        for month, spending in sorted(monthly_totals.items()):
            # Assume monthly income of $3000 for example
            monthly_income = 3000
            calc.result = monthly_income  # Reset calculator
            calc.subtract(spending)  # Subtract expenses
            calc.subtract(target_savings)  # Subtract target savings
            
            remaining = calc.result
            status = "✅ Within budget" if remaining >= 0 else "❌ Over budget"
            print(f"      {month}: ${remaining:.2f} remaining ({status})")
    
    # Try to run advanced examples if data is available
    try:
        from Expense_tracker import load_expenses
        expenses = load_expenses("sample_expenses.csv")
        
        analyze_spending_trends(expenses)
        calculate_monthly_budget(expenses)
        
    except (FileNotFoundError, ImportError) as e:
        print(f"   ⚠️ Advanced examples require sample data: {e}")
    
    # Example 3: Error handling best practices
    print("\n3. Error Handling Best Practices:")
    
    def safe_expense_analysis(file_path):
        """Demonstrate proper error handling for expense analysis."""
        try:
            from Expense_tracker import load_expenses, total_spent
            
            expenses = load_expenses(file_path)
            total = total_spent(expenses)
            print(f"   ✅ Successfully analyzed {len(expenses)} expenses")
            print(f"   💰 Total spending: ${total:.2f}")
            
        except FileNotFoundError:
            print(f"   ❌ File '{file_path}' not found")
            print("   💡 Make sure the CSV file exists in the current directory")
            
        except ValueError as e:
            print(f"   ❌ Data format error: {e}")
            print("   💡 Check that dates are in YYYY-MM-DD format")
            print("   💡 Check that amounts are valid numbers")
            
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")
    
    # Test with both existing and non-existing files
    safe_expense_analysis("sample_expenses.csv")
    safe_expense_analysis("nonexistent_file.csv")


def main():
    """Run all example demonstrations."""
    print("🐍 Python Practice Project - API Examples")
    print("This script demonstrates all public APIs with practical examples.")
    
    # Run calculator examples
    calculator_examples()
    
    # Run expense tracker examples  
    expense_tracker_examples()
    
    # Run advanced examples
    advanced_examples()
    
    print("\n" + "=" * 50)
    print("✨ Examples completed!")
    print("📚 Check API_DOCUMENTATION.md for detailed API reference")
    print("⚡ Check QUICK_REFERENCE.md for quick function lookup")
    print("=" * 50)


if __name__ == "__main__":
    main()