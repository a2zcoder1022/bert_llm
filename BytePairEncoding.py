

class BytePairEncoding():
    def __init__(self, vocab_size, corpus, merges=5):
        assert corpus != [], "corpus is empty, please pass actual text data"
        self.vocab_size = vocab_size
        self.corpus = corpus
        self.tokens = self.create_vocabulary()
        self.updatedVocabulary = {}

    #initializing the vocabulary
    def create_vocabulary():
        tokens = {}
        for text in self.corpus:
            text_split = text.lower().replace("\n", "").split(" ")
            for word in text_split:
                new_word = "  ".join(list(word)) + " </w>"
                if new_word in tokens:
                    tokens[new_word] += 1
                else:
                    tokens[new_word] = 1
        return tokens

    #creating adjacent paris
    def identify_pairs():
        pairs = {}
        for token in self.tokens:
            seq = token.split()
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i + 1])
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
         return pairs