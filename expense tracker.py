"""
Project 2: The Expense Tracker
DecodeLabs - Python Programming (Industrial Training Kit, Batch 2026)

Goal : The user enters expense amounts (e.g. 100, 50, 20). The program adds
       them up and displays the Total Spent.
Skill: Math operations and Accumulators  ->  total = total + new_expense

IPO model used in this program:
    Input   -> the Gatekeeper: raw text from input() is converted with
               float() inside try/except so bad data never reaches the math
    Process -> the Engine: the accumulator adds each valid expense to total
    Output  -> the Display: the final total is shown, e.g. FINAL TOTAL: $150.00

Quality checklist (The Quality Standard slide):
    [x] Stability : handles 5+ transactions (the loop has no fixed limit)
    [x] State     : "total" is initialized OUTSIDE the loop
    [x] Defense   : "ValueError" is caught on every input
    [x] Control   : the kill switch ("quit") prints the final total
"""

import math

SENTINEL = "quit"  # the Kill Switch value that stops the loop


# ---------------------------------------------------------------
# MODEL (logic) - no print() and no input() in here
# ---------------------------------------------------------------
def parse_expense(raw_text):
    """
    PHASE 1 - THE GATEKEEPER
    Convert raw text (a string like "100") into a number (100.0).
    Raises ValueError for anything that is not a valid expense, so the
    caller can catch it. '100' + '50' = '10050' (disaster), but
    float('100') + float('50') = 150.0 (truth).
    """
    amount = float(raw_text)  # raises ValueError for "ten", "", "5$", etc.
    if not math.isfinite(amount):  # float() also accepts "nan" and "inf"
        raise ValueError("amount must be a real number")
    if amount <= 0:
        raise ValueError("amount must be greater than zero")
    return amount


def add_expense(total, new_expense):
    """
    PHASE 2 - THE ENGINE (Accumulator Pattern)
    State(new) = State(old) + Input
    """
    return total + new_expense


def format_total(total):
    """PHASE 3 - turn the number into display text, e.g. $150.00"""
    return f"${total:,.2f}"


# ---------------------------------------------------------------
# VIEW (display) - only deals with input() and print()
# ---------------------------------------------------------------
def main():
    # STATE: initialized OUTSIDE the loop so it is never reset to 0
    # (if it were inside the loop, the program would forget every
    # previous expense on each pass - "amnesia").
    total = 0.0
    count = 0

    print("=" * 40)
    print("         EXPENSE TRACKER")
    print("=" * 40)
    print("Enter an expense amount (e.g. 100, 50, 20).")
    print(f"Type '{SENTINEL}' when you are finished.\n")

    while True:  # the continuous audit loop
        try:
            raw = input("Enter expense: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Ctrl+D / Ctrl+C: still shut down gracefully with the total
            print()
            break

        # KILL SWITCH: the sentinel value ends the loop gracefully
        if raw.lower() == SENTINEL:
            break

        # DEFENSE: the Digital Poka-Yoke
        try:
            new_expense = parse_expense(raw)
        except ValueError:
            print("Invalid Data - please enter a positive number "
                  f"(or '{SENTINEL}' to finish).")
            continue  # skip the math, ask again

        total = add_expense(total, new_expense)
        count += 1
        print(f"  Added {format_total(new_expense)} | "
              f"Running total: {format_total(total)}")

    # OUTPUT: runs after the loop ends
    print("\n" + "-" * 40)
    print(f"Transactions recorded: {count}")
    print(f"FINAL TOTAL: {format_total(total)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
