class Category:
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []
        self._budget = 0.0
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self._budget += amount


def create_spend_chart(categories):
    pass