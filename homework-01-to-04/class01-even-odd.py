#def prompt/get input
def get_number_input(prompt) -> float | int:
    while True:
        try:
            # Accept number only
            num: float = float(input(prompt))
            if num.is_integer():
                return int(num)
            else:
                return num
        except ValueError:
            print("This is not valid! Enter a number.")

# function to check if the last digit before the decimal is even or odd
def check_even_odd(num: float | int):
    # get the integer part of the number and check the last digit before the decimal point
    integer_part = int(num)
    
    if integer_part % 2 == 0:
        return "even"
    else:
        return "odd"

# Main Program
number = get_number_input("Enter a number: ")
even_or_odd = check_even_odd(number)

print(f"The {number} is {even_or_odd}.")