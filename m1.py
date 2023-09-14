#!/usr/bin/env python3
import sys

# Mapper Stage 1

for line in sys.stdin: #input_file:
    data = line.strip().split('\t')
    record_type = data[0]
    if record_type == 'order':
        order_id, customer_id, product_id, quantity, price = data[1:]
        print(customer_id, product_id, quantity, record_type, sep="\t")

        #order_data.append((customer_id, product_id, quantity))

    elif record_type == 'review' and int(data[4]) < 3:
        review_id, product_id, customer_id, rating, review_text = data[1:]
        #review_data.add((customer_id, product_id,rating))
        print(customer_id, product_id, rating, record_type, sep="\t")

