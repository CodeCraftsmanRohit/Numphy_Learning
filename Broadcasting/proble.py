'''
prices=[1100,200,300]

discount=10

final_prices=[]

for price in prices:
    final_price=price-(price * discount/100)
    final_prices.append(final_price)

print(final_prices)
'''

import numpy as np

prices =np.array([100,200,300])

discount=10

final_prices=prices-(prices*discount/100)
print(final_prices)