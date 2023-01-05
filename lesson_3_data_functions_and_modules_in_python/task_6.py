# Given a sequence of N integers and the number K.
# It is necessary to shift the entire sequence (shift - cyclic)
# by |K| elements to the right if K is positive and to the left if negative.
# Example:
# input:  5
#         5 3 7 4 6
#         3
# output: 7 4 6 5 3

import random

while True:
    try:
        n = int(input("Enter an unsigned integer (from 1 to 100000) or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if 1 <= n <= 10**5:
            print(f"Number of elements: {n}")
            shift = random.randint(n * (-1), n)
            mylist = [random.randint(-100, 100) for i in range(n)]
            print(mylist)
            print(f"Shift: {shift}")
            newlist = [None] * n
            if shift > 0:
                for i in range(n):
                    j = n * (-1) + i + shift
                    newlist[j] = mylist[i]
            elif shift < 0:
                for i in range(n):
                    j = i + shift
                    newlist[j] = mylist[i]
            else:
                newlist = mylist
            print(newlist)
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")