# It is required to find the smallest natural divisor of an integer N other than 1.

# input: 15, 35.
# output: 3, 5.

while True:
    try:
        n = int(input("Enter the number of coins (from 2 to 1000000) or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if 1 < n <= 1000000:
            min = 0
            for i in (range(2, n + 1)):
                if n % i == 0:
                    min = i
                    break
            print(f"The smallest natural divisor of an integer {n}: {min}")
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")