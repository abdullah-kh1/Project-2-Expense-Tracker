# Project 2: Expense Tracker (Python)

A command-line Expense Tracker built with Python. You enter expense amounts one by one (for example 100, 50, 20), and the program adds them up and shows the **Total Spent**. When you are finished, type `quit` to see the final total.

Built as part of the **DecodeLabs Python Programming - Industrial Training Kit (Batch 2026)**.

## Features

- Enter as many expenses as you want (there is no fixed limit)
- Shows a running total after every expense
- Accepts decimal amounts (for example `75.50`)
- Rejects invalid data without crashing: text (`ten`), empty input, zero, negative numbers, and values like `nan` or `inf`
- Type `quit` (any capitalization) to stop and see the final total and the number of transactions

## Concepts used

- **Accumulator pattern:** the total keeps growing as new expenses are added (`total = total + new_expense`)
- `total` is created **outside** the loop, so it is never reset by mistake
- `while True` loop with a **sentinel value** (`quit`) as the kill switch
- **Defensive coding:** `float()` inside `try / except ValueError` so bad input never reaches the math
- Input -> Process -> Output structure, with the calculation logic kept separate from the screen (input/print) code
- f-strings for formatted output (for example `$1,260.50`)
- `if __name__ == "__main__":` guard

## How to run

You need Python 3 installed.

```
python expense_tracker.py
```

## Example output

```
========================================
         EXPENSE TRACKER
========================================
Enter an expense amount (e.g. 100, 50, 20).
Type 'quit' when you are finished.

Enter expense: 100
  Added $100.00 | Running total: $100.00
Enter expense: 50
  Added $50.00 | Running total: $150.00
Enter expense: ten
Invalid Data - please enter a positive number (or 'quit' to finish).
Enter expense: 20
  Added $20.00 | Running total: $170.00
Enter expense: quit

----------------------------------------
Transactions recorded: 3
FINAL TOTAL: $170.00
----------------------------------------
```

## Project structure

```
project2/
├── expense_tracker.py   # the program
└── README.md            # this file
```
