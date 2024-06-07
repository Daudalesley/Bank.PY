
class ChildrenAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)
        self._balance *= 1.007  # 0.7% interest

    def withdraw(self, amount):
        print("Withdrawal not allowed for Children Account!")
