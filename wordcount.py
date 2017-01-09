import string
from sys import argv

try:
    text_file = open(argv[1])
except IndexError:
    text_file = open("twain.txt")
word_counter = {}

for line in text_file:
    words = line.rstrip().split()

    for word in words:
        word = word.strip(string.punctuation).lower()
        #word = word.strip(".,?:;' \"_ ")
        word_counter[word] = word_counter.get(word, 0) + 1


for word, count in word_counter.iteritems():
    print word, count
