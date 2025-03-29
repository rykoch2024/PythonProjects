# Tasks
# [] Split item into 3 parts: int1, int2, and symbol
# [] Determine length of longer number
# [] Determine if + or -



def sizeMatch(number, length):
    sizeDifference = length - len(number)
    result = ''
    for _ in range(sizeDifference):
        result += ' '
    result += number    
    return result

def arithmetic_arranger(problems, show_answers=False):
    firstNum = []
    secondNum = []
    result = []
    lineDraw = []
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    for equation in problems:
        parts = equation.split()
        line = ''
        answer = ''
#Error tests: 1 - Numbers only contain digits, 2: Numbers 4 digits or less, 3: operator is + or -
        if not (parts[1] == '+' or parts[1] == '-'):
            raise ValueError("Error: Operator must be '+' or '-'.")
        elif max(len(parts[0]), len(parts[2])) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        elif not (parts[0].isdigit() and parts[2].isdigit()):
            raise ValueError('Error: Numbers must only contain digits.')

    #Expression Evaluation        
        if parts[1] == '+':
            answer = int(parts[0]) + int(parts[2])
        if parts[1] == '-':
            answer = int(parts[0]) - int(parts[2])

    # initial size Adjustments
        longer = max(len(parts[0]), len(parts[2]))
        parts[0] = '  ' + sizeMatch(parts[0], longer) + '    '
        parts[2] = parts[1]+ ' ' + sizeMatch(parts[2], longer) + '    '

        
        

        if show_answers:
            answer = str(answer)
            newLonger = max(len(parts[0]) - 4,len(parts[0]) - 4, len(answer))
            parts[0]  = sizeMatch(parts[0], newLonger)
            parts[2]  = sizeMatch(parts[2], newLonger)
            result.append(sizeMatch(answer, newLonger) + '    ')
        
        for _ in range(len(parts[2]) - 4):
            line += '-'

        firstNum.append(parts[0])
        secondNum.append(parts[2])
        lineDraw.append(line + '    ')
        
            
        


    print(firstNum)
    print(secondNum)
    print(lineDraw)
    print(result)
    return problems


print(f'\n{arithmetic_arranger(["9932 + 9"], True)}')
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')