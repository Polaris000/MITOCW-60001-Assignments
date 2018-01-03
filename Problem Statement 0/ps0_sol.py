"""
## ps0
## Name-Polaris000
## Time-1 min

Take user input for numbers x and y
Print x ** y
Print log2(x) (base2)
"""


import numpy as np
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

print("x**y = ", x ** y)
print("log(x) =", np.log2(x))
