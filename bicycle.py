from __future__ import (absolute_import, print_function, unicode_literals, division)

import bicycle_classes
import random


def ul_string(string_to_ul, ul_char="-"):
    return str(string_to_ul) + "\n" + (ul_char * len(string_to_ul))

budget_wheel = bicycle_classes.Wheel("Leadset", 2.29, 54.99)
midrange_wheel = bicycle_classes.Wheel("IronWorks", 2.16, 149.99)
highend_wheel = bicycle_classes.Wheel("NanoTube", 1.58, 449.99)

budget_frame = bicycle_classes.Frame("Tank", "steel", 28.5, 49.99)
midrange_frame = bicycle_classes.Frame("Sedan", "aluminum", 24.5, 99.99)
highend_frame = bicycle_classes.Frame("Butterfly", "carbon", 20.5, 699.99)

beta_bikes = bicycle_classes.BicycleManufacturer("Beta Bikes", .10, [
    bicycle_classes.Bicycle("B1", budget_wheel, budget_frame, "Beta Bikes"),
    bicycle_classes.Bicycle("B2", budget_wheel, midrange_frame, "Beta Bikes"),
    bicycle_classes.Bicycle("B3", midrange_wheel, budget_frame, "Beta Bikes")
])

omega_bikes = bicycle_classes.BicycleManufacturer("Mega Bikes", .12, [
    bicycle_classes.Bicycle("M4", midrange_wheel, midrange_frame, "Beta Bikes"),
    bicycle_classes.Bicycle("M5", midrange_wheel, highend_frame, "Beta Bikes"),
    bicycle_classes.Bicycle("M6", highend_wheel, highend_frame, "Beta Bikes")
])

alpha_bike_shop = bicycle_classes.BikeShop("Alpha Bike Shop", beta_bikes.models_sold + omega_bikes.models_sold)

customer1 = bicycle_classes.Customer("Ophelia Payne", 300)
customer2 = bicycle_classes.Customer("Eureka Garlic", 450)
customer3 = bicycle_classes.Customer("Orson Buggy", 1200)

print ("\n" + ul_string("{} Initial Inventory:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

for customer in (customer1, customer2, customer3):
    print ("Customer name:", customer.name)
    print ("Bikes in Budget:", end=" ")
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        bikes_in_budget.sort()
        print (", ".join(bikes_in_budget) + "\n")
    else:
        print ("None.\n")

for customer in (customer1, customer2, customer3):
    bikes_in_budget = customer.affordable_bikes(alpha_bike_shop).keys()
    if len(bikes_in_budget) > 0:
        bike_name = random.choice(bikes_in_budget)
        customer.buy_bicycle(alpha_bike_shop, bike_name)
    else:
        print (customer.name, "doesn't have enough money to buy a bike!")
        print ("Their bicycle fund still has ${:.02f} remaining.\n".format(customer.bike_fund))

print ("\n" + ul_string("{} Final Inventory:".format(alpha_bike_shop.name), "~"))
print (alpha_bike_shop.pretty_inventory())

print ("\nProfit made: ${:.2f}".format(alpha_bike_shop.report_profit()))
