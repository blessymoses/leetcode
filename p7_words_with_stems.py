"""
In data science, there exists the concept of stemming, which is the heuristic of chopping off the end of a word to clean and bucket it into an easier feature set. 

Given a dictionary consisting of many roots and a sentence, 
write a function replace_words to stem all the words in the sentence with the root forming it. 
If a word has many roots that can form it, replace it with the root with the shortest length.
"""
roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
roots = ["accurate", "possible"]
sentence = "The result of the match was inaccurate, adding every single point it's impossible that it adds to the total result in play the match"
# output - "the cat was rat by the bat"

def replace_words(roots, sentence):
  output = []
  for w in sentence.split():
    r = [root for root in roots if root in w and w.startswith(root)]
    if r:
        output.append(min(r, key=len))
    else:
        output.append(w)
#   print(*output, sep=" ")
  print(" ".join(output))

replace_words(roots, sentence)