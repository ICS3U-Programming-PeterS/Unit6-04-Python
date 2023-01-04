#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 2, 2023
# This program uses 2 loops (a loop inside a loop) to generate
# random numbers between 1 and 50 and display them to the user.
# It then places the numbers into the 2D array
import math
import random
import constants


# Function to calculate the average of all values in the array
def calc_average(array, row, column):
    # Initialize sum and number of numbers to zero
    sum = 0
    num_numbers = 0
    # Loop through all elements in the array and add their values to the sum
    # Increment the number of numbers by 1 for each element
    for i in range(row):
        for j in range(column):
            sum += array[i][j]
            num_numbers += 1

    # Calculate the average by dividing the sum by the number of numbers
    average = sum / num_numbers
    return average


def main():
    MAX_NUM = 50
    # get 2D array size and try catch
    rows_str = input("How many row would you like: ")

    try:
        rows = int(rows_str)
        columns_str = input("How many columns would you like: ")

        try:
            columns = int(columns_str)

        except Exception:
            print("Enter an integer for how many columns.")

    except Exception:
        print("Enter an integer for how many rows.")

    # Initialize 2D array
    array = [[0] * columns for i in range(rows)]

    # Populate array with random numbers
    for i in range(rows):
        for j in range(columns):
            random_number = random.randint(constants.MIN_NUM, MAX_NUM)
            array[i][j] = random_number
            print(random_number, end="\t")
        print()

    # Calculate and print average of array elements
    average = calc_average(array, rows, columns)
    print(f"The average is: {average}")


if __name__ == "__main__":
    main()
