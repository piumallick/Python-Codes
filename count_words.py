# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 17:26:06 2018

@author: piuma
"""



def count_words(text):
    """
    Count the number of times each word occurs in the text (str).
    Return dictionary where the keys are unique words and values are word counts.
    Skip punctuation.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:    # known word
            word_counts[word] += 1
        else:
            word_counts[word] = 1  # unknown word
    return word_counts

from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in the text (str).
    Return dictionary where the keys are unique words and values are word counts.
    Skip punctuation. This time, by using Counter object from collections library.
    """
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = Counter(text.split(" "))
    return word_counts

text = "This is my test text. We're keeping this text short to keep things manageable."
    
#text = "Here you can get help of any object by pressing Ctrl+I in front of it, either on the Editor or the Console. Help can also be shown automatically after writing a left parenthesis next to an object. You can activate this behavior in Preferences > Help."

# Output:
#count_words(text)
#Out[139]: 
#{'is': 1,
# 'keep': 1,
# 'keeping': 1,
# 'manageable': 1,
# 'my': 1,
# 'short': 1,
# 'test': 1,
# 'text': 2,
# 'things': 1,
# 'this': 2,
# 'to': 1,
# 'were': 1}
#
#count_words_fast(text)
#Out[142]: 
#Counter({'is': 1,
#         'keep': 1,
#         'keeping': 1,
#         'manageable': 1,
#         'my': 1,
#         'short': 1,
#         'test': 1,
#         'text': 2,
#         'things': 1,
#         'this': 2,
#         'to': 1,
#         'were': 1})

# Checking whether result returned are same 
#
#count_words_fast(text) == count_words(text)
#Out[143]: True


# Some more checking
#
#count_words("This comprehension check is to check for comprehension.")
#Out[144]: {'check': 2, 'comprehension': 2, 'for': 1, 'is': 1, 'this': 1, 'to': 1}
#
#len(count_words("This comprehension check is to check for comprehension."))
#Out[145]: 6
#
#count_words_fast(text) is count_words(text)
#Out[146]: False