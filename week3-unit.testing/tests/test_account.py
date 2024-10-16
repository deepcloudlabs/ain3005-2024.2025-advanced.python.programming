"""
CUT: Account
MUT: business methods: withdraw, deposit, ...
"""
import pytest

from banking.account import Account, AccountStatus
negative_amounts = [
    0, -1, -0.1, -1.1
]
@pytest.fixture
def an_active_account():
    return Account("tr1", 1_000, AccountStatus.ACTIVE)

@pytest.fixture
def a_closed_account():
    return Account("tr1", 0, AccountStatus.CLOSED)

@pytest.mark.parametrize("amount",negative_amounts)
def test_deposit_with_negative_amount_should_fail(an_active_account,amount):
   with pytest.raises(ValueError):
       an_active_account.deposit(amount)

def test_deposit_to_not_activeaccount_should_fail(a_closed_account):
   with pytest.raises(ValueError):
       a_closed_account.deposit(1)

def test_deposit_with_positive_amount_should_success(an_active_account):
   an_active_account.deposit(1)
   assert an_active_account.balance == 1_001
   assert an_active_account.status == AccountStatus.ACTIVE
