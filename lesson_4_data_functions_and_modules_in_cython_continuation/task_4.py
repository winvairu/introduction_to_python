# Set the natural degree k.
# Generate a random list of coefficients (values from 0 to 100)
# of the polynomial and write a polynomial of degree k to the file.
# Example:
# - k = 2 => 2 * x² + 4 * x + 5 = 0 or x² + 5 = 0 or 10 * x² = 0

import random

def input_validation():

    while True:
        try:
            n = int(input("Enter the natural degree of the polynomial (from 2 to 9) or enter 0 to exit: "))
        except ValueError:
            print("Error! Invalid value.")
        else:
            if 2 <= n <= 9:
                return n
            elif n == 0:
                break
            else:
                print("Error! Invalid value.")

def create_polynomial(a):
    mylist1 = [chr(0x2070), chr(0x00B9), chr(0x00B2), chr(0x00B3), chr(0x2074),
    chr(0x2075), chr(0x2076), chr(0x2077), chr(0x2078), chr(0x2079)]
    mylist2 = [' + ', ' - ']
    print("{}x{}{}{}x{}{} = 0".format(random.randint(0, 100), mylist1[a], mylist2[random.randint(0, 1)],
    random.randint(0, 100), mylist2[random.randint(0, 1)], random.randint(0, 100)))

k = input_validation()
if k == None:
    print("The program is completed.")
    exit()
create_polynomial(k)