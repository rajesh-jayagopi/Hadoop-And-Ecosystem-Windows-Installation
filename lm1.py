#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    record_type, *fields = line
    customer_id = fields[1]
    product_id = fields[2]
    if record_type == 'order':
        key = (product_id, 'order')
    elif record_type == 'review':
        key = (product_id, 'review')
    values = '\t'.join(fields)
    print(key[0], key[1], values, sep="\t")

