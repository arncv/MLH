import pandas as pd
from taipy.gui import Gui, Markdown, notify

# Define your page
page = Markdown(
"""
<center>
<|navbar|lov={[("page1", "Homepage"), ("https://docs.taipy.io/en/latest/manuals/about/", "Taipy Docs"), ("https://docs.taipy.io/en/latest/getting_started/", "Getting Started")]}|>
</center>

# Financial Planner

Enter your monthly income: <|{income}|input|>

Enter your monthly expenses: <{expenses}input|>

<|Calculate|button|on_action=on_calculate|>

Your savings: <|savings|text|>
"""
)

# Define action functions
def on_calculate(state):
    income = float(state.vars.get('income', 0))
    expenses = float(state.vars.get('expenses', 0))
    savings = calculate_savings(income, expenses)
    state.vars.savings = f"Your savings are {savings}"
    notify(state, "success", f"Your savings are {savings}")

# Define helper functions
def calculate_savings(income, expenses):
    # Here you could use the Capital One API to get real-world financial data
    # and use it to calculate the user's savings. For simplicity, we'll just
    # subtract expenses from income.
    return income - expenses

# Run your application
if __name__ == "__main__":
    gui = Gui(page=page)
    gui.run(title="Financial Planner")
