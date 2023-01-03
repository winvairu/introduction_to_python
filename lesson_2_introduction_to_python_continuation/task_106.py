#There are n coins on the table. Some of them are tails up, and some are coats of arms.
#Determine the minimum number of coins that need to be turned over so that all the coins are turned up with the same side.

# input: 5 -> 1 0 1 1 0
# output: 2

import random

while True:
    try:
        n = int(input("Enter the number of coins (from 1 to 100) or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if 1 <= n <= 100:
            count1 = 0
            count2 = 0
            for i in range(n):
                coin = random.randint(0, 1)
                print(f"{coin} ", end = '')
                if coin == 0:
                    count1 += 1
                else:
                    count2 += 1
            if count1 < count2:
                print()
                print(f"Minimum number of coins: {count1}")
            else:
                print()
                print(f"Minimum number of coins: {count2}")
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")