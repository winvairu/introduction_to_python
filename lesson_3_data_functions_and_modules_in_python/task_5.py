# Set a number.
# Make a list of Fibonacci numbers, including for negative indices.
# Example:
# - for k = 8, the list will look like this: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

while True:
    try:
        n = int(input("Enter an unsigned integer or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if n > 0:
            mylist = [1, 0, 1]
            a = mylist[1]
            a1 = mylist[1]
            b = mylist[2]
            b1 = mylist[0]
            for i in range(1, n):
                c = a + b
                c1 = a1 - b1
                a = b
                a1 = b1
                b = c
                b1 = c1
                mylist.append(b)
                mylist.insert(0, b1)
            print(mylist)
        elif n == 0:
            break
        else:
            print("Error! Invalid value.")