n = input("Enter a three-digit number: ")
n = int(n)

l, left = divmod(n, 100)
m, left = divmod(left, 10)

print('The Sum = ', l + m + left)
