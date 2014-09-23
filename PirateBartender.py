import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def askStyle(styleDict):
    for style in questions.keys():
        response = raw_input(questions[style] + " ")
        styleDict[style]=response.lower() in ("y", "yes")

    return styleDict

def constructDrink(styleDict):
    drink = []
    for style in styleDict.keys():
        if styleDict[style] == True:
            randIndex = random.randint( 0, len(ingredients[style])-1 )
            drink.append(ingredients[style][randIndex])
    return drink

if __name__ == '__main__':
    styleDict = {}
    print
    drink = constructDrink(askStyle(styleDict))
    print "\nHere ye be... yer drink be having:"
    for i in drink:
        print i