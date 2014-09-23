import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
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

    drink = constructDrink(askStyle(styleDict))

    if len(drink) > 1:
        print '\nHere be yer',
        print random.choice(adjectives), random.choice(nouns) + ":"
        for i in drink:
            print " -", i
    else: 
        print "\nYar a picky one!  No drink for ye, then."