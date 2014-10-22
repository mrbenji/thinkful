#!/bin/env python

def calculate_discount(item_cost, relative_discount, absolute_discount):
    total_discount = float(item_cost) * (1/float(relative_discount))
    total_discount += float(absolute_discount)
    return float(item_cost) - total_discount


def main():
    item_cost_in = raw_input("Enter the cost of the item: ")
    relative_discount_in = raw_input("Enter the relative discount percentage: ")
    absolute_discount_in = raw_input("Enter additional discount in dollars: ")
    print "${:,.2f}".format(calculate_discount(item_cost_in, relative_discount_in, absolute_discount_in))


if __name__ == "__main__":
    main()
