#!/usr/bin/env python3
import sys

current_customer = None
order_data = []
review_data = []

for line in sys.stdin:
    customer_id, data = line.strip().split('\t', 1)

    #print(current_customer, customer_id, sep="|")
    if current_customer == customer_id:
        if data.startswith('O:'):
            order_data.append(data[2:])
        elif data.startswith('R:'):
            review_data.append(data[2:])
    else:
        if current_customer:
            for order in order_data:
                for review in review_data:
                    print(f'{current_customer}\t{order}\t{review}')
        current_customer = customer_id
        order_data = []
        review_data = []

if current_customer:
    for order in order_data:
        for review in review_data:
            print(f'{current_customer}\t{order}\t{review}')

