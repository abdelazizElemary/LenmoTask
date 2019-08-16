class investor:

    name = 'investor'
    balance = 0.0
    offers = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class borrower:

    name = 'borrower'
    balance = 0.0
    requests = 0

    def __init__(self, name, requests, balance):
        self.name = name
        self.requests = requests
        self.balance = balance
