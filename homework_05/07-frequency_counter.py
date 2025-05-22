def character_count(text):
    """
    Counts how often each character appears in a string, ignoring spaces.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_dict = {}  # Create an empty dictionary

    for char in text:
        if char != ' ':  # Ignore spaces
            if char in char_dict:
                char_dict[char] += 1  # Increase the count
            else:
                char_dict[char] = 1  # Add new character with basic count 1

    return char_dict

# main

user_input = input("Enter a string: ")
result = character_count(user_input)
print("Character count:", result)
