class Category:
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []
        self._budget = 0.0
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self._budget += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -1 * amount, 'description': description})
            self._budget -= amount
            return True
        return False
    
    def get_balance(self):
        return self._budget

    def transfer():
        pass

    #Required for use by withdraw and transfer
    def check_funds(self, amount):
        if amount > self._budget:
            return False
        return True

def create_spend_chart(categories):
    pass


food = Category('food')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
print('test')