# Write a program that finds the product of pairs of numbers in the list.
# We consider the first and last element as a pair, the second and penultimate, etc.
#
# Example:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15].

import random

while True:
    try:
        n = int(input("Enter the number of list items or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if n > 0:
            mylist = [random.randint(0, 99) for i in range(n)]
            print(mylist)
            j = 0
            if len(mylist) % 2 == 0:
                j = len(mylist) // 2
            else:
                j = len(mylist) // 2 + 1
            product = 0
            for i in range(j):
                product = mylist[i] * mylist[-1 - i]
                print(f"{product} ", end = '')
            print()
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")