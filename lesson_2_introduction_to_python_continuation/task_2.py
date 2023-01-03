# It is required to calculate the sum of integers located between the numbers 1 and N inclusive.

while True:
    try:
        n = int(input("Enter the number of coins (from 1 to 10000) or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if 1 <= n <= 10000:
            sum = 0
            for i in (range(1, n + 1)):
                sum += i
            print(sum)
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")