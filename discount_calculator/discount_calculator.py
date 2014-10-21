#!/bin/env python

def calculate_discount(item_cost, relative_discount, absolute_discount):
    total_discount = item_cost * (1/relative_discount)
    total_discount += absolute_discount
    return item_cost - total_discount

