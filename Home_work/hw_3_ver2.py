# Exercise 1
#
# try:
#     user_digit = int(input('Enter the digit to be raised to the power: '))
#
#     degree = (((
#         user_digit ** 0, user_digit ** 1, user_digit ** 2, user_digit ** 3,
#         user_digit ** 4, user_digit ** 5, user_digit ** 6, user_digit ** 7
#     )))
#     print(f'Your digit to the power of 0 to 7 {degree}')
# except ValueError:
#     print('You are entering an invalid value!')

# Exercise 2

# try:
#     life = int(input('Price of Life for calling per minute: '))
#     vodafone = int(input('Price of Vodafone for calling per minute: '))
#     time_call = int(input('''How much minutes you want to call? Enter: '''))
#     user_choice = int(input('''Which operator:
#     if life -> Vodafone choose 1
#     if Vodafone -> Life choose 2
#     Your choice: '''))
#     x = 'Price for calling is'
#     if user_choice == 1:
#         print(x, time_call * life)
#     elif user_choice == 2:
#         print(x, time_call * vodafone)
#     else:
#         print('Incorrect choice! Must be 1 or 2')
# except ValueError:
#     print('Incorrect symbol! Must be only digits!')


# Exercise 3

try:
    zp_men = 200
    prem_men = 200
    men_1 = int(input('Sales of the first manager: '))
    men_2 = int(input('Sales of the second manager: '))
    men_3 = int(input('Sales of the third manager: '))

    if men_1 <= 500:
        print(round(200 + (men_1 * 3)/100, 2))
    elif 500 < men_1 <= 1000:
        print(round(200 + (men_1 * 5)/100, 2))
    elif 1000 < men_1:
        print(round(200 + (men_1 * 8)/100, 2))


except ValueError:
    print('You only need to enter numbers!')

