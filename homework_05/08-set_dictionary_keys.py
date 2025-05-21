def check_key_in_dict(dictionary, key):
    """
    Extracts keys of the dictionary into a set and checks if a specific key exists.

    Args:
        dictionary (dict): The dictionary to check.
        key: The key to search for.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    # Extract keys into a set
    key_set = set(dictionary.keys())

    # Check for key membership
    return key in key_set

# main
sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = input("Enter the key you want to check: ")

if check_key_in_dict(sample_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")