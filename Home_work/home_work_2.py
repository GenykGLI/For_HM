# Exercise 1

digit_1 = int(input('Enter first digit:  '))
digit_2 = int(input('Enter first second: '))
digit_3 = int(input('Enter first third:  '))
user_choice = int(input('''Choose priority function:
for maximum input    1 
for minimum input    2 
for midl_arifm input 3
'''))

if user_choice == 1:
    print(f'Maximum of three digit = {digit_1 + digit_2 + digit_3}')
elif user_choice == 2:
    print(f'Minimum of three digit = {digit_1 - digit_2 - digit_3}')
elif user_choice == 3:
    print(f'Minimum of three digit = {(digit_1 * digit_2 * digit_3)/3}')
else:
    print('Invalid value entered!')
