#Define a fonction that will calculate area of rectangle 
def calculate_area(length, width):
    return length * width

try:
    # Take input from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    #assuring the program doesnt crash if anwser invalid with "try" and "except"
except ValueError:
    print("Invalid input! Please enter numeric values.")

    #Giving a variable the value of the fonction "calculate_area(length, width)" then printing 
area = calculate_area(length, width)
print("The area of the rectangle is:", area)