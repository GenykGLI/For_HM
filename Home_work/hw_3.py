# Exercise 1
#
# try:
#     user_choice = int(input('Enter the number of the day in the week: '))
#     day1, day2, day3, day4 = 'Monday', 'Tuesday', 'Wednesday', 'Thursday'
#     day5, day6, day7 = 'Friday', 'Saturday', 'Sunday'
#     reduction = 'Your chosen day is '
#
#     if user_choice == 1:
#         print(f'{reduction + day1}')
#     elif user_choice == 2:
#         print(f'{reduction + day2}')
#     elif user_choice == 3:
#         print(f'{reduction + day3}')
#     elif user_choice == 4:
#         print(f'{reduction + day4}')
#     elif user_choice == 5:
#         print(f'{reduction + day5}')
#     elif user_choice == 6:
#         print(f'{reduction + day6}')
#     elif user_choice == 7:
#         print(f'{reduction + day7}')
#     else:
#         print('There is no day of the week under this number!')
# except ValueError:
#     print('You got a ValueError')

# Exercise 2

# try:
#     digit_1 = int(input('Enter the first digit: '))
#     digit_2 = int(input('Enter the second digit: '))
#     text = 'Ascending numbers'
#     if digit_1 == digit_2:
#         print('The input numbers are equal', digit_1, 'and',  digit_2)
#     else:
#         print(text, min(digit_1, digit_2), 'and', max(digit_1, digit_2))
# except ValueError:
#     print('You got a ValueError')
# else:
#     print('Anyway you did a good job! ;)')


# Exercise 3
#
# try:
#     first_digit = int(input('Enter the first digit: '))
#     operation = input('Enter the operation for calculation +, -, / or *:  ')
#     second_digit = int(input('Enter the second digit: '))
#
#     if operation == '+':
#         print(first_digit + second_digit)
#     elif operation == '-':
#         print(first_digit - second_digit)
#     elif operation == '/':
#         print(first_digit / second_digit)
#     elif operation == '*':
#         print(first_digit * second_digit)
#     else:
#         print('Wrong operation for calculation!')
# except ValueError:
#     print('error ValueError')
# except ZeroDivisionError:
#     print('error ZeroDivision')
