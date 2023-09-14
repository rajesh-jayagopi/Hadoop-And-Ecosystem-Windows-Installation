#!/usr/bin/env python

import sys

# Mapper Stage 3
for line in sys.stdin: #input_file:
    product_id, order_count = line.strip().split('\t')
    print(f"{order_count}\t{product_id}")

# Reducer Stage 3
top_product_ids = []
top_order_count = 0

for line in sys.stdin:
    order_count, product_id = line.strip().split('\t')
    order_count = int(order_count)

    if order_count > top_order_count:
        top_product_ids = [product_id]
        top_order_count = order_count
    elif order_count == top_order_count:
        top_product_ids.append(product_id)

for product_id in top_product_ids:
    print(f"{product_id}\t{top_order_count}")

