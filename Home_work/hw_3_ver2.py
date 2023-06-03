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
    zp = 200
    prem = 200
    men_1 = int(input('Sales of the first manager: '))
    men_2 = int(input('Sales of the second manager: '))
    men_3 = int(input('Sales of the third manager: '))
    best = 'The best manager is the'
    other = 'Manger salary'

    if 500 < men_1:
        salary1 = zp + (men_1 * 3)/100
    else:
        if 500 < men_1 > 1000:
            salary1 = zp + (men_1 * 5)/100
        else:
            salary1 = zp + (men_1 * 8)/100
    if 500 < men_2:
        salary2 = zp + (men_2 * 3)/100
    else:
        if 500 < men_2 < 1000:
            salary2 = zp + (men_2 * 5)/100
        else:
            salary2 = zp + (men_2 * 5)/100
    if 500 < men_3:
        salary3 = zp + (men_3 * 3)/100
    else:
        if 500 < men_3 < 1000:
            salary3 = zp + (men_3 * 5)/100
        else:
            salary3 = zp + (men_3 * 8)/100
    if salary1 > salary2 and salary1 > salary3:
        print(f'{best} first manager!')
    elif salary2 > salary1 and salary2 > salary3:
        print(f'{best} second manager!')
    else:
        print(f'{best} third manager!')
    print(f'''{other} first {salary1} \n{other} second {salary2} \n{other} third {salary3}''')
except ValueError:
    print('You only need to enter the digits!')

