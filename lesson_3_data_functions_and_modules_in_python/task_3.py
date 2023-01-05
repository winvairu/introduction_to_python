# Set a list of real numbers.
# Write a program that will find the difference between the maximum and
# minimum values of the fractional part of the elements.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

while True:
    try:
        n = int(input("Enter the number of list items or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if n > 0:
            mylist = [random.randint(0, 99999) / 1000 for i in range(n)]
            print(mylist)
            min = mylist[0] % 1
            max = mylist[0] % 1
            for i in range(n):
                if mylist[i] % 1 > max:
                    max = mylist[i] % 1
                elif mylist[i] % 1 < min:
                    min = mylist[i] % 1
            print(f"Minimum: {min:.3f}")
            print(f"Maximum: {max:.3f}")
            print("Difference: {:.3f}" .format(max - min))
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")