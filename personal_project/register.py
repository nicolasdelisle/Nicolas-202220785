# function to get user information
def get_my_information():
    first_name = input("Enter your first name: ").title().strip()
    last_name = input("Enter your last name: ").title().strip()
    city = input("In which city do you reside: ").title().strip()
    state = input("In which province/state do you reside: ").title().strip()
    country = input("In which country de you reside: ").title().strip()

#asking age to be integer
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                break
            else:
                print("Must be only positif number.")
        except ValueError:
                print("Invalid input! Enter a number (exemple: 21).")

#asking phone number and formating 
    while True:
         phone = input("Enter your phone number without space (10 digits): ")
         if phone.isdigit() and len(phone) == 10:
              formatted_number = f"{phone[:3]}-{phone[3:6]}-{phone[6:10]}"
              break
         else:
             print("Invalid input must be exactlt 10 digits.")


#return user details
    return first_name, last_name, city, state, country, age, formatted_number

#main program
first_name, last_name, city, state, country,  age, phone = get_my_information()

#displaying the user information
print("\n    My Information ")
print(f"Name: {first_name} {last_name}")
print(f"From: {country}, {state}, {city}")
print(f"Age: {age} years old")
print(f"Phone number: {phone}")