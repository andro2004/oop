class Stydent:
    def __init__(self, name, age, student_id,courses, grades):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses  
        self.grades = grades    

    
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print( f"Enrolled in course: {course}")
        else:
            print( "Already enrolled in this course.")

    def add_grade(self, course, grade):
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return
        else:
            self.grades[course] = grade
            print(f"Added grade {grade} for course {course}.")
    def get_student_id(self):
        return self.student_id
     