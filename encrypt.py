import random


# target = input("Please input the sentence you want to encrypt: \n")
target = "Demonstrate that if you use the same seed value twice, you will get the same random number twice"
seed = random.randint(1, 1e5)
# if  seed := input("Optional: provide your seed number (type \"no\" if you don't have it):\n").lower() == "no":

random.seed(2)

word_bag = target.split()
new_word_bag = [None] * len(word_bag)
choice_range = list(range(len(word_bag)))
random.shuffle(choice_range)

# initial shuffle of inputting sentence word_bag
for i in range(len(word_bag)):
    choice_i = choice_range[i]
    new_word_bag[i] = word_bag[choice_i]

print(word_bag)
print(new_word_bag)

print(" ".join(new_word_bag))