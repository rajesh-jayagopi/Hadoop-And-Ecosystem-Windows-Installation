#!/usr/bin/env python

import sys

# Mapper Stage 2
for line in sys.stdin: #input_file:
    product_id, order_count, review_sum = line.strip().split('\t')
    if int(review_sum) < 3:
        print(f"{product_id}\t{order_count}")

# Reducer Stage 2
current_product_id = None
total_orders = 0

for line in sys.stdin:
    product_id, order_count = line.strip().split('\t')

    if current_product_id != product_id:
        if current_product_id is not None:
            print(f"{current_product_id}\t{total_orders}")
        current_product_id = product_id
        total_orders = 0

    total_orders += int(order_count)

if current_product_id is not None:
    print(f"{current_product_id}\t{total_orders}")

