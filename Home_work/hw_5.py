# Exercise 1
#
# n = [1, -2, 3, -1, 4, 12, -34, 23, 652]
# sum_neg = 0
# sum_even = 0
# sum_proizv_indx = 1
# sum_first_last_poz = 0
#
# for i in n:
#     if i < 0:
#         sum_neg += i
# print('Sum of negative digits is', sum_neg)
#
# for i in n:
#     if i % 2 == 0:
#         sum_even += i
# print('Sum of even numbers is', sum_even)
#
# for i in n:
#     if i % 3 == 0:
#         sum_proizv_indx *= i
# print('Product of elements with indices divisible by three is', sum_proizv_indx)
#
# print('Sum of even min and max numbers is', min(n) * max(n))
#
# for i in n:
#     if i > 0:
#         sum_first_last_poz += i
# print('The sum of the elements between the first and last positive elements is', sum_first_last_poz)

#########################################################

# Exercise 2

# n = [1, -2, 3, -1, 4, 12, -34, 23, 652]
#
# even_numbers = []
# odd_numbers = []
# negative_numbers = []
# positive_numbers = []
#
# for i in n:
#     if i % 2 == 0:
#         even_numbers.append(i)
# print('Even list numbers', even_numbers)
#
# for i in n:
#     if i % 2 > 0:
#         odd_numbers.append(i)
# print('Odd list numbers is', odd_numbers)
#
# for i in n:
#     if i < 0:
#         negative_numbers.append(i)
# print('Negative list numbers is', negative_numbers)
#
# for i in n:
#     if i > 0:
#         positive_numbers.append(i)
# print('Positive list numbers is', positive_numbers)
