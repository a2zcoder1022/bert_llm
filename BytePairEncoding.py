
import re
from collections import defaultdict
from typing import List, Tuple, Dict
from dataclasses import dataclass, field

@dataclass
class BytePairEncoding:

    vocab_size: int
    corpus: List[str]
    merge_count: int = 100
    tokens: List[str] = field(init=False)
    
    def main__init__(self):
        assert corpus != [], "corpus is empty, please pass actual text data"
        self.tokens = self.create_vocabulary()

    def clean_text(self, text:str) -> str:
        return re.sub(r'\s+', ' ', text).strip().lower()
        
        
    # Initializing the vocabulary
    def create_vocabulary(self) -> list:
        return [
            " ".join(list(word.lower())) + " _"
            for text in self.corpus for word in
            self.clean_text(text).split()
        ]
    
    # Creating adjacent pairs 
    def identify_pairs(self) -> Dict[Tuple[str, str], int]:
        pairs = defaultdict(int)
        for token in self.tokens:
            seq = token.split(" ")
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i + 1])
                pairs[pair] += 1
        return dict(pairs)

    def merge_pair(self, token:str, pair: Tuple[str, str]) -> str:

        first, second = token
        merged_token = token.replace(f"{first} {second}", f"{first}{second}")
        return merged_token

    def apply_merges(self, most_frequent_pair: Tuple[str, str]):
        self.tokens = [
            self.merge_pair(token, most_frequent_pair)
            for token in self.tokens
        ]

    def run_merge(self) -> None:
        for i in range(self.merge_count):
            pairs = self.identify_pairs()
            if not pairs:
                print("There are no more pairs")
                break
            most_frequent_pair = max(pairs, key=pairs.get)
            self.apply_merges(most_frequent_pair)

    def get_tokens(self) -> List[str]:
        return self.tokens
        
    
