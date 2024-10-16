from banking.customer import Customer


class Bank:
    def __init__(self, name):
        self._name = name
        self._customers = []

    @property
    def name(self):
        return self._name

    @property
    def customers(self):
        return self._customers

    def create_customer(self, identity, fullname):
        customer = Customer(identity, fullname)
        self._customers.append(customer)
        return customer

    def get_account(self, iban):
        for customer in self._customers:
            account = customer.get_account(iban)
            if account is not None:
                return account
        return None
