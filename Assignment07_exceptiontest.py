# ------------------------------------------------- #
# Title: exceptiontest.py
# Description: script for showing exception handling
# ChangeLog: (Who, When, What)
# KHarms,8.20.2023,created script
# ------------------------------------------------- #

first_num = None
second_num = None

try:
    # put the code that may cause exceptions in the try clause
    # the program will attempt to execute this clause first

    # get user input
    first_num = float(input('Please enter a number: '))
    second_num = float(input('Please enter another number: '))

    # Process and display sum, difference, product, quotient
    print(f'The product of  {first_num} and {second_num} is', first_num * second_num)
    print(f'The quotient of {first_num} and {second_num} is', first_num / second_num)

except ValueError as e:
    # when an exception is found the except clause will execute instead
    # tell the program how you want it to respond to a ValueError exception
    print('There was an error -- please enter numeric characters only')

except ZeroDivisionError as e:
    # tell the program how you want it to respond to a ZeroDivisionError exception
    print('There was an error -- cannot divide by 0')

except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')

input('Hit enter to exit program')
