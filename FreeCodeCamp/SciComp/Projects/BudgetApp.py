class Category:
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []
        self._budget = 0.0

    def __str__(self):
        printOut = ''
        # Title Line(FUNCTIONAL)
        numAstrisk = (30 - len(self.catName)) // 2

        for _ in range(numAstrisk):
            printOut += '*'
        printOut += self.catName

        while len(printOut) < 30:
            printOut += '*'

        printOut += '\n'
        

        # There has to be a better way than this...
        #Item List
        for item in self.ledger:
            line = ''
            line += f'{item['description']:<23}'
            line += '\n'

            printOut += line



        # Total(FUNCTIONAL)
        printOut += f'Total: {self._budget}'
        return printOut
    
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

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.catName}')
            other.deposit(amount, f'Transfer from {self.catName}')
            return True
        return False

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
print(food)