class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost

    def sell_bicycle(self, customer):
        pass

class BikeShop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def sell_bicycle(self, margin):
        pass

    def calc_profit(self):
        pass

class Customer(object):
    def __init__(self, name, bike_fund):
        self.name = name


