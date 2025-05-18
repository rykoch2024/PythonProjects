# The following code is from freecodecamp.org
# Path: The Scientific Computing with Python.
# Project: Build a Budget App Project

import math
class Category:
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []
        self._budget = 0.0

    def __str__(self):
        printOut = ''

        # Title Line
        numAstrisk = (30 - len(self.catName)) // 2
        for _ in range(numAstrisk):
            printOut += '*'
        printOut += self.catName
        while len(printOut) < 30:
            printOut += '*'
        printOut += '\n'
        
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

        # Total
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

#for use by create_spend_chart
def _withdrawTotals(cat=Category):
    totalWithdraw = 0
    if hasattr(cat, 'ledger'):
        for item in cat.ledger:
            if item.get('amount') < 0:
                totalWithdraw =  item.get('amount') * -1
    return [cat.catName, totalWithdraw]


def create_spend_chart(categories=Category):
    dispGraph = {}
    returnString = ''
    title = 'Percentage spent by category'
    TotalWithdrawAmount = 0
    withdrawList = []

    #get withdraws for each category
    for item in categories:
        currentTotal = _withdrawTotals(item)
        withdrawList.append(currentTotal)
        TotalWithdrawAmount += currentTotal[1]

    #init graph generation
    for i in range(100, -10, -10):
        key = str(i)
        graph = [f'{i:>3}| ']
        i -= 10
        dispGraph.update({key:graph})
    dispGraph.update({'final': [f"{'':4}-"]})
    
    #Bar Generation
    for j in range(len(withdrawList)):
        addMarker = math.floor(withdrawList[j][1] / TotalWithdrawAmount * 10) * 10
        currKey = 0
        while currKey <= 100:
            newMark = ''
            if currKey <= addMarker:
                newMark = f'{"o":<3}'
            else:
                newMark = f'{"":<3}'
            dispGraph[f'{currKey}'].append(newMark)
            currKey += 10
    
    # break line
    for j in range(len(withdrawList)):
        dispGraph['final'].append('---')                

    # Titles under bars
    longestTitle = len(withdrawList[0][0])
    for item in withdrawList:
        if len(item[0]) > longestTitle:
            longestTitle = len(item[0])

    #return statement
    returnString += title + '\n'
    #Graph portion
    for val in dispGraph.values():
        for j in val:
            returnString += j
        returnString += '\n'
    #Below Graph
    for j in range(longestTitle):
        returnString += f"{' ':5}"
        for item in withdrawList:
            if j >= len(item[0]):
                returnString += f"{' ':3}"
            else:
                addMe = f"{item[0][j]:3}"
                returnString += addMe
        returnString += '\n'

    return returnString.strip('\n')




#My Tests
abc = Category('abc')
abc.deposit(900, 'deposit')
abc.withdraw(10.10, 'milk, cereal, eggs, bacon, bread')
abc.withdraw(20.20, 'taco')
abc.withdraw(50.50, 'pasta')
abc.withdraw(80.80, 'spaghetti')
abc.withdraw(90.90, 'cherry')
#print(abc)

# Their Tests
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
#print(food)

print(create_spend_chart([abc, food]))

