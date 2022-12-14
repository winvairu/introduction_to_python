# Write a program that, according to a given number of quarters,
# shows the range of possible coordinates of points in this quarter (x and y).

while True:
    try:
        a = int(input("Enter the number of the coordinate quarter: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        match a:
            case 1:
                print("X > 0, Y > 0")
            case 2:
                print("X > 0, Y < 0")
            case 3:
                print("X < 0, Y < 0")
            case 4:
                print("X < 0, Y > 0")
            case _:
                print("Error! Invalid value.")
        break