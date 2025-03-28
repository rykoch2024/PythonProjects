# Tasks
# [] Split item into 3 parts: int1, int2, and symbol
# [] Determine length of longer number
# [] Determine if + or -
# []
# []
# []
# []
# []
# []
# []



def arithmetic_arranger(problems, show_answers=False):
    firstNum = []
    sign = []
    secondNum = []
    result = []
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    for equation in problems:
        parts = equation.split()
#Error tests: 1 - Numbers only contain digits, 2: Numbers 4 digits or less, 3: operator is + or -
        if not (parts[1] == '+' or parts[1] == '-'):
            raise ValueError("Error: Operator must be '+' or '-'.")
        elif max(len(parts[0]), len(parts[2])) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        elif not (parts[0].isdigit() and parts[2].isdigit()):
            raise ValueError('Error: Numbers must only contain digits.')
        else:
            firstNum.append(parts[0])
            sign.append(parts[1])
            secondNum.append(parts[2])
        
        if parts[1] == '+':
            result.append(int(parts[0]) + int(parts[2]))
        if parts[1] == '-':
            equation.append(int(parts[0]) - int(parts[2]))

        
            
        


    print(firstNum)
    print(sign)
    print(secondNum)
    print(equation)
    return problems


print(f'\n{arithmetic_arranger(["32 + 699"])}')
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')