
t1234 = int(input('Enter a four-digit number: '))
thousands, left = divmod(t1234, 1000)
hundreds, left = divmod(left, 100)
tens, left = divmod(left, 10)
print(thousands, '\n', hundreds, '\n', tens, '\n', left, sep='')
