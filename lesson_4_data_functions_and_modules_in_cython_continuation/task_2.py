# Set the natural number N.
# Write a program that will make a list of prime factors of the number N.

def input_validation():

    while True:
        try:
            n = int(input("Enter an unsigned integer (from 1 to 100000) or enter 0 to exit: "))
        except ValueError:
            print("Error! Invalid value.")
        else:
            if 1 < n <= 10**5:
                return n
            elif n == 0:
                break
            else:
                print("Error! Invalid value.")

def simple_multiplier(a):
    if a == None:
        print("The program is completed.")
        exit()
    while a > 1:
        if a % 2 == 0:
            a = a // 2
            print("2 ", end = '')
        elif a % 3 == 0:
            a = a // 3
            print("3 ", end = '')
        elif a % 5 == 0:
            a = a // 5
            print("5 ", end = '')
        elif a % 7 == 0:
            a = a // 7
            print("7 ", end = '')
        elif a // a == 1:
            print(f"{a}", end = '')
            a = a // a

number = input_validation()
simple_multiplier(number)