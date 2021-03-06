#!/bin/env python

from __future__ import division
import argparse, sys


def calculate_discount(item_cost, relative_discount, absolute_discount):

    item_cost = float(item_cost)
    relative_discount = float(relative_discount)
    absolute_discount = float(absolute_discount)

    if relative_discount > 0.00:
        discount = item_cost * float(relative_discount/100)
    else:
        discount = 0.00

    if absolute_discount > 0.00:
        discount += absolute_discount

    discounted_price = item_cost - discount

    if discounted_price < 0.00:
        return 0.0
    else:
        return round(discounted_price,2)


def make_parser():
    """ Construct the command line parser """
    description = "Discount calculator"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("cost", type=float, help="item cost")
    parser.add_argument('-rd', '--relative-discount', type=float, help="discount by a percentage")
    parser.add_argument('-ad', '--absolute-discount', type=float, help="discount by a dollar amount")

    return parser


def main():
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)

    relative_discount_in = 0.0
    absolute_discount_in = 0.0

    item_cost_in = arguments["cost"]

    if arguments["relative_discount"]:
        relative_discount_in = arguments["relative_discount"]
    if arguments["absolute_discount"]:
        absolute_discount_in = arguments["absolute_discount"]

    print "${:,.2f}".format(calculate_discount(item_cost_in, relative_discount_in, absolute_discount_in))


if __name__ == "__main__":
    main()
