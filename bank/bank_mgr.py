class BankMgr:

    def __init__(self, id, interests, accounts, currencies, balance):
        self.id = id
        self.interests = interests
        self.accounts = accounts
        self.currencies = currencies
        self.balance = balance


print(type(BankMgr))
