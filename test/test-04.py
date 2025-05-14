def word_count(sentence: str) -> dict:
    # Split the sentence into words by spaces (you can also use regex to handle punctuation)
    words = sentence.split()
    
    # Create an empty dictionary to store word counts
    word_dict = {}
    
    # Loop through each word in the list
    for word in words:
        # Convert word to lowercase to make the counting case-insensitive
        word = word.lower()
        
        # If the word is already in the dictionary, increment its count
        if word in word_dict:
            word_dict[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            word_dict[word] = 1
    
    return word_dict

# Example usage
sentence = "This is a test sentence. This is a test."
result = word_count(sentence)
print(result)