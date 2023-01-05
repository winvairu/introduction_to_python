# Write a program that will convert a decimal number to binary.
# Example:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

while True:
    try:
        n = int(input("Enter an unsigned integer or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if n > 0:
            print(format(n, 'b'))
            # or
            mylist = []
            i = 0
            while n > 0:
                n2 = n % 2
                n = n // 2
                mylist.append(n2)
            for i in range(len(mylist)):
                print(mylist[-1 - i], end = '')
            print()
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")