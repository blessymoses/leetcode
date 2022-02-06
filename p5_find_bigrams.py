"""find_bigrams
Take a string and return a list of all bigrams.

[('have', 'free'), ('free', 'hours'), ('hours', 'and'), ('and', 'love'), ('love', 'children?'), ('children?', 'drive'), ('drive', 'kids'), ('kids', 'to'), ('to', 'school,'), ('school,', 'soccer'), ('soccer', 'practice'), ('practice', 'and'), ('and', 'other'), ('other', 'activities.')]
"""
from typing import List


def find_bigrams(sentence: str) -> List[tuple]:
    result = []
    words = sentence.lower().split()
    i = 0
    while i < len(words) - 1:
        result.append((words[i], words[i + 1]))
        i += 1
    return result


sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""
print(find_bigrams(sentence))
