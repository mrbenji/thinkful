from __future__ import (absolute_import, print_function, unicode_literals, division)

import random

import bicycle_classes
from bicycle_classes import pretty_money

BUY_BEST_BIKE_POSSIBLE = True


def ul_string(string_to_ul, ul_char="-"):
    """
    Returns a 1-line string in "underlined" form.
    Does not work properly on strings containing "\n"
    :param string_to_ul: input string
    :param ul_char: character to use for "underlining," defaults to "-"
    :returns: The original string + "\n" + len(string_to_ul) of ul_char
    """
    return str(string_to_ul) + "\n" + (ul_char * len(string_to_ul))

budget_wheel = bicycle_classes.Wheel("Leadset", 2.29, 54.47)
midrange_wheel = bicycle_classes.Wheel("IronWorks", 2.16, 149.19)
highend_wheel = bicycle_classes.Wheel("NanoTube", 1.58, 449.29)

budget_frame = bicycle_classes.Frame("Tank", "steel", 28.5, 49.34)
midrange_frame = bicycle_classes.Frame("Sedan", "aluminum", 24.5, 99.72)
highend_frame = bicycle_classes.Frame("Butterfly", "carbon", 20.5, 699.09)

weeble_bikes = bicycle_classes.BicycleManufacturer("Weeble Bikes", .10, [
    bicycle_classes.Bicycle("E1", budget_wheel, budget_frame, "Weeble Bikes"),
    bicycle_classes.Bicycle("E2", budget_wheel, midrange_frame, "Weeble Bikes"),
    bicycle_classes.Bicycle("E3", midrange_wheel, budget_frame, "Weeble Bikes")
])

weasel_bikes = bicycle_classes.BicycleManufacturer("Weasel Bikes", .12, [
    bicycle_classes.Bicycle("A4", midrange_wheel, midrange_frame, "Weasel Bikes"),
    bicycle_classes.Bicycle("A5", midrange_wheel, highend_frame, "Weasel Bikes"),
    bicycle_classes.Bicycle("A6", highend_wheel, highend_frame, "Weasel Bikes")
])

alpha_bike_shop = bicycle_classes.BikeShop("Alpha Bike Shop", weeble_bikes.models_sold + weasel_bikes.models_sold)

customers = [
    bicycle_classes.Customer("Ophelia Payne", 300),
    bicycle_classes.Customer("Eureka Garlic", 500),
    bicycle_classes.Customer("Orson Buggy", 1200)
]

print ("\n" + ul_string("{} Initial Inventory:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

for customer in customers:
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        bikes_in_budget.sort()
        print ("{} can afford these models: {}".format(customer.name, ", ".join(bikes_in_budget))+"\n")
    else:
        print ("None.\n")

for customer in customers:
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        if BUY_BEST_BIKE_POSSIBLE is True:
            bike_name = customer.most_expensive_affordable_bike(alpha_bike_shop)
        else:
            bike_name = random.choice(bikes_in_budget)
        customer.buy_bicycle(alpha_bike_shop, bike_name)
    else:
        print (customer.name, "doesn't have enough money to buy a bike!")
        print ("Their bicycle fund still has {} remaining.\n".format(pretty_money(customer.bike_fund)))

print ("\n" + ul_string("{} Final Inventory:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

print ("\nProfit made: {}".format(pretty_money(alpha_bike_shop.report_profit())))
