student = {
    "bob": [85, 70, 90],
    "roger": [60, 30, 99],
    "tais": [80, 33 ,32]
}
#add new student
student["serge"] = [91, 90, 11]
#update student note
student["bob"] = [60, 45, 21]
for student_name, grades in student.items():
    average = sum(grades) / len(grades) 
    print(f"{student_name}: {grades} | Average: {average:.2f}")       #:.2f to cut decimal at 2