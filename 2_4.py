from collections import Counter
import re
from string import punctuation
import os.path


class TextProcessor:
    __slots__ = ["file_name", "filtered", "popular_list"]

    def __init__(self, file_name):
        if not os.path.isfile(file_name):
            raise ValueError("File doesnt exist!")
        self.file_name = file_name
        # Open text file for reading.

    def searcher(self, inp):
        with open(self.file_name) as f:
            text = f.read()
            count = Counter(text.lower())
            return f'Number of occurrences of {inp} is {count[inp]}'

    def word_count(self):
        with open(self.file_name) as f:
            text = f.read()
            words = len(text.split())
        return words

    def sentence_count(self):
        with open(self.file_name) as f:
            text = f.read()
            sentences = len(re.split(r"[.!?]+", text))
        return sentences

    def most_common(self):
        with open(self.file_name) as f:
            text = f.read()
            count = Counter(text.translate(punctuation).lower().split())
        return [item for item in count.most_common(10)]

    def __str__(self):
        return f'Number of words: {self.word_count()} Number of sentences: {self.sentence_count()}\n' \
               f'Most popular words: {self.most_common()}'


def main():
    obj = TextProcessor('test.txt')
    print(obj)
    print(obj.searcher('b'))


if __name__ == '__main__':
    main()
