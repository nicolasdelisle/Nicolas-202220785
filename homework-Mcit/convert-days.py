#Getting the prompt needed
def get_positive_integer_input(prompt):
    while True:
        try:
            days = int(input(prompt))
            if days >= 0:
                return days
            else:
                print("Invalid answer! Enter a positif number this time.")
        except ValueError:
                print("Invalid answer! Enter a number this time.")

#conversion constant
def unit_calculation(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return hours, minutes, seconds

# Main Program
days = get_positive_integer_input("Enter a number of days to convert: ")
hours, minutes, seconds = unit_calculation(days)
print(f"{days} days = {hours} hours, {minutes} minutes and {seconds} seconds.")