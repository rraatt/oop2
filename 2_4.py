from collections import Counter
import re
from string import punctuation


class TextProcessor:
    __slots__ = ["raw", "words", "sentences", "filtered", "popular_list"]

    def __init__(self, file):
        if not isinstance(file, str):
            raise TypeError("Name of file required in input!!!")
        self.raw = open(file).read()
        # Open text file for reading.
        self.words = len(self.raw.split())
        # Splitting the file for words counting
        self.sentences = len(re.split(r"[.!?]+", self.raw))
        # Splitting the file for sentences counting.
        self.filtered = self.raw.translate(punctuation).lower().split()
        # Splitting the text and removing punctuation to find most common words
        count = Counter(self.filtered)
        self.popular_list = [item for item in count.most_common(10)]

    def searcher(self, inp):
        count = Counter(self.raw.lower())
        return f'Number of occurrences of {inp} is {count[inp]}'

    def __str__(self):
        return f'Number of words: {self.words} Number of sentences: {self.sentences}\n' \
               f'Most popular words: {self.popular_list}'


obj = TextProcessor('test.txt')
print(obj)
print(obj.searcher('b'))
