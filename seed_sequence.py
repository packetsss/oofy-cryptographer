import random

random.seed(2)
word_bag = input("Enter the encrypted sentence")

word_bag_key = list(range(len(word_bag)))
random.shuffle(word_bag_key)
print(word_bag_key)

decrypted_word_bag = [None] * len(word_bag)
for i, key in enumerate(word_bag_key):
    decrypted_word_bag[key] = word_bag[i]

print(word_bag)
print(decrypted_word_bag)
random.seed(2)
