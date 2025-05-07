user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
else:
    print("That is not a number")