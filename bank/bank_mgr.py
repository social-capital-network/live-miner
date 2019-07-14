class BankMgr:

    def __init__(self, balance):
        self.id = 1
        self.interests = ['ai', 'blockchain']
        self.accounts = {'CAD': 1000.0, 'USD': 2000.0, 'python': 314.0}
        self.currencies = ['CAD', 'USD', 'PYTHON']
        self.balance = balance


banker = BankMgr(3314.0)
print(type(banker))
print(type(BankMgr))
