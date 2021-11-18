students=[]
grades=[]
while True:
   student = input("Please give me the name of the student (q to quit): ")
   if student == 'q':  
       for i in range(len(students)):
           print("Student: " + students[i] + ", Grade: " + grades[i])
       break
   grade =input("Please give me their grade: ")
   students.append(student)
   grades.append(grade)