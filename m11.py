#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    #print(len(data), data[0])
    record_type = data[0]
    if record_type == 'order':
        customer_id, product_id, quantity = data[2], data[3], data[4]
        print(f'{customer_id}\tO:{product_id}:{quantity}')
    elif record_type == 'review':
        customer_id, product_id, rating = data[3], data[2], data[4]
        print(f'{customer_id}\tR:{product_id}:{rating}')

