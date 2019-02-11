'''
n为正多边形
'''
import numpy as np
from decimal import *


# 内割6边形，每次递增6边
def pi(n):
    y = Decimal(1.0)
    for i in range(n):
        pi = Decimal(3) * Decimal(2) ** Decimal(i) * Decimal(y)
        print(6 + 6 * i, '边形, PI: ', pi)
        y = (Decimal(2) - (Decimal(4) - y ** Decimal(2)) ** Decimal(0.5)) ** Decimal(0.5)
    return pi


print(getcontext())
getcontext().prec = 50  # 提高精度

print(pi(50))
print(np.pi)
