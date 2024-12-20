class Course:
    """Represents a course in the system."""
    def __init__(self, course_id, name, fee):
        self.course_id = course_id  # Unique identifier
        self.name = name  # Course name
        self.fee = fee  # Course fee

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Fee: ${self.fee}"

class Student:
    """Represents a student in the system."""
    def __init__(self, student_id, name, email):
        self.student_id = student_id  # Unique identifier
        self.name = name  # Student name
        self.email = email  # Student email
        self.courses = []  # List of enrolled courses
        self.balance = 0  # Outstanding balance

    def enroll(self, course):
        """Enroll the student in a course and update their balance."""
        if course in self.courses:
            raise ValueError(f"Student {self.name} is already enrolled in {course.name}.")
        self.courses.append(course)
        self.balance += course.fee

    def __str__(self):
        enrolled_courses = ', '.join(course.name for course in self.courses) if self.courses else "No courses enrolled"
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Enrolled Courses: {enrolled_courses}, Balance: ${self.balance}"

class RegistrationSystem:
    """Manages courses, students, and enrollments."""
    def __init__(self):
        self.courses = {}  # Dictionary of courses (key: course_id, value: Course object)
        self.students = {}  # Dictionary of students (key: student_id, value: Student object)

    def add_course(self, course_id, name, fee):
        """Adds a new course."""
        if course_id in self.courses:
            raise ValueError("Error: Course ID already exists.")
        self.courses[course_id] = Course(course_id, name, fee)
        print(f"Course {name} added successfully.")

    def register_student(self, student_id, name, email):
        """Registers a new student."""
        if student_id in self.students:
            raise ValueError("Error: Student ID already exists.")
        self.students[student_id] = Student(student_id, name, email)
        print(f"Student {name} registered successfully.")

    def enroll_in_course(self, student_id, course_id):
        """Enrolls a student in a specified course."""
        if student_id not in self.students:
            raise ValueError("Error: Student not found.")
        if course_id not in self.courses:
            raise ValueError("Error: Course not found.")
        student = self.students[student_id]
        course = self.courses[course_id]
        student.enroll(course)
        print(f"Student {student.name} has been enrolled in {course.name}.")

    def calculate_payment(self, student_id, payment_amount):
        """Processes payments. Requires at least 40% of the balance to confirm registration."""
        if student_id not in self.students:
            raise ValueError("Error: Student not found.")
        student = self.students[student_id]
        if payment_amount < 0.4 * student.balance:
            raise ValueError(f"Error: Minimum payment required is 40% of ${student.balance}.")
        if payment_amount > student.balance:
            raise ValueError(f"Error: Payment cannot exceed the balance of ${student.balance}.")
        student.balance -= payment_amount
        print(f"Payment of ${payment_amount} processed. Remaining balance: ${student.balance}.")

    def check_student_balance(self, student_id):
        """Displays the current balance of a specific student."""
        if student_id not in self.students:
            raise ValueError("Error: Student not found.")
        student = self.students[student_id]
        print(f"Student {student.name} has an outstanding balance of ${student.balance}.")

    def show_courses(self):
        """Lists all available courses."""
        if not self.courses:
            print("No courses available.")
        else:
            print("Available Courses:")
            for course in self.courses.values():
                print(course)

    def show_registered_students(self):
        """Lists all registered students."""
        if not self.students:
            print("No students registered.")
        else:
            print("Registered Students:")
            for student in self.students.values():
                print(student)

    def show_students_in_course(self, course_id):
        """Lists all students enrolled in a specific course."""
        if course_id not in self.courses:
            raise ValueError("Error: Course not found.")
        course = self.courses[course_id]
        enrolled_students = [student for student in self.students.values() if course in student.courses]
        if not enrolled_students:
            print(f"No students are enrolled in {course.name}.")
        else:
            print(f"Students enrolled in {course.name}:")
            for student in enrolled_students:
                print(f"Student ID: {student.student_id}, Name: {student.name}")

# Menu-driven system
def main():
    system = RegistrationSystem()

    while True:
        print("\n--- Course Registration and Payment System ---")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in a Course")
        print("4. Process Payment")
        print("5. Check Student Balance")
        print("6. Show All Courses")
        print("7. Show All Registered Students")
        print("8. Show Students in a Course")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                course_id = input("Enter Course ID: ")
                name = input("Enter Course Name: ")
                fee = float(input("Enter Course Fee: "))
                system.add_course(course_id, name, fee)
            elif choice == "2":
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                email = input("Enter Student Email: ")
                system.register_student(student_id, name, email)
            elif choice == "3":
                student_id = input("Enter Student ID: ")
                course_id = input("Enter Course ID: ")
                system.enroll_in_course(student_id, course_id)
            elif choice == "4":
                student_id = input("Enter Student ID: ")
                payment_amount = float(input("Enter Payment Amount: "))
                system.calculate_payment(student_id, payment_amount)
            elif choice == "5":
                student_id = input("Enter Student ID: ")
                system.check_student_balance(student_id)
            elif choice == "6":
                system.show_courses()
            elif choice == "7":
                system.show_registered_students()
            elif choice == "8":
                course_id = input("Enter Course ID: ")
                system.show_students_in_course(course_id)
            elif choice == "9":
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()

# I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT.
