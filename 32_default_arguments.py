# DEFUALT ARGUMENT = A default value for certain paramaters
#                   default is when the argument is omitted
#                   make your functions more flexible, reduces # of arguments
#                   1. positinal, 2. DEFAULT, 3. keyword, 4. arbitrary




'''
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
'''


'''
def net_price(list_price, discount=0, tax=0.05):           #Discount and tax setneme as DEFAULT, Tzn defaultne bude mít hodnotu kterou zadáme, pokud uživatel nezadá jinou, bude defaultní hodnota platná
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0, 0.2))
'''

# EXERCISE # - Count up timer

import time

def count(end, start=0, ):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
print("done")

count(30,15)