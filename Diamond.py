# CodeWars Give me a Diamond

import statistics


def diamond(n):
    # Make some diamonds!
    # return "*"
    return "".join(
        " " * (n // 2) + i * "*" + "\n"
        for i in range(1, n)
        for i in reversed(range(1, n + 1))
    )

    # return " " * (n) + "*\n"


print(diamond(7))

"""


   *
  ***
 *****
******* 7
 *****
  ***
   *


       *
      ***
     *****
    *******
   *********
  ***********
 *************
*************** 15
 *************
  ***********
   *********
    *******
     *****
      ***
       *

print(diamond(1))
print(diamond(2))
print(diamond(3))
print(diamond(5))
print(diamond(0))
print(diamond(-3))

"""
