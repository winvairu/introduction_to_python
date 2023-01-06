# The user enters a number,
# you need to output the number pi with the specified accuracy.

def input_validation():

    while True:
        try:
            n = int(input("Enter an unsigned integer (from 1 to 15) or enter 0 to exit: "))
        except ValueError:
            print("Error! Invalid value.")
        else:
            if 1 <= n <= 15:
                return n
            elif n == 0:
                break
            else:
                print("Error! Invalid value.")

def output_accuracy(a):
    pi = 3.141592653589793
    print(f"{pi:.{a}f}")

number = input_validation()
output_accuracy(number)