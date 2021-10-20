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
        occurrences = 0
        with open(self.file_name) as f:
            for lines in f:
                occurrences += lines.lower().count(inp)
            return f'Number of occurrences of {inp} is {occurrences}'

    def word_count(self):
        words = 0
        with open(self.file_name) as f:
            for lines in f:
                words += len(lines.split())
        return words

    def sentence_count(self):
        sentences = 0
        with open(self.file_name) as f:
            for lines in f:
                if not lines.endswith('.' or '!' or '?'):
                    sentences -= 1
                sentences += len(re.split(r"[.!?]+", lines))
        return sentences

    def most_common(self):
        with open(self.file_name) as f:
            text = f.read()
            count = Counter(text.translate(punctuation).lower().split())
            print(count)
        return [item for item in count.most_common(10)]

    '''
    count = Counter()
        with open(self.file_name) as f:
            for lines in f:
                count += Counter(lines.translate(punctuation).lower().split())
        return [item for item in count.most_common(10)]
        
    Weird behavior???
    '''

    def __str__(self):
        return f'Number of words: {self.word_count()} Number of sentences: {self.sentence_count()}\n' \
               f'Most popular words: {self.most_common()}'


def main():
    obj = TextProcessor('test.txt')
    print(obj)
    print(obj.searcher('b'))


if __name__ == '__main__':
    main()
