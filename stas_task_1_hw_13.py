class Currency:
    currencies = 0 # Amount of currencies in our class
    curr_list = set()  # Make vault for currencies which we want to add later

    def __init__(self, name, amount, country):
        self.name = name
        self.amount = amount
        self.country = country
        Currency.currencies += 1

    def __call__(self, coeff):  # Lets multiply amount of our currency
        return self.amount * coeff

    def __repr__(self):  # Return string representation of currency name
        return self.name

    @classmethod  # Return amount of currencies in our class
    def get_currency_amount(cls):
        return cls.currencies

    @staticmethod  # Return list of currencies which we will add later
    def base_currencies(*args):
        Currency.curr_list.add(*args)
        return list(Currency.curr_list)

    @property  # Make getter,setter,deleter for country of our currency
    def country_name(self):
        return self.country

    @country_name.setter
    def country_name(self, value: str):
        self.country = value

    @country_name.deleter
    def country_name(self):
        self.country = None


curr_1 = Currency('usd', 10, 'Usa')
print(curr_1(4))
print(curr_1.__repr__())
print(Currency.get_currency_amount())

print(Currency.base_currencies('eur'))
print(Currency.base_currencies('uah'))

print(curr_1.country_name)
curr_1.country_name = 'Canada'
print(curr_1.country)
del curr_1.country_name
print(curr_1.country)
