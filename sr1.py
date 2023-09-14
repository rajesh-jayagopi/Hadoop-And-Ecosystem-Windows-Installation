#!/usr/bin/env python3
import sys
import string

last_customer_id = None
orders = []
reviews = []
current_quantity = 0

for line in sys.stdin:
    line = line.strip()
    customer_id, product_id, quantity, record_type = line.split("\t")
    # if this is the first iteration
    #print(last_customer_id, customer_id, product_id, quantity, record_type, sep='|')
    if last_customer_id != customer_id:
        if last_customer_id is not None:
            for order in orders:
                print (customer_id, product_id,quantity, "order", sep="\t")
            for review in reviews:
                print (customer_id, product_id,quantity, "review", sep="\t")
        last_customer_id = customer_id
        orders = []
        reviews = []
        #current_quantity = int(quantity)
    if record_type == 'order':
        orders.append(f'{product_id}\t{quantity}\torder')
    elif record_type == 'review':
        reviews.append(f'{product_id}\t{quantity}\treview')
    #elif customer_id == last_customer_id:
      #  quantity = current_quantity
     #   print (product_id,quantity, sep="\t")

if last_customer_id is not None:
    for order in orders:
        print(last_customer_id, order, 'order_test', sep="\t")
        pass
    for review in reviews:
        print(last_customer_id, review, 'review_test', sep="\t")
        pass

