import random

questions = {
    "strong": "Do ye want yer drink strong?",
    "salty": "Do ye want it with a salty tang?",
    "bitter": "Are ye a lubber who wants it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["shot of tequila", "glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["seaweed flakes","olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["minced radicchio","shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["powdered lead", "sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["durian puree", "slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["Furry","Balding","Slutty","Shiny","Uncultured"]
nouns = ["Dingo","Jackhammer","Navel", "Superhero","Doughnut"]


def askStyle(styleDict):
    
    print

    for style in questions.keys():
        response = raw_input(questions[style] + " ")
        styleDict[style]=response.lower() in ("y", "yes")

    return styleDict


def constructDrink(styleDict):
    
    drink = []
    
    for style in styleDict.keys():
        if styleDict[style] == True:
            drink.append( random.choice(ingredients[style]) )

    return drink


if __name__ == '__main__':
    
    styleDict = {}
    numDrunk = 0

    print "\nAhoy thar... let's find a new drink for ye!"

    while True:

        if numDrunk > 4:
            print "\nYer too drunk to even walk the plank... yer cut off!"
            break

        drink = constructDrink(askStyle(styleDict))

        if len(drink) > 1:
            numDrunk += 1
            print '\nHere be yer',
            print random.choice(adjectives), random.choice(nouns) + ":"
            for i in drink:
                print " -", i
        else: 
            print "\nYar a picky one!  No drink for ye, then."
            break

        while True: 
            print
            another = raw_input('Would ye like another? ')
            if another.lower() in ("y","yes","n","no"):
                break

        if another.lower() in ("y","yes"):
            print "\nLet's see what grog suits yer fancy this time."

        if another.lower() in ("n","no"):
            print ("\nOff with ye then, ye scallywag!")
            break

