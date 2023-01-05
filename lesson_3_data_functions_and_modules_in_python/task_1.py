# Set a list of several numbers.
# Write a program that will find the sum of the list items standing in an odd position.

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
            s = 0
            for i in range(n):
                if i % 2 > 0:
                    s += mylist[i]
                    print(f"{mylist[i]} ", end = '')
            print()
            print(s)
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")