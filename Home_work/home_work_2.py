# # Exercise 1
#
# digit_1 = int(input('Enter first digit:  '))
# digit_2 = int(input('Enter first second: '))
# digit_3 = int(input('Enter first third:  '))
# user_choice = int(input('''Choose priority function:
# for maximum input    1
# for minimum input    2
# for midl_arifm input 3
# '''))
#
# if user_choice == 1:
#     print(f'Maximum of three digit = {digit_1 + digit_2 + digit_3}')
# elif user_choice == 2:
#     print(f'Minimum of three digit = {digit_1 - digit_2 - digit_3}')
# elif user_choice == 3:
#     print(f'Minimum of three digit = {(digit_1 * digit_2 * digit_3)/3}')
# else:
#     print('Invalid value entered!')
#
# Exercise 2

user_metr = int(input('Enter the required number of meters: '))
user_choice = int(input('''What do you want to do:
Сonvert to miles, then choose  1
Сonvert to inches, then choose 2
Сonvert to yards, then choose  3
'''))

if user_choice == 1:
    print(round(user_metr * 0.6, 2))
elif user_choice == 2:
    print(round(user_metr * 39.37, 2))
elif user_choice == 3:
    print(round(user_metr * 1.09, 2))
else:
    print('Invalid value entered!')

