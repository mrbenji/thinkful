import bicycle_classes
import random


def ul_string(string_to_ul, ul_char="-"):
    return str(string_to_ul) + "\n" + (ul_char * len(string_to_ul))

budget_wheel = bicycle_classes.Wheel("Leadset", 2.29, 54.99)
midrange_wheel = bicycle_classes.Wheel("IronWorks", 2.16, 149.99)
highend_wheel = bicycle_classes.Wheel("NanoTube", 1.58, 449.99)

budget_frame = bicycle_classes.Frame("Tank", "steel", 28.5, 49.99)
midrange_frame = bicycle_classes.Frame("Sedan", "aluminum", 24.5, 149.99)
highend_frame = bicycle_classes.Frame("Butterfly", "carbon",20.5, 699.99)

bike1 = bicycle_classes.Bicycle("M1", budget_wheel, budget_frame)
bike2 = bicycle_classes.Bicycle("M2", budget_wheel, midrange_frame)
bike3 = bicycle_classes.Bicycle("M3", midrange_wheel, budget_frame)
bike4 = bicycle_classes.Bicycle("M4", midrange_wheel, midrange_frame)
bike5 = bicycle_classes.Bicycle("M5", midrange_wheel, highend_frame)
bike6 = bicycle_classes.Bicycle("M6", highend_wheel, highend_frame)

alpha_bikes = bicycle_classes.BikeShop("Alpha Bikes", [bike1, bike2, bike3, bike4, bike5, bike6])

customer1 = bicycle_classes.Customer("Customer1", 200)
customer2 = bicycle_classes.Customer("Customer2", 500)
customer3 = bicycle_classes.Customer("Customer3", 1000)

print "\n" + ul_string("{} Initial Inventory:".format(alpha_bikes.name), "~")
print alpha_bikes.pretty_inventory()

for customer in (customer1, customer2, customer3):
    print "Customer name:", customer.name
    print "Bikes in Budget:",
    bikes_in_budget = customer.affordable_bikes(alpha_bikes).keys()
    bikes_in_budget.sort()
    print ", ".join(bikes_in_budget) + "\n"

for customer in (customer1, customer2, customer3):
    bike_name = random.choice(customer.affordable_bikes(alpha_bikes).keys())
    customer.buy_bicycle(alpha_bikes,bike_name)

print "\n" + ul_string("{} Final Inventory:".format(alpha_bikes.name), "~")
print alpha_bikes.pretty_inventory()

print "\nProfit made: ${:.2f}".format(alpha_bikes.report_profit())

