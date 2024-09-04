'''
student_heights = input("Input a list of student heights ").split()
print(student_heights)
hight = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  hight += student_heights[n]
  ad = hight/ len(student_heights)
  
print(ad)

for n in student_heights:
    hight += student_heights

av = hight/ len(student_heights)

print(av)'''

student_heights = input("Input a list of student heights ").split()
print(student_heights)
total_height = 0 
number_of_student = 0
for n in range(0 , len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n] # total height
    number_of_student += 1 # Number of student
    
'''average_HEIGHT = total_height/ len(student_heights)'''
print(number_of_student)
average_HEIGHT = total_height/ number_of_student
print(average_HEIGHT)