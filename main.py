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
    lines = file.readlines()
    words = []
  for line in lines:
    words += re.findall(r'\w+', line.lower())
  return words
    #just in case some words are lowercase
  
  ##


words = read_corpus('./atlasshrugged.txt')
print(f'There are {len(words)} words in total in this corpus') 


vocabs = set(words)
print(f'there are {len(vocabs)} unique words in this vocab')
print(words)