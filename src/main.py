import webbrowser
from taipy.gui import Gui, Markdown, notify

# Define your page
page = Markdown(
"""
# Financial Planner

Enter your monthly income: <|income|text|on_action=handle_change|>

Enter your monthly expenses: <|expenses|text|on_action=handle_change|>

<|Calculate|button|on_action=on_calculate|>

Your savings: <|savings|text|>
"""
)

# Define action functions
def handle_change(state, var_name: str, var_value):
    if var_name == "income":
        state.vars.income = float(var_value)
    elif var_name == "expenses":
        state.vars.expenses = float(var_value)

def on_calculate(state):
    income = state.vars.get('income')
    expenses = state.vars.get('expenses')
    if income and expenses:
        savings = calculate_savings(income, expenses)
        state.vars.savings = f"Your savings are {savings}"
        notify(state, "success", f"Your savings are {savings}")
    else:
        notify(state, "error", "Please enter your income and expenses")

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
