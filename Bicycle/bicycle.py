from __future__ import (absolute_import, print_function, unicode_literals, division)

import random
import itertools

from bdt_utils import ul_string
from bicycle_classes import Wheel, Frame, Bicycle, Customer, BikeShop, BikeManufacturer, pretty_money

BUY_BEST_BIKE_POSSIBLE = False

budget_wheel = Wheel("Leadset", 2.29, 54.47)
midrange_wheel = Wheel("IronWorks", 2.16, 149.19)
highend_wheel = Wheel("NanoTube", 1.58, 449.29)

budget_frame = Frame("Tank", "steel", 28.5, 49.34)
midrange_frame = Frame("Sedan", "aluminum", 24.5, 99.72)
highend_frame = Frame("Butterfly", "carbon", 20.5, 699.09)

manufacturers = [
    BikeManufacturer("Weeble Bikes", .10, [
        Bicycle("E1", budget_wheel, budget_frame, "Weeble Bikes"),
        Bicycle("E2", budget_wheel, midrange_frame, "Weeble Bikes"),
        Bicycle("E3", midrange_wheel, budget_frame, "Weeble Bikes")
    ]),
    BikeManufacturer("Weasel Bikes", .12, [
        Bicycle("A4", midrange_wheel, midrange_frame, "Weasel Bikes"),
        Bicycle("A5", midrange_wheel, highend_frame, "Weasel Bikes"),
        Bicycle("A6", highend_wheel, highend_frame, "Weasel Bikes")
    ])
]

alpha_bike_shop = BikeShop("Alpha Bike Shop", 10000,
    list(
        itertools.chain.from_iterable(
            [manufacturer.models_sold for manufacturer in manufacturers]
        )
    )
)

customers = [
    Customer("Ophelia Payne", 300),
    Customer("Tristan Schaut", 400),
    Customer("Selma Junkoff", 700),
    Customer("Nadia Geddit", 1200)
]

print ("\n" + ul_string("Initial Inventory for {}:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

for customer in customers:
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        bikes_in_budget.sort()
        print (" - {} can afford these models: {}".format(customer.name, ", ".join(bikes_in_budget)))
    else:
        print ("None.")

print()  # needed a blank line for formatting

for customer in customers:
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        if BUY_BEST_BIKE_POSSIBLE is True:
            bike_name = customer.most_expensive_affordable_bike(alpha_bike_shop)
        else:
            bike_name = random.choice(bikes_in_budget)
        customer.buy_bike(alpha_bike_shop, bike_name)
    else:
        print (customer.name, "doesn't have enough money to buy a bike!")
        print ("Their bike fund still has {} remaining.\n".format(pretty_money(customer.bike_fund)))

print ("\n" + ul_string("Remaining Inventory for {}:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

print ("Profit made: {}".format(pretty_money(alpha_bike_shop.report_profit()))+"\n")
