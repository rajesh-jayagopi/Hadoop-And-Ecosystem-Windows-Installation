#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys

# Mapper Stage 1
order_data = []
review_data = set()

for line in sys.stdin: #input_file:
    data = line.strip().split('\t')
    record_type = data[0]
    if record_type == 'order':
        order_id, customer_id, product_id, quantity, price = data[1:]
        print(f"order\t{customer_id}\t{product_id}\t{quantity}")
        
        order_data.append((customer_id, product_id, quantity))

    elif record_type == 'review' and int(data[4]) < 3:
        review_id, product_id, customer_id, rating, review_text = data[1:]
        review_data.add((customer_id, product_id,rating))
        print(f"review\t{customer_id}\t{product_id}\t{rating}")

#print(str(order_data))
#print(str(review_data))
result = {}
for order in order_data:
    for review in review_data:
        if(
                order[0] == review[0]
                and order[1] == review[1]
          ):
            print(f"{order[0]=}, {review[0]=}, {order[1]=}, {review[1]=}, {order[2]=} ")
            if order[1] in result:
                result[order[1]] += int(order[2])
            else:
                result[order[1]] = int(order[2])
            print(f"{result=}")
print(str(result))
for product_id, total_quantity in sorted(result.items()):
    #print(f"{product_id}\t{total_quantity}")
    pass





