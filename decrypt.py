import random
class decrypt:
    def __init__(self, sentence, seed):
        self.sentence = sentence
        self.seed = seed
        random.seed(self.seed)

        # initiate global word bag
        self.word_bag = self.sentence.split()
        
        self.rand_word_bag_index = list(range(len(self.word_bag)))
        random.shuffle(self.rand_word_bag_index)

    def run(self):
        decode_dict = {
            1: self.shuffle
        }

        function_sequence = []
        for i in self.rand_word_bag_index:
            try:
                func_num = int(self.word_bag[i][-1])
                self.word_bag[i] = self.word_bag[i][:-1]
                function_sequence.append(func_num)
            except:
                break
    
        for x in function_sequence:
            decode_dict[x]()
        self.wordlock()
        
        return self.output()

    def shuffle(self):
        decrypted_word_bag = [None] * len(self.word_bag)
        for i, key in enumerate(self.rand_word_bag_index):
            decrypted_word_bag[key] = self.word_bag[i]
        self.word_bag = decrypted_word_bag
    
    def wordlock(self):
        random.seed(self.seed)
        # run through whole wordbag and shuffle each word
        for i in range(len(self.word_bag)):
            random.shuffle(len_list := list(range(len(self.word_bag[i]))))
            print(len_list, self.word_bag[i])
            self.word_bag[i] = "".join([self.word_bag[i][index] for index in len_list])

    def output(self):
        return " ".join(self.word_bag)

d = decrypt("rnuedt of fgsoo poteviis noit cna be rhmu,o snsee eiamasrgsnbr1 esonmtihg a with", 2)
print(d.run())