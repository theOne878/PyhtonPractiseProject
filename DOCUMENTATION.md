# Project Documentation

Welcome to the **Python Practise Project** repository. This project contains two independent Python modules:

1. **Expense Tracker** – Analyse and report personal expenses from a CSV file.
2. **Simple Calculator** – Perform basic arithmetic operations while automatically persisting a history of results.

This document serves as the single source of truth for all public APIs, functions, and components exposed by each module. Short runnable examples are included so you can quickly get started.

---

## Table of Contents

1. [Calculator Module](#calculator-module)
   * [Overview](#calculator-overview)
   * [Installation](#calculator-installation)
   * [Quick-start](#calculator-quick-start)
   * [Public API](#calculator-public-api)
   * [CSV Output Format](#calculator-csv-output-format)
2. [Expense Tracker Module](#expense-tracker-module)
   * [Overview](#expense-tracker-overview)
   * [Installation](#expense-tracker-installation)
   * [Quick-start](#expense-tracker-quick-start)
   * [Public API](#expense-tracker-public-api)
   * [Expected CSV Schema](#expense-tracker-expected-csv-schema)

---

## Calculator Module <a name="calculator-module"></a>

### Overview <a name="calculator-overview"></a>
`Calculator.py` provides an interactive, state-ful calculator that supports addition, subtraction, multiplication and division across an **arbitrary number of operands**. Results are stored between runs in a CSV file (`Calculations.csv`) so you always have a historical record of your calculations.

Key design points:

* State is kept inside the `Calculator` instance via the `result` attribute.
* All arithmetic methods (`add`, `subtract`, `multiply`, `divide`) accept **variadic positional arguments** (`*args`).
* Every time an arithmetic method is called, the new result is automatically appended to `Calculations.csv` together with a one-line header describing the operation.
* A simple CLI demo is executed when you run `Calculator.py` directly.

### Installation <a name="calculator-installation"></a>
```bash
# 1. Clone this repository (if you haven’t already)
$ git clone <repo-url> && cd <repo-dir>

# 2. (Recommended) Create a virtual environment
$ python -m venv .venv && source .venv/bin/activate

# 3. Install runtime dependencies – only the standard library is required
$ # Nothing to install 🎉
```

### Quick-start <a name="calculator-quick-start"></a>
Run the demo script:
```bash
$ python Calculator.py
```
Expected output (shortened):
```
Calculator initialized. Ready for calculations.
Previous results saved in Calculations.csv
['Calculation Results']
['Timestamp: 2024-05-23 14:02:15']
...
```

Or embed the module in your own code:
```python
from Calculator import Calculator

calc = Calculator()
calc.add(2, 3)
print(calc.result)   # 5

calc.multiply(4)
print(calc.result)   # 20

calc.divide(2)
print(calc.result)   # 10
```

### Public API <a name="calculator-public-api"></a>

| Function / Method | Signature | Description |
|-------------------|-----------|-------------|
| `save_to_csv` | `save_to_csv(data: list[list[Any]], file_path: str)` | Helper: Append an iterable of rows (`list[list]`) to the CSV file at `file_path`. Each inner list represents one row. |
| `read_csv` | `read_csv(file_path: str)` | Helper: Stream the entire CSV file to `stdout`. Useful for quickly inspecting saved calculations. |
| `Calculator.__init__` | `Calculator()` | Create a new calculator instance. A CSV file is created on first run and re-used on subsequent runs. Initial `result` is `0`. |
| `Calculator.add` | `add(*args: float | int)` | Add all supplied operands to `result`. Accepts 1-N operands. Returns `None`. |
| `Calculator.subtract` | `subtract(*args: float | int)` | Subtract all supplied operands from `result`. |
| `Calculator.multiply` | `multiply(*args: float | int)` | Multiply `result` by all supplied operands in order. If `result` is `0`, it is reset to `1` before multiplication so results are mathematically correct. |
| `Calculator.divide` | `divide(*args: float | int)` | Divide `result` by all supplied operands in order. Raises `ValueError` on divide-by-zero. |

All arithmetic methods mutate `self.result` **in place** and persist the new value to `Calculations.csv`.

### CSV Output Format <a name="calculator-csv-output-format"></a>
Example excerpt:
```csv
Calculation Results
Timestamp: 2024-05-23 14:02:15

Result for addition:
8
Result for subtraction:
-5
...
```
Each pair of header and value is written on separate lines, allowing simple parsing or manual inspection.

---

## Expense Tracker Module <a name="expense-tracker-module"></a>

### Overview <a name="expense-tracker-overview"></a>
`Expense_tracker.py` analyses a personal expenses CSV and prints a concise report: total items, total spend, most common categories, per-month totals and averages.

Design highlights:

* Parsing is performed with `csv.DictReader` into a list of dictionaries (`expenses`).
* All currency values are coerced to `float` and dates to `datetime` for accurate computations.
* Stand-alone helper functions make the logic reusable from other scripts or interactive sessions.

### Installation <a name="expense-tracker-installation"></a>
No external dependencies beyond the Python standard library – see the Calculator installation steps.

### Quick-start <a name="expense-tracker-quick-start"></a>
1. Prepare a CSV file named `expenses.csv` in the project root. See [Expected CSV Schema](#expense-tracker-expected-csv-schema).
2. Execute:
```bash
$ python Expense_tracker.py
```
Sample output:
```
=== All Expenses ===
2024-05-01 - $ 15.50 - Grocery - Milk & Bread
...
🧾 Total number of expenses: 42
💸 Total amount spent: $1234.56
📊 Most frequent category: Grocery (18 entries)
🗓️ Total spent per month:
  2024-04: $200.00
  2024-05: $350.00
...
💥 Most expensive month: 2024-05 ($350.00)
📉 Average expense amount: $29.39
```

### Public API <a name="expense-tracker-public-api"></a>

| Function | Signature | Description |
|----------|-----------|-------------|
| `load_expenses` | `load_expenses(file_path: str) -> list[dict]` | Read CSV into list of dicts with parsed types. |
| `display_expenses` | `display_expenses(expenses: list[dict]) -> None` | Pretty-print each expense row. |
| `count_expenses` | `count_expenses(expenses: list[dict]) -> int` | Return total number of expense entries. |
| `total_spent` | `total_spent(expenses: list[dict]) -> float` | Sum of `Amount` across all expenses. |
| `most_common_category` | `most_common_category(expenses: list[dict]) -> tuple[str, int]` | The category with the highest occurrence and its count. |
| `total_per_month` | `total_per_month(expenses: list[dict]) -> dict[str, float]` | Mapping `YYYY-MM → total spent in that month`. |
| `most_expensive_month` | `most_expensive_month(month_totals: dict[str, float]) -> tuple[str, float]` | Month with highest spending. |
| `average_expense` | `average_expense(expenses: list[dict]) -> float` | Mean amount spent per entry. |

Each helper function is **pure** (no side effects) except `display_expenses`, which prints directly to `stdout`.

### Expected CSV Schema <a name="expense-tracker-expected-csv-schema"></a>
The input file **must** contain a header row with the following columns (case-sensitive):

| Column     | Type   | Example        |
|------------|--------|----------------|
| `Date`     | `YYYY-MM-DD` | `2024-05-01` |
| `Amount`   | `float`      | `15.50`      |
| `Category` | `str`        | `Grocery`    |
| `Description` | `str`     | `Milk & Bread` |

---

## Contributing
Pull requests are welcome! If you add new modules or extend existing ones, please remember to update this documentation accordingly.

## License
MIT