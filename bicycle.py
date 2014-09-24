import bicycle_classes, random

bike1 = bicycle_classes.Bicycle("M1", 32.0, 164.98)
bike2 = bicycle_classes.Bicycle("M2", 31.0, 203.98)
bike3 = bicycle_classes.Bicycle("M3", 30.5, 317.98)
bike4 = bicycle_classes.Bicycle("M4", 29.0, 474.98)
bike5 = bicycle_classes.Bicycle("M5", 26.0, 799.98)
bike6 = bicycle_classes.Bicycle("M6", 24.0, 975.98)

alpha_bikes = bicycle_classes.BikeShop("Alpha Bikes", [bike1, bike2, bike3, bike4, bike5, bike6])

customer1 = bicycle_classes.Customer("Customer1",200)
customer2 = bicycle_classes.Customer("Customer2",500)
customer3 = bicycle_classes.Customer("Customer3",1000)

print "\nInitial inventory:\n------------------"
print alpha_bikes.prettyInventory()

for customer in (customer1, customer2, customer3):
    print "Customer name:", customer.name
    print "Bikes in Budget:",
    bikes_in_budget = customer.affordable_bikes(alpha_bikes).keys()
    bikes_in_budget.sort()
    print ", ".join(bikes_in_budget) + "\n"

for customer in (customer1, customer2, customer3):
    bike_name = random.choice(customer.affordable_bikes(alpha_bikes).keys())
    customer.buy_bicycle(alpha_bikes,bike_name)

print "\nFinal inventory:\n----------------"
print alpha_bikes.prettyInventory()

print "\nProfit made: ${:.2f}".format(alpha_bikes.report_profit())
