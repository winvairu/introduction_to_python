# Write a program that takes the coordinates of two points as input and
# finds the distance between them in 2D space.

while True:
    try:
        print("Enter the coordinates of point A (integers only, X ≠ 0, Y ≠ 0)")
        xa = int(input("A x = "))
        ya = int(input("A y = "))
        print("Enter the coordinates of point B (integers only, X ≠ 0, Y ≠ 0)")
        xb = int(input("B x = "))
        yb = int(input("B y = "))
    except ValueError:
        print("Error! Enter a number.")
    else:
        if xa == 0 or ya == 0 or xb == 0 or yb == 0:
            print("Error! Invalid value.")
        else:
            ab = float((((xb - xa) ** 2) + ((yb - ya) ** 2)) ** (0.5))
            print(f"Distance between two points: {ab:.2f}")
            break