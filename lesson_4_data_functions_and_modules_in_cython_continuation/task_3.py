# Set a sequence of numbers.
# Write a program that outputs a list of non-repeating elements of the original sequence.

import random
def input_validation():

    while True:
        try:
            n = int(input("Enter an unsigned integer (from 1 to 100) or enter 0 to exit: "))
        except ValueError:
            print("Error! Invalid value.")
        else:
            if 1 <= n <= 100:
                return n
            elif n == 0:
                break
            else:
                print("Error! Invalid value.")

def create_list(a):
    mylist = [random.randint(-15, 15) for i in range(a)]
    print(mylist)
    return mylist

def nonrepeating_elements(a):
    new_list = []
    for i in range(len(a)):
        b = a[i]
        count = 0
        for j in range(len(a)):
            if b == a[j]:
                count += 1
        if count == 1:
            new_list.append(b)
    print(new_list)

number = input_validation()
if number == None:
    print("The program is completed.")
    exit()
my_list = create_list(number)
print("Non-repeating elements:")
nonrepeating_elements(my_list)