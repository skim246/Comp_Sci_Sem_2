with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        print(l)

f.close()

import random
wordlist = []
a = random.randrange(wordlist)
b = input("Guess a word: ")