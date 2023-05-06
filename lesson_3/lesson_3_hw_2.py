
word = str(input('Enter string in snake_case style: '))
words = word.split('_')

for i in range(len(words)):
    words[i] = words[i].capitalize()

rez = ''.join(words)
print(rez)
