
t12345 = int(input('Enter a five-digit number: '))
tth, left = divmod(t12345, 10000)
th, left = divmod(left, 1000)
hdr, left = divmod(left, 100)
tens, left = divmod(left, 10)
result = left * 10000 + tens * 1000 + hdr * 100 + th * 10 + tth
print(result)
