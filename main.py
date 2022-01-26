import re
#
import string
#
from collections import Counter
#
import numpy as np
#


def read_corpus(filename):
  with open(filename, "r") as file:
    lines = file.readlines(290131)
    words = []
    for line in lines:
      words += re.findall(r'\w+', line.lower())
#i had to import the file that stores all the words i'll be using for my spellcheck. there was a capacity on line 13 so i have to fix that. it also has to eb lowecase
  return words
    #just in case some words are lowercase
  
  ##


words = read_corpus('./atlasshrugged.txt')
print(f'There are {len(words)} words in total in this corpus') 
#we imported our book, which is like the longest book in the world lol. but we print how many words there are in total.

vocabs = set(words)
print(f'there are {len(vocabs)} unique words in this vocab')
#we also print how many words aren't duplicate in an f string
# line 32 AN EXAMPEL
word_counts = Counter(words)
print(word_counts['love'])

#we could also find hte probability we would find the roes
total_word_count = float(sum(word_counts.values()))
word_probas = {word: word_counts[word] / total_word_count for word in word_counts.keys()}

print(word_probas['there'])
#we track the probability a word is going to appear

def split(word):
  return [(word[:i], word[i:]) for i in range(len(words) + 1)]

#analyzes each word you input letter by letter
#splits into two components

def delete(word):
  return [ l + r[l:] for l, r in split(word) if len(r)> 1]
#deletes a word and returns any other word

def swap(word):
  return [l + r [1] + r[0] + r[2:] for l,r in split(words) if len(r)>1]
# swaps a word from code from left to right (love: olve, lvoe, loev). love how it checkes for valid ones in our dictionary

def insert(word):
  letters = string.ascii_lowercase
  return [l + c + r for l, r in split(word) for c in letters]
#like the other changes, you could replace a letter with any other one in the alphabet

#now to amp my codeeee

def first_form_(word):
  return set(split(word) + swap(word) + insert(word) + delete(word))

def second_form(word):
  return set(e2 for e1 in first_form_(word) for e2 in first_form_(e1))

print(second_form("like"))