from __future__ import (absolute_import, print_function, unicode_literals, division)


class Wheel(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = float(weight)
        self.cost = cost


class Frame(object):
    def __init__(self, name, material, weight, cost):
        self.name = name
        self.material = material
        self.weight = float(weight)
        self.cost = cost


class Bicycle(object):
    def __init__(self, model_name, wheel_type, frame, manufacturer):
        self.model_name = model_name
        self.wheels = wheel_type
        self.frame = frame
        self.manufacturer = manufacturer

        self.cost = frame.cost + wheel_type.cost*2
        self.weight = frame.weight + wheel_type.weight*2


class BicycleManufacturer(object):
    def __init__(self, name, margin, models_sold):
        self.name = name
        self.margin = margin
        self.models_sold = models_sold


class BikeShop(object):

    margin = 0.2
    profit_made = 0.0

    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def price_plus_margin(self, price):
        return price + price * self.margin

    def add_profit(self, cost):
        self.profit_made += cost * self.margin

    def check_inventory(self, model_name):
        for next_bike in self.inventory:
            if next_bike.model_name == model_name:
                return next_bike
        return None

    def sell_bicycle(self, customer, model_name):
        for next_bike in self.inventory:
            if (next_bike.model_name == model_name) and (customer.bike_fund > self.price_plus_margin(next_bike.cost)):
                self.inventory.remove(next_bike)
                customer.bike_fund -= self.price_plus_margin(next_bike.cost)
                customer.bicycles_owned.append(next_bike)
                self.add_profit(next_bike.cost)
                return True
        return False

    def report_profit(self):
        return self.profit_made

    def prices(self):
        return_dict = {}
        for next_bike in self.inventory:
            return_dict[next_bike.model_name] = self.price_plus_margin(next_bike.cost)
        return return_dict

    def pretty_inventory(self):
        data = []
        return_string = ""

        data.append(["Model", "Frame", "Wheels", "Weight", "Cost", "Price"])
        data.append(["-----", "-----", "------", "------", "----", "-----"])

        for bike in self.inventory:
            data.append([
                bike.model_name,
                bike.frame.name,
                bike.wheels.name,
                "{:.2f} lbs".format(bike.weight),
                "${:.2f}".format(bike.cost),
                "${:.2f}".format(self.price_plus_margin(bike.cost))
            ])

        col_width = 0
        for row in data:
            for col in row:
                if len(col) > col_width:
                    col_width = len(col)

        for row in data:
            return_string = return_string + "".join(col.ljust(col_width + 3) for col in row) + "\n"

        return return_string


class Customer(object):
    bicycles_owned = []

    def __init__(self, name, bike_fund):
        self.name = name
        self.bike_fund = float(bike_fund)

    def affordable_bikes(self, bike_shop):
        return_dict = {}
        price_dict = bike_shop.prices()
        for next_bike_name in price_dict:
            if price_dict[next_bike_name] <= self.bike_fund:
                return_dict[next_bike_name] = price_dict[next_bike_name]
        return return_dict

    def buy_bicycle(self, bike_shop, model_name):
        if bike_shop.sell_bicycle(self, model_name):
            print ("{} bought a Model {} bike from {} for".format(self.name, model_name, bike_shop.name), end=" ")
            # Need to access cost via bicycles_owned, not bike_shop.inventory, because bike object has been moved
            print ("${:.2f},".format(bike_shop.price_plus_margin(self.bicycles_owned[-1].cost)))
            print ("and now has ${0:.2f} remaining in their bike fund.\n".format(self.bike_fund))

