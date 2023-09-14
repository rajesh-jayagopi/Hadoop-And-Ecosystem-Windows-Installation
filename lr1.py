#!/usr/bin/env python3
import sys

current_product_id = None
orders = []
reviews = []

for line in sys.stdin:
    line = line.strip().split('\t')
    product_id, record_type, *fields = line
    values = '\t'.join(fields)
    
    if current_product_id != product_id:
        if current_product_id is not None:
            for order in orders:
                print(f"{current_product_id}\t{order}")
            for review in reviews:
                print(f"{current_product_id}\t{review}")
        
        current_product_id = product_id
        orders = []
        reviews = []

    if record_type == 'order':
        orders.append(f'order\t{values}')
    elif record_type == 'review':
        reviews.append(f'review\t{values}')

# Output the remaining records
if current_product_id is not None:
    for order in orders:
        print(f"{current_product_id}\t{order}")
    for review in reviews:
        print(f"{current_product_id}\t{review}")

