import sys

words = []

for line in sys.stdin:
 words.append(line.strip())

def mk(lower=False):
 for word in words:
  for word2 in words:
   if word == word2: continue
   if lower == True: 
    word = word.lower()
    word2 = word2.lower()
   print("{}{}".format(word, word2))
   print("{}-{}".format(word, word2))
   print("{}.{}".format(word, word2))
   print("{}_{}".format(word, word2))


words = list(set(words))
print(mk())
print(mk(lower=True))
