from collections import Counter

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 'a', 7]

print(Counter(mylist))

print(Counter('asdsadqwesadsss'))

sentence = "How many times does each letter show up"

print(Counter(sentence))
print(Counter(sentence.split()))
print(Counter(sentence.lower().split()))

letters = 'aaaaaaabbbbbbbbbbcccccccccccccddddddddddd'

c = Counter(letters)

print(c.most_common(2))  # TShe number is , the 2 most common letters in this case

print(list(c))

