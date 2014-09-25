from __future__ import (absolute_import, unicode_literals, print_function, division)

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
    "salty": ["seaweed flakes", "olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["minced radicchio", "shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["powdered lead", "sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["durian puree", "slice of orange", "dash of cassis", "cherry on top"]
}

stock_used = {}

for style in ingredients:
    for ingredient in ingredients[style]:
        stock_used[ingredient] = random.randint(1, 6)

adjectives = ["Furry", "Balding", "Slutty", "Shiny", "Uncultured"]
nouns = ["Dingo", "Jackhammer", "Navel", "Superhero", "Doughnut"]

customers = {}


def ask_style():
    
    style_dict = {}

    for next_style in questions.keys():
        response = raw_input(questions[next_style] + " ")
        style_dict[next_style]=response.lower() in ("y", "yes")

    return style_dict


def construct_drink():
    
    style_dict = ask_style()
    drink = []

    for next_style in style_dict.keys():

        if style_dict[next_style] is True:

            random_choice = random.choice(ingredients[next_style])

            if stock_used[random_choice] == 0:
                print ("\n Arrr... be right back, need to refill my", random_choice, "supply.")
                stock_used[random_choice] == random.randint(1, 5)
            else:
                stock_used[random_choice] -= 1

            drink.append(random_choice)

    return drink


def valid_response(response):

    if response.lower() in ("y", "yes", "n", "no"):
        return True
    else:
        return False


def serve_customer(name):

    while True:

        if customers[name]["numDrunk"] > 4:
            print ("\nYar too drunk to even walk the plank... yar cut off!")
            break

        if len(customers[name]["regDrinkIngredients"]) > 1:
            customers[name]["numDrunk"] += 1
            print ('\nHere be yer', customers[name]["regDrinkName"] + ":")
            for i in customers[name]["regDrinkIngredients"]:
                print (" -", i)
        else: 
            print ("\nYar a picky one!  No drink for ye, then.")
            break

        another_drink = ""

        while True:
            another_drink = raw_input('\nWould ye like another? ')
            if valid_response(another_drink):
                break

        if another_drink.lower() in ("n", "no"):
            print ("\nOff with ye then, ye scallywag!")
            break

    return


if __name__ == '__main__':
    
    while True:
        customer_name = raw_input("\nAhoy thar... what be yar name? ")
        if customer_name not in customers:
            print ("\nWell, " + customer_name + "... let's find a new drink for ye!\n")
            customers[customer_name]={}
            customers[customer_name]["numDrunk"] = 0
            customers[customer_name]["regDrinkName"] = random.choice(adjectives) + " " + random.choice(nouns)
            customers[customer_name]["regDrinkIngredients"] = construct_drink()

        serve_customer(customer_name) 

        another_customer = ""

        while True:
            another_customer = raw_input('\nIs thar another customer to serve? ')
            if valid_response(another_customer):
                break

        if another_customer.lower() in ("n", "no"):
            print ("\nI'm closing up, then... be gone with ye all!\n")
            break

