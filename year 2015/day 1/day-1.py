import math
import os
import random
import re
import sys

if __name__ == '__main__':

    # region data
    data = ""
    # endregion

    a = 0
    b = 1
    c = -1

    data.split(",")

    for item in data:
        if item == "(":
            a = a + b
            print(a)
        elif item == ")":
            a = a + c
            print(a)
