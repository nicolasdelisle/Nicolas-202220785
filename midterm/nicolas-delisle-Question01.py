#using try else so anything not an integer will not make crash program
try:
    number = int(input("Enter a number: "))                           #asking user an input 
except ValueError:
    print("Invalid input! Enter a valid integer.")
    
    #if it got a integer it will start the loop and stop at the first true statement if false will continue until true  
else:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)