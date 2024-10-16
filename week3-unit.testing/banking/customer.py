class Customer:
    def __init__(self, identity, fullname):
        self.__identity = identity
        self.__fullname = fullname
        self.__accounts = []

    @property
    def identity(self):
        return self.__identity

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname):
        self.__fullname = fullname

    @property
    def accounts(self):
        return self.__accounts

    def add_account(self, account):
        self.__accounts.append(account)

    def remove_account(self, account):
        self.__accounts.remove(account)

    def get_account(self, iban):
        for account in self.__accounts:
            if account.iban == iban:
                return account
        return None
