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
            lineDesc = item.get('description')
            lineAmount = f"{item.get('amount'):.2f}"
            if len(lineDesc) >= 23:
                FinalDesc = lineDesc[:23]
            else:
                FinalDesc = lineDesc
                while len(FinalDesc) < 23:
                    FinalDesc += ' '
            if len(lineAmount) < 7:
                lineAmount = ' ' + lineAmount

            line += FinalDesc + lineAmount
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









# Problems are here

def create_spend_chart(categories=Category):
    localCal = categories
    dispGraph = {}
    returnString = ''
    title = 'Percentage spent by category'
    totalWithdraws = 0
    withdrawItem = 0
    withdrawList = []

    returnString += title + '\n'

    #init graph generation
    i = 100
    while i >= 0:
        key = str(i)
        graph = [f'{i:>3}| ']
        i -= 10
        dispGraph.update({key:graph})
    dispGraph.update({'final': f"{'':4}-"})


    for item in dispGraph.values():
        returnString += item[0] + '\n'


    #FUCK THE LEDGER!! THIS SHIT IS BREAKING STUFF IT HAS NO RIGHT BREAKING!!
    
    if hasattr(localCal, "ledger"):
        pass
#        for item in localCal.ledger:
#            if item.get('amount') < 0:
#                item['amount'] = item.get('amount') * -1
#                withdrawList.append(item)
#                totalWithdraws += item.get('amount')
    else:
        returnString += 'no ledger'


        #calculate percentages & add to graph
    for item in withdrawList:
        if totalWithdraws > 0:
            percentage = int(round(item['amount'] / totalWithdraws, 1) * 100)
            item.update({'percentage': percentage})

    
        withdrawItem = 0

    while withdrawItem < len(withdrawList):
        addMarker = withdrawList[withdrawItem]['percentage']
        currKey = 0
        while currKey <= 100:
            newMark = ''
            if currKey <= addMarker:
                newMark += f"{'0':<3}"
            else:
                newMark += f"{'':3}"
            
            temp = dispGraph[str(currKey)]
            temp.append(newMark)
            dispGraph[str(currKey)] = temp

            currKey += 10
        
        temp = dispGraph['final']
        temp += '---'
        dispGraph['final'] = temp
        withdrawItem += 1
    
    return returnString


food = Category('food')
food.deposit(900, 'deposit')
food.withdraw(10.10, 'milk, cereal, eggs, bacon, bread')
food.withdraw(20.20, 'taco')
food.withdraw(50.50, 'pasta')
food.withdraw(80.80, 'spaghetti')
food.withdraw(90.90, 'cherry')
#print(food)

print(create_spend_chart(food))

