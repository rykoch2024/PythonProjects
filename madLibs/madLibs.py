"""
Madlibs project Goals
1. User input prompt
    a. verify it is a word.
2. Multiple inserts for verbs, adjatives, nouns
3. Random sentence selection
"""

def getVerb():
    return input("Enter Verb: ")

def getAdj():
    return input("Enter Adjective: ")

def getNoun():
    return input("Enter Noun: ")

def getColor():
    return input("Enter Color: ")


noun1 = getNoun()
verb = getVerb()
adj1 = getAdj()
noun2 = getNoun()
adj2 = getAdj()

"""The little red rabbit ran over the river"""

print("The " + adj1 + " " + adj2 + " " + noun1 + " " + verb + " over the " + noun2 + "." )

