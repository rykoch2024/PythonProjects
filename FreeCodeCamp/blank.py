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











def create_spend_chart(categories):
    dispGraph = {}
    returnString = ''
    title = "Percentage spent by category\n"
    totalWithdraws = 0
    withdrawList = []
    
    #init graph generation
    i = 100
    while i >= 0:
        key = str(i)
        if i == 100:
            graph = str(i) + '|'
        elif i == 0:
            graph = '  ' + str(i) + '|'
        else:
            graph = ' ' + str(i) + '|'
        i -= 10
        dispGraph.update({key:[graph]})
        dispGraph.update({'final': '    '})

    #calculate total withdraws
    for item in categories.ledger:
        if item.get('amount') < 0:
            item['amount'] = item.get('amount') * -1
            withdrawList.append(item)
            totalWithdraws += item.get('amount')
    
    #calculate percentages & add to graph
    for item in withdrawList:
        percentage = int(round(item['amount'] / totalWithdraws, 1) * 100)
        item.update({'percentage': percentage})

    withdrawItem = 0

    while withdrawItem < len(withdrawList):
        addMarker = withdrawList[withdrawItem]['percentage']
        currKey = 0
        while currKey <= 100:
            newMark = ''
            if currKey <= addMarker:
                newMark = ' o '
            else:
                newMark = '   '
            
            temp = dispGraph[str(currKey)]
            temp.append(newMark)
            dispGraph[str(currKey)] = temp

            currKey += 10
        
        temp = dispGraph['final']
        temp += '---'
        dispGraph['final'] = temp
        withdrawItem += 1
    
    
    #print(dispGraph)


    #Final display
    returnString += title

    for key, value in dispGraph.items():
        if key is not 'final':
            for i in value:
                returnString += i
            returnString += '\n'
    for key, value in dispGraph.items():
        if key is 'final':
            for i in value:
                returnString += i
            returnString += '-\n'
    
    return title