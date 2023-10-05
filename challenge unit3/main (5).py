class Student:
  def __init__(self, name, roll_number, cgpa):
     self.name= name
     self.roll_number= roll_number
     self.cgpa= cgpa

def sort_Students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse= True) 
  return sorted_students

# Example usage

students = [Student("priya","A123",7.8),Student("Ajay","A124",8.9),Student("Asifa","A125",9.1),Student("Sanju","A126",9.9)]

sorted_students= sort_Students(students) 

# Print the sorted list of students

for student in sorted_students:
  print("Name: {}, Roll number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))


