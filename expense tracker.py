
import math

SENTINEL = "quit"  

def parse_expense(raw_text):
    """
    PHASE 1 - THE GATEKEEPER
    Convert raw text (a string like "100") into a number (100.0).
    Raises ValueError for anything that is not a valid expense, so the
    caller can catch it. '100' + '50' = '10050' (disaster), but
    float('100') + float('50') = 150.0 (truth).
    """
    amount = float(raw_text)  
    if not math.isfinite(amount):  
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


def main():
    
    total = 0.0
    count = 0

    print("=" * 40)
    print("         EXPENSE TRACKER")
    print("=" * 40)
    print("Enter an expense amount (e.g. 100, 50, 20).")
    print(f"Type '{SENTINEL}' when you are finished.\n")

    while True:  
        try:
            raw = input("Enter expense: ").strip()
        except (EOFError, KeyboardInterrupt):
            
            print()
            break

        
        if raw.lower() == SENTINEL:
            break

        
        try:
            new_expense = parse_expense(raw)
        except ValueError:
            print("Invalid Data - please enter a positive number "
                  f"(or '{SENTINEL}' to finish).")
            continue  

        total = add_expense(total, new_expense)
        count += 1
        print(f"  Added {format_total(new_expense)} | "
              f"Running total: {format_total(total)}")

   
    print("\n" + "-" * 40)
    print(f"Transactions recorded: {count}")
    print(f"FINAL TOTAL: {format_total(total)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
