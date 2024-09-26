
import re

class BytePairEncoding():
    def __init__(self, vocab_size, corpus, merges=100):
        assert corpus != [], "corpus is empty, please pass actual text data"
        self.vocab_size = vocab_size
        self.corpus = corpus
        self.merge_count = merges
        self.initial_vocab = self.create_vocabulary()
        self.tokens = self.create_vocabulary()
    
    # Initializing the vocabulary
    def create_vocabulary(self):
        tokens = []
        for text in self.corpus:
            text_split = re.sub(r'\s+', ' ', text).strip()
            for word in text_split.split(" "):
                new_word = " ".join(list(word.lower())) + " _"
                tokens.append(new_word)
        return tokens

    # Creating adjacent pairs 
    def identify_pairs(self):
        pairs = {}
        for token in self.tokens:
            seq = token.split(" ")
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i + 1])
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
        self.pairs = dict(sorted(pairs.items(), key=lambda x: x[1], reverse=True))
        if len(self.pairs) > 0:
            self.max_pair = list(self.pairs.keys())[0]

    def merge(self):
        j = 0
        while j < self.merge_count:
            self.identify_pairs()
            new_tokens = []

          
            for token in self.tokens:
                seq = token.split(" ") 
                new_sentence = []
                i = 0
                while i < len(seq) - 1:
                    
                    if seq[i] == self.max_pair[0] and seq[i + 1] == self.max_pair[1]:
                        new_sentence.append(seq[i] + seq[i + 1])
                        i += 2 
                    else:
                        new_sentence.append(seq[i])
                        i += 1  

                if i == len(seq) - 1:
                    new_sentence.append(seq[-1])

                new_tokens.append(" ".join(new_sentence))

     
            self.tokens = new_tokens
            j += 1
