# Petya first came to a physical education lesson at a new school.
# Before the start of the lesson, students are lined up by height,
# in the order of non-growth.
# Write a program that will determine which place in the row Petya needs
# to stand in order not to break the tradition,
# if the growth of each student is known in advance and
# these data are already arranged according to non-growth (that is,
# each next number is no greater than the previous one).
# If there are several students in the class with the same height as Petya,
# then the program should place him after them.

# input: 8
#        165 163 160 160 157 157 155 154
#        162
#
# output: 3

import random

while True:
    try:
        n = int(input("Enter the number of students in the class (from 1 to 100) or enter 0 to exit: "))
    except ValueError:
        print("Error! Invalid value.")
    else:
        if 1 <= n <= 100:
            position = 1
            height_students = 200
            petya_height = random.randint(150, 200)
            for i in (range(1, n + 1)):
                height_students = random.randint(height_students - 2, height_students)
                if petya_height <= height_students:
                    position = i + 1
                print(f"{height_students} ", end = '')
            print()
            print(f"Petya's height is: {petya_height} cm")
            print(f"Petya's number in the line of students: {position}")
        elif n == 0:
            print("The program is completed.")
            break
        else:
            print("Error! Invalid value.")