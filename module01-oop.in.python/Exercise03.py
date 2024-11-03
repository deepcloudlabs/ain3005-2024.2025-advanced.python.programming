from abc import ABC, abstractmethod
from enum import Enum


class InsufficientBalanceException(Exception):
    def __init__(self, message, deficit):
        super().__init__()
        self.message = message
        self.deficit = deficit


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


# interface -> abstract class
class Depositable(ABC):
    # abstract method
    @abstractmethod
    def deposit(self, amount: float) -> float:
        pass

    # abstract method
    @abstractmethod
    def gun(self):
        pass


class Withdrawable:
    def withdraw(self, amount: float) -> float:
        pass


class SavingsAccount(Withdrawable):
    pass


class CurrencyHedgedAccount(Depositable):
    pass


class DebitAccount(Depositable, Withdrawable):
    def __init__(self, iban, balance=5_000, status=AccountStatus.ACTIVE):
        # attributes/state/data: iban, balance
        self.__iban = iban
        # constraint: self.balance must be always positive or zero
        self._balance = balance
        self.__status = status

    def deposit(self, amount):
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        self._balance = self._balance + amount
        return self._balance

    # business method
    def withdraw(self, amount):
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        # business rule
        if amount > self._balance:
            deficit = amount - self._balance
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount
        return self._balance

    def gun(self):
        pass

    @property
    def balance(self):
        return self._balance

    @property
    def iban(self):
        return self.__iban

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError('Status cannot be None')
        if status not in [AccountStatus.ACTIVE, AccountStatus.CLOSED, AccountStatus.BLOCKED]:
            raise ValueError('Status must be either "Active", "Closed", "Blocked"')
        self.__status = status

    def __str__(self):
        return f"Account: iban: {self.__iban}, balance: {self._balance}, status: {self.__status}"


"""
CheckingAccount: sub class,derived class
Account        : super class, base class
"""


class CheckingAccount(DebitAccount):
    def __init__(self, iban, balance=5_000, status=AccountStatus.ACTIVE, overdraft_amount=1_000):
        super().__init__(iban, balance, status)
        self.__overdraftAmount = overdraft_amount

    # overriding
    def withdraw(self, amount):
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        # business rule
        if amount > (self._balance + self.__overdraftAmount):
            deficit = amount - self._balance - self.__overdraftAmount
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount
        return self._balance

    @property
    def overdraft_balance(self):
        return self.__overdraftAmount

    @overdraft_balance.setter
    def overdraft_balance(self, overdraft_amount):
        if overdraft_amount <= 0.0:
            raise ValueError('Overdraft amount must be positive')
        self.__overdraftAmount = overdraft_amount

    def __str__(self):
        return f"CheckingAccount: iban: {self.iban}, balance: {self.balance}, status: {self.status}, overdraftAmount: {self.__overdraftAmount}"


class Customer:
    def __init__(self, identity, fullname):
        self.__identity = identity
        self.__fullname = fullname
        self.__accounts: [Withdrawable] = []

    def add_account(self, account):
        self.__accounts.append(account)

    def fun(self, amount):
        for account in self.__accounts:
            if isinstance(account, Withdrawable):
                account.withdraw(amount)


acc1 = DebitAccount("TR290006222359813456984831", 100_000)
acc2 = CheckingAccount("TR290006222359813456984831", 100_000, overdraft_amount=10_000)
jack = Customer("11111111110", "jack bauer")
jack.add_account(acc1)
jack.add_account(acc2)
try:
    acc1.withdraw(50_000)
    print(acc1)
    print(acc2)
    acc1.withdraw(25_000)
    print(str(acc1))
    print(acc1)
    print(acc1.balance)
    print(acc1.status)  # calls getter method
    acc1.status = AccountStatus.CLOSED  # calls setter method
    acc1.withdraw(1_000_000)
except InsufficientBalanceException as e:
    print(f"Reason is {e.message}")
    print(f"Deficit is {e.deficit}")
except ValueError as e:
    print(f"Reason is {e}")
