class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, GPA):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.GPA = GPA

    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")

    def calculate_GPA(self):
        return self.GPA

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def grade_students(self):
        print(f"{self.name} is grading students' work.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Creating instances of Teacher and Student
teacher_instance = Teacher("Tenzin", 29, "10101005546", "Math", 100000000, "Mathematics", "Professor")
student_instance = Student("Lhamo", 19, "10101005547", "02230110", "ECE", 2, 3.5)

# Accessing common attributes and methods
student_instance.walk()
teacher_instance.walk()

# Accessing specific attributes and methods
print(student_instance.student_id)
print(teacher_instance.subject)

student_instance.study()
teacher_instance.teach()

# Using specific methods
print(f"{student_instance.name}'s GPA is {student_instance.calculate_GPA()}")

student_instance.write_exam()
teacher_instance.attend_meeting()
