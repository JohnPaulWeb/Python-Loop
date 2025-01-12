class Student:
    def __init__(self, name, age, grade):
        """
        Initializes the Student 
        """
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        """
        Returns True if the student's grade is 60 or higher, 
        """
        return self.grade >= 60



student1 = Student(name="John", age=19, grade=75)


student2 = Student(name="Emma", age=21, grade=58)

students = [student1, student2]

for student in students:

    passing_status = "passing" if student.is_passing() else "not passing"
    print(f"{student.name}, aged {student.age}, is {passing_status}.")