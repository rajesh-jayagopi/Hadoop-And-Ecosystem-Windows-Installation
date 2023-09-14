#!/usr/bin/env python
# Reducer Stage 1

import sys

order_data = []
review_data = []
current_product_id = None
order_count = 0
review_sum = 0

for line in sys.stdin:
    record_type, customer_id, product_id, value = line.strip().split('\t')
    if record_type

    if current_product_id != 
    product_id:
        if current_product_id is not None:
            print(f"{current_product_id}\t{order_count}\t{review_sum}")
        current_product_id = product_id
        order_count = 0
        review_sum = 0
    
    if record_type == 'order':
        order_count += int(value)
    elif record_type == 'review':
        review_sum += int(value)

if current_product_id is not None:
    print(f"{current_product_id}\t{order_count}\t{review_sum}")
