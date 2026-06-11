# FinanceTracker Crew

A multi-agent AI system that analyzes your personal finances from a CSV file — fully local, free, and private. Built with [crewAI](https://crewai.com) and powered by [Ollama](https://ollama.com) (no OpenAI account or API key needed).

## What It Does

Four AI agents work in sequence to process your bank transactions:

| Agent                       | Role                                                             |
| --------------------------- | ---------------------------------------------------------------- |
| **Transaction Categorizer** | Labels each transaction (Food, Rent, Transport, etc.)            |
| **Financial Analyst**       | Calculates totals, flags large expenses, spots recurring charges |
| **Report Writer**           | Produces a readable summary with spending breakdown              |
| **Finance Advisor**         | Gives personalized tips to improve your spending habits          |

The final report is saved to `finance_report.md` in your project root.

## Requirements

- Python 3.10–3.12
- [Ollama](https://ollama.com) installed and running locally

## Installation

**1. Install uv** (if you haven't already):

```bash
pip install uv
```

**2. Install Ollama** from [ollama.com](https://ollama.com), then pull a model:

```bash
ollama pull llama3.1
```

**3. Install project dependencies:**

```bash
crewai install
```

**4. Configure your `.env` file** in the project root:

```
MODEL=ollama/llama3.1:latest
API_BASE=http://localhost:11434
```

> Run `ollama list` to confirm the exact model name to use.

## Running the Project

**1. Make sure Ollama is running** (in a separate terminal if needed):

```bash
ollama serve
```

**2. Add your CSV file** to the project root. It should have columns like:

```
Date, Description, Amount, Type
```

**3. Set your CSV filename** in `src/finance_tracker/main.py`:

```python
csv_path = "your_transactions.csv"
```

**4. Run the crew:**

```bash
crewai run
```

The agents will work through your transactions one by one. When finished, your report is saved to `finance_report.md`.

## Project Structure

```
finance_tracker/
├── .env                          # Ollama model config
├── sample_transactions.csv       # Test data
├── finance_report.md             # Generated report (after running)
└── src/finance_tracker/
    ├── main.py                   # Entry point — set your CSV path here
    ├── crew.py                   # Wires agents and tasks together
    └── config/
        ├── agents.yaml           # Agent roles, goals, and backstories
        └── tasks.yaml            # Task instructions and expected outputs
```
