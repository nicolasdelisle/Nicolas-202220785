#prompt the user to get 5 number one at time 
numbers = []                                                             #initializes a empty list
for i in range(5):                                                       # start a loop for 5 number
    #making sure to receive number no other character
    while True:
        try:
            number = float(input("Enter a number: "))
            if number.is_integer():                                      #making integer look cleaner
             number = int(number)
            numbers.append(number)                                       #add a number to the numbers 
            break                                                        
        except ValueError:                                               #if not a valid anwser prompt the user again
            print('Invalid input! Try enter a number.')                  

#sorting number ascend    
numbers.sort()
#average of all numbers
average_all = sum(numbers) / len(numbers) 
print("You entered:", numbers)                                           #same as line 27 but since list is dynamic it show numbers before removing the highest and the average

#removing Highest
numbers.pop()
#average of remaining numbers
average_remain = sum(numbers) / len(numbers)
   
    #main program
print("You entered:", numbers)
print('Average of numbers excluding the highest number: ', average_remain)
print('Average of all numbers: ', average_all)