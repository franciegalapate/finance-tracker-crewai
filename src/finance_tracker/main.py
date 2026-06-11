#!/usr/bin/env python
import sys
import os
import warnings
from finance_tracker.crew import FinanceTracker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def load_csv(filepath: str) -> str:
    """Read CSV file and return its content as a string."""
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    with open(filepath, "r") as f:
        return f.read()


def run():
    csv_path = "sample_transactions.csv"

    print(f"\n📂 Loading transactions from: {csv_path}")
    csv_content = load_csv(csv_path)
    print(f"✅ Loaded {len(csv_content.splitlines())} lines\n")

    inputs = {
        "csv_content": csv_content,
        "large_expense_threshold": "500",  # flag transactions above this amount
    }

    try:
        FinanceTracker().crew().kickoff(inputs=inputs)
        print("\n✅ Done! Report saved to finance_report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()