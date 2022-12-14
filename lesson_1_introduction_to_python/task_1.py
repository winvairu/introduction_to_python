# Write a program that accepts a digit indicating the day
# of the week as input and checks whether this day is a weekend.

while True:
    try:
        day_week = int(input("Enter the day of the week: " ))
    except ValueError:
        print("Error! It's not a number, try again.")
    else:
        match day_week:
            case 1:
                print('working day')
            case 2:
                print('working day')
            case 3:
                print('working day')
            case 4:
                print('working day')
            case 5:
                print('working day')
            case 6:
                print('weekend')
            case 7:
                print('weekend')
            case _:
                print('Invalid value.')
        break