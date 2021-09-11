# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

import random

class encrypt:
    def __init__(self, sentence):
        self.sentence = sentence
        self.seed = 2 # random.randint(1, 1e5)
        random.seed(self.seed)
        
        # determine which functions are used
        self.sequence = []
        self.encode_dict = {
            "shuffle": 1,
            "wordlock": 2,
        }

        # initiate global word bag
        self.word_bag = self.sentence.split()

        self.rand_word_bag_index = list(range(len(self.word_bag)))
        random.shuffle(self.rand_word_bag_index)
    
    def shuffle(self):
        new_word_bag = [None] * len(self.word_bag)

        # initial shuffle of inputting sentence word_bag
        for i in range(len(self.word_bag)):
            choice_i = self.rand_word_bag_index[i]
            new_word_bag[i] = self.word_bag[choice_i]
        
        self.word_bag = new_word_bag
        self.sequence.append(self.encode_dict["shuffle"])
    
    def wordlock(self):
        random.seed(self.seed)
        # run through whole wordbag and shuffle each word
        for i in range(len(self.word_bag)):
            random.shuffle(len_list := list(range(len(self.word_bag[i]))))
            self.word_bag[i] = "".join([self.word_bag[i][index] for index in len_list])

        self.sequence.append(self.encode_dict["wordlock"])

    def output(self):
        index_to_use = self.rand_word_bag_index[:len(self.sequence)]

        # inserting each sequence in word_bag
        for i, choice in enumerate(index_to_use):
            self.word_bag[choice] += str(self.sequence[i])
        
        ###TODO
        # insert self.seed into encoded sentence

        # output encrypted sentence
        return " ".join(self.word_bag)

e = encrypt("with a sense of humor, embarrassing goofs can be turned into something positive")
e.shuffle()
e.wordlock()
print(e.output())

"""
[0, 1, 2, 3, 4]
random.shuffle():
[3, 0, 4, 1, 2]
goofs -> fgsoo
"00000"
"00f00"
...
"""