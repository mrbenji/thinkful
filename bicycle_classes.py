from __future__ import (absolute_import, print_function, unicode_literals, division)
import re


def pretty_money(amount):
    """
    Return integer or float as US-currency-formatted string.
    Ex. 1289 -> "$1,289.00" and 75.98 -> "$75.98"

    Caveats:
    - Will not work properly if amount > 999,999.99
    - Requires "re" module

    :param amount: integer or float to format
    :returns: formatted string
    """
    return re.sub(r'(\d)+(\d\d\d)(\.\d\d$)', r'\1,\2\3', "${:.2f}".format(amount))


def pretty_table(data, padding=2):
    """
    "Pretty print" a table to a returned string, with cols as narrow as possible.

    :param data: nested list representing a table (list of rows that are each a list of columns)
    :param padding: minimum space to include between columns
    :return: a multi-line string containing a formatted table
    """
    error_string = "pretty_table() encountered a improperly-formatted table.\n"
    error_string += "Expected a list of rows, every row a list of the same number of columns.\n"

    return_string = ""

    # sanity check... is this a list of lists?
    if not (type(data) is list and type(data[0]) is list):
        return error_string

    col_widths = [0 for col in range(len(data[0]))]
    for row in data:

        # every row should have the same number of columns
        if len(row) != len(col_widths):
            return error_string

        col_num = 0

        for col in row:
            if len(col) > col_widths[col_num]:
                col_widths[col_num] = len(col)
            col_num += 1

    for row in data:
        col_num = 0
        for col in row:
            return_string += col.ljust(col_widths[col_num]+padding)
            col_num += 1
        return_string += "\n"

    return return_string


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

        data.append(["MFG", "Model", "Frame", "Wheels", "Weight", "Cost", "Price"])
        data.append(["---", "-----", "-----", "------", "------", "----", "-----"])

        for bike in self.inventory:
            data.append([
                bike.manufacturer,
                bike.model_name,
                bike.frame.name,
                bike.wheels.name,
                "{:.2f} lbs".format(bike.weight),
                pretty_money(bike.cost),
                pretty_money(self.price_plus_margin(bike.cost))
            ])

        return pretty_table(data)

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

    def most_expensive_affordable_bike(self, bike_shop):
        max_price = 0
        return_string = ""
        bike_dict = self.affordable_bikes(bike_shop)
        for key in bike_dict.keys():
            if bike_dict[key] > max_price:
                max_price = bike_dict[key]
                return_string = key

        return return_string

    def buy_bicycle(self, bike_shop, model_name):
        if bike_shop.sell_bicycle(self, model_name):
            print ("{} bought a Model {} bike from {} for".format(self.name, model_name, bike_shop.name), end=" ")
            # Need to access cost via bicycles_owned, not bike_shop.inventory, because bike object has been moved
            print ("{},".format(pretty_money(bike_shop.price_plus_margin(self.bicycles_owned[-1].cost))))
            print ("and now has {} remaining in their bike fund.\n".format(pretty_money(self.bike_fund)))

