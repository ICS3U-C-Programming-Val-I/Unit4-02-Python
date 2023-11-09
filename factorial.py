#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 9, 2023
# This program asks the user to enter a positive number.
# It then uses a while true loop to multiply all the whole numbers
# starting from 1, until that number and display the factorial to the user.


def main():
    user_num_str = input("Enter a number: ")
    factorial = 1
    counter = 0

    try:
        user_num_int = int(user_num_str)
        if user_num_int < 0:
            print("Enter a positive number")
        else:
            while True:
                counter = counter + 1
                factorial = factorial * counter
                if counter >= user_num_int:
                    break
            print(f"{user_num_int}! = {factorial}")
    except ValueError:
        print(f"{user_num_str} is not a number")


if __name__ == "__main__":
    main()
