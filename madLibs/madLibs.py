# Basic Madlib project

#help functions
def getVerb():
    return input("Enter past tense verb: ")

def getAdj():
    return input("Enter Adjective: ")

def getNoun():
    return input("Enter Noun: ")

def getColor():
    return input("Enter Color: ")

def getDirection():
    return input("Enter a direction: ")
#main
def main():
    print("Lets play MadLibs!")
    noun1 = getNoun()
    verb = getVerb()
    adj1 = getAdj()
    noun2 = getNoun()
    adj2 = getAdj()
    direction = getDirection()

    print("The " + adj1 + " " + adj2 + " " + noun1 + " " + verb + " " + direction +" the " + noun2 + "." )

main()