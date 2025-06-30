from accounts import Account
import gradio as gr

# Create an instance of Account for demonstration
user_account = Account("user_001")
initial_deposit = 1000.0  # Let's assume an initial deposit for calculation

# Function to handle deposit
def handle_deposit(amount):
    user_account.deposit(amount)
    return f"Deposited ${amount:.2f}. Current Balance: ${user_account.balance:.2f}"

# Function to handle withdrawal
def handle_withdraw(amount):
    try:
        user_account.withdraw(amount)
        return f"Withdrew ${amount:.2f}. Current Balance: ${user_account.balance:.2f}"
    except ValueError as e:
        return str(e)

# Function to handle buying shares
def handle_buy(symbol, quantity):
    try:
        user_account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}. Current Holdings: {user_account.holdings}"
    except ValueError as e:
        return str(e)

# Function to handle selling shares
def handle_sell(symbol, quantity):
    try:
        user_account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}. Current Holdings: {user_account.holdings}"
    except ValueError as e:
        return str(e)

# Function to report total portfolio value
def report_portfolio_value():
    total_value = user_account.total_portfolio_value()
    return f"Total Portfolio Value: ${total_value:.2f}"

# Function to report profit/loss
def report_profit_loss():
    profit_loss = user_account.profit_loss(initial_deposit)
    return f"Profit/Loss: ${profit_loss:.2f}"

# Function to report current holdings
def report_holdings():
    holdings = user_account.report_holdings()
    return f"Current Holdings: {holdings}"

# Function to list transactions
def list_transactions():
    transactions = user_account.list_transactions()
    return f"Transactions: {transactions}"

# Set up gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### Trading Simulation Account Management")
    deposit_amount = gr.Number(label="Deposit Amount", value=0)
    deposit_btn = gr.Button("Deposit")
    deposit_output = gr.Textbox(label="Deposit Output", interactive=False)

    withdraw_amount = gr.Number(label="Withdrawal Amount", value=0)
    withdraw_btn = gr.Button("Withdraw")
    withdraw_output = gr.Textbox(label="Withdrawal Output", interactive=False)

    buy_symbol = gr.Textbox(label="Buy Symbol (e.g., AAPL)")
    buy_quantity = gr.Number(label="Buy Quantity", value=0)
    buy_btn = gr.Button("Buy Shares")
    buy_output = gr.Textbox(label="Buy Output", interactive=False)

    sell_symbol = gr.Textbox(label="Sell Symbol (e.g., AAPL)")
    sell_quantity = gr.Number(label="Sell Quantity", value=0)
    sell_btn = gr.Button("Sell Shares")
    sell_output = gr.Textbox(label="Sell Output", interactive=False)

    portfolio_value_btn = gr.Button("Get Total Portfolio Value")
    portfolio_value_output = gr.Textbox(label="Portfolio Value", interactive=False)

    profit_loss_btn = gr.Button("Get Profit/Loss")
    profit_loss_output = gr.Textbox(label="Profit/Loss", interactive=False)

    holdings_btn = gr.Button("Report Holdings")
    holdings_output = gr.Textbox(label="Current Holdings", interactive=False)

    transactions_btn = gr.Button("List Transactions")
    transactions_output = gr.Textbox(label="Transactions", interactive=False)

    # Bind functions to buttons
    deposit_btn.click(handle_deposit, inputs=deposit_amount, outputs=deposit_output)
    withdraw_btn.click(handle_withdraw, inputs=withdraw_amount, outputs=withdraw_output)
    buy_btn.click(handle_buy, inputs=(buy_symbol, buy_quantity), outputs=buy_output)
    sell_btn.click(handle_sell, inputs=(sell_symbol, sell_quantity), outputs=sell_output)
    portfolio_value_btn.click(report_portfolio_value, outputs=portfolio_value_output)
    profit_loss_btn.click(report_profit_loss, outputs=profit_loss_output)
    holdings_btn.click(report_holdings, outputs=holdings_output)
    transactions_btn.click(list_transactions, outputs=transactions_output)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()