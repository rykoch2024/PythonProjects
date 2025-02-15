import random

def game():
    number = random.randrange(1,100)
    print(number)
    guess = int(input("Give your guess (1-100): "))
    for x in range(5):
        if guess == number: 
            print("You win!")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
        currentTurn = 5 - x
        print(str(currentTurn) + " turns Remaining")
        guess = int(input("Give your guess (1-100): "))
    print("Game over, value was " + str(number))



def runGame():
    continuing = True
    while continuing:
        game()
        cont = input("Continue(Y/N)? ")
        cont = cont.upper()
        if cont == "Y":
            continuing = True
        else:
            continuing = False

runGame()