class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost


class BikeShop(object):

    margin = 0.2
    profit_made = 0.0

    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def price_plus_margin(self, price):
        return float(price) + float(price) * self.margin

    def add_profit(self, price):
        self.profit_made += self.price_plus_margin(price) - price

    def check_inventory(self, model_name):
        for nextBike in self.inventory:
            if nextBike.model_name == model_name:
                return nextBike
        return None

    def sell_bicycle(self, customer, model_name):
        for nextBike in self.inventory:
            if (nextBike.model_name == model_name) and (customer.bike_fund > self.price_plus_margin(nextBike.cost)):
                self.inventory.remove(nextBike)
                customer.bike_fund -= self.price_plus_margin(nextBike.cost)
                customer.bicycles_owned.append(nextBike)
                self.add_profit(nextBike.cost)
                return True
        return False

    def report_profit(self):
        return self.profit_made

    def prices(self):
        return_dict = {}
        for nextBike in self.inventory:
            return_dict[nextBike.model_name] = self.price_plus_margin(nextBike.cost)
        return return_dict

    def prettyInventory(self):
        returnString = ""
        for bike in self.inventory:
            returnString = returnString + "Model: {} | Weight: {}lbs | Cost: ${:.2f} | Price: ${:.2f}\n".format(bike.model_name, bike.weight, bike.cost, self.price_plus_margin(bike.cost))
        return returnString

class Customer(object):
    bicycles_owned = []

    def __init__(self, name, bike_fund):
        self.name = name
        self.bike_fund = float(bike_fund)

    def affordable_bikes(self,bikeShop):
        return_dict = {}
        price_dict = bikeShop.prices()
        for next_bike_name in price_dict:
            if price_dict[next_bike_name] <= self.bike_fund:
                return_dict[next_bike_name] = price_dict[next_bike_name]
        return return_dict

    def buy_bicycle(self,bikeShop,model_name):
        if bikeShop.sell_bicycle(self,model_name):
            print "{} bought a Model {} bike from {} for".format(self.name, model_name, bikeShop.name),
            # Need to access cost via bicycles_owned, not bikeShop.inventory, because bike object has been moved
            print "${:.2f},".format(bikeShop.price_plus_margin(self.bicycles_owned[-1].cost))
            print "and now has ${0:.2f} remaining in their bike fund.\n".format(self.bike_fund)

