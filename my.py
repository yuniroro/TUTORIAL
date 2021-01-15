for i in range(5):
	print(i)

word = 'apple'
for letter in word:
	print(letter)

for i, letter in enumerate(word):
	print(i, letter)

word2 = '12345'

for letter1, letter2 in zip(word, word2):
	print(letter1, letter2)