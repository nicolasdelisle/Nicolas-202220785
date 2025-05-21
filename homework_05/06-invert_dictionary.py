from collections import defaultdict                     #container https://docs.python.org/3/library/collections.html
import string

def word_count(sentence: str, invert=False):
    # Remove punctuation and split into words
    words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
    word_dict = defaultdict(int)

    for word in words:
        word = word.lower()
        word_dict[word] += 1

    if invert:
        # Invert the dictionary (make counts the keys, words the values)
        inverted_dict = defaultdict(list)
        for word, count in word_dict.items():
            inverted_dict[count].append(word)
        return dict(inverted_dict)

    return dict(word_dict)

# main program
sent = input("Enter a sentence: ")
invert_word = input("Do you want to invert the dictionary? (yes/no): ").lower() == 'yes'
result = word_count(sent, invert=invert_word)
print(result)