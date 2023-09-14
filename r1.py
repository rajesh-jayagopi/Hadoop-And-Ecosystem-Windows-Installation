#!/usr/bin/env python3

import sys

# Mapper Reduce 1
#!/usr/bin/env python3

current_customer = None
order_data = []
review_data = []

for line in sys.stdin:
    customer_id, product_id, value, record_type = line.strip().split('\t')

    if current_customer == customer_id:
        if record_type == "order":
            order_data.append(value)
            print(str(order_data))
        elif  record_type == "review":
            review_data.append(value)
            print(str(review_data))
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

