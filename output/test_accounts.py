import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("user123")
        self.initial_deposit = 1000.0
        self.account.deposit(self.initial_deposit)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-200.0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_withdraw(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 700.0)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(2000.0)
        self.assertEqual(str(context.exception), "Insufficient funds for this withdrawal.")

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-100.0)
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")

    def test_buy_shares(self):
        self.account.buy_shares("AAPL", 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.holdings["AAPL"], 2)

    def test_buy_shares_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.buy_shares("GOOGL", 1)
        self.assertEqual(str(context.exception), "Insufficient funds to buy shares.")

    def test_sell_shares(self):
        self.account.buy_shares("TSLA", 1)
        self.account.sell_shares("TSLA", 1)
        self.assertEqual(self.account.balance, 700.0 + 720.0)
        self.assertNotIn("TSLA", self.account.holdings)

    def test_sell_shares_insufficient_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.account.sell_shares("AAPL", 1)
        self.assertEqual(str(context.exception), "Insufficient shares to sell.")

    def test_profit_loss(self):
        self.account.buy_shares("AAPL", 1)
        self.account.buy_shares("TSLA", 1)
        self.assertAlmostEqual(self.account.profit_loss(self.initial_deposit), (150.0 + 720.0) - 1000.0)

    def test_total_portfolio_value(self):
        self.account.buy_shares("AAPL", 1)
        self.assertAlmostEqual(self.account.total_portfolio_value(), 1000.0 - 150.0 + 150.0)

    def test_report_holdings(self):
        self.account.buy_shares("AAPL", 3)
        self.assertEqual(self.account.report_holdings(), {"AAPL": 3})

    def test_report_profit_loss(self):
        self.assertAlmostEqual(self.account.report_profit_loss(self.initial_deposit), 0.0)

    def test_list_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        transactions = self.account.list_transactions()
        self.assertIn("Deposited $200.00", transactions)
        self.assertIn("Withdrew $100.00", transactions)

if __name__ == '__main__':
    unittest.main()