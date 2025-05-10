#prompt the user to get 5 number one at time
numbers = []   #Float or Integer
for i in range(5):
    while True:
        try:
            number = float(input("Enter a number: "))
            if number.is_integer:    #making integer look cleaner
             number = int(number)
            numbers.append(number)
            break
        except ValueError:
            print('Invalid input! Try enter a number.')




#sorting number ascend and remove the highest number   
numbers.sort()
#average of all numbers
average_all = sum(numbers) / len(numbers)         #need to be placed before the number pop
numbers.pop()

#average of remaining numbers
average_remain = sum(numbers) / len(numbers)
   
    #main program
print("You entered:", numbers)
print('Average of numbers excluding the highest number: ', average_remain)
print('Average of all numbers: ', average_all)