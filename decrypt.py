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
            1: self.decrypt_shuffle
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
        
        return self.output()

    def decrypt_shuffle(self):
        decrypted_word_bag = [None] * len(self.word_bag)
        for i, key in enumerate(self.rand_word_bag_index):
            decrypted_word_bag[key] = self.word_bag[i]
        self.word_bag = decrypted_word_bag

    def output(self):
        return " ".join(self.word_bag)

d = decrypt("turned of goofs positive into can be humor, sense embarrassing1 something a with", 2)
print(d.run())