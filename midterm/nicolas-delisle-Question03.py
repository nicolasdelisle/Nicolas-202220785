#list use[] ----  dictionary use{}
#the giving list of tuples
students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]

#1. Convert list of tuples to dictionary (name → score)
student_dict = {name: score for name, score in students}
print("Dictionary:", student_dict)

#2. Filter dictionary to include only students with "score > 80"
#".item()" let me get info in the list and "if" make a condition to be selected 
note_dict = {name: score for name, score in student_dict.items() if score > 80}
print("Scored above 80:", note_dict)

#3. Use list comprehension to extract just the names 
#Unpack name and score but only use the name in list
names = [name for name, score in student_dict.items()]
print("Names of students:", names)