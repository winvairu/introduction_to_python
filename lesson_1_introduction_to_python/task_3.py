# Write a program that takes the coordinates of a point (X and Y) as input,
# with X ≠ 0 and Y ≠ 0 and outputs the number of the quarter of the plane in
# which this point is located (or on which axis it is located).

print("Enter the coordinates of the point (only integers and X ≠ 0, Y ≠ 0):")
while True:
    try:
        x = int(input("X = "))
        y = int(input("Y = "))
    except ValueError:
        print("Error!")
    else:
        if x == 0 or y == 0:
            print("The value of X or Y cannot be zero.")
        if x > 0 and y > 0:
            print("The point is in the first quarter.")
        if x > 0 and y < 0:
            print("The point is in the second quarter.")
        if x < 0 and y < 0:
            print("The point is in the third quarter.")
        if x < 0 and y > 0:
            print("The point is in the third quarter.")
        break