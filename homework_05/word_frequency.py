def word_count(sentence: str):
    words = sentence.split()                   #split the sentence into words by spaces enter
    word_dict = {}                             # {} empty dictionary
    for word in words:
        word = word.lower()                      #convert all letter to lower case so can calculate duplicate
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
sent = input("Enter a sentence: ")
result = word_count(sent)
print(result)
