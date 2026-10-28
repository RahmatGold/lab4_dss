# Authors: Rahmatulloh and Bahodir
# 4.1 10.5 -> TypeError, -10 -> ValueError. deposit(True) is rejected because type(True) is bool.
# 4.3 Refund is a third kind, because the history must show why the money came.
# 4.4 0.1 + 0.2 = 0.30000000000000004, int tiyin is exact.
class Wallet:
    def __init__(self, owner_id):
        self.owner_id = owner_id
        self._balance = 0
        self._history = []
    @property
    def balance(self):
        return self._balance
    @property
    def history(self):
        return tuple(self._history)
    def _check(self, amount):
        if type(amount) is not int:
            raise TypeError("int needed")
        if amount <= 0:
            raise ValueError("must be positive")
    def deposit(self, amount):
        self._check(amount)
        self._balance += amount
        self._history.append(("deposit", amount, self._balance))
    def withdraw(self, amount):
        self._check(amount)
        if amount > self._balance:
            raise ValueError("not enough money")
        self._balance -= amount
        self._history.append(("withdraw", amount, self._balance))
    def refund(self, amount):
        self._check(amount)
        self._balance += amount
        self._history.append(("refund", amount, self._balance))

def test_wallet():
    w = Wallet("Rahmatulloh")
    w.deposit(1000)
    w.withdraw(300)
    assert w.balance == 700
    try:
        w.balance -= 500
        assert False
    except AttributeError:
        pass
    try:
        w.withdraw(5000)
        assert False
    except ValueError:
        pass


