import csv

class Student:
    def __init__(self, name, student_id, grade, scores=None):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.scores = scores if scores else {}

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Scores: {self.scores}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def search_student(self, query):
        for student in self.students:
            if student.name == query or student.student_id == query:
                return student
        return None

    def update_student(self, student_id, updates):
        student = self.search_student(student_id)
        if student:
            for key, value in updates.items():
                setattr(student, key, value)
            return True
        return False

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

    def display_all_students(self):
        for student in self.students:
            print(student)

    def analyze_scores(self):
        all_scores = [score for student in self.students for score in student.scores.values()]
        if all_scores:
            average = sum(all_scores) / len(all_scores)
            max_score = max(all_scores)
            min_score = min(all_scores)
            print(f"Average Score: {average:.2f}, Max Score: {max_score}, Min Score: {min_score}")
        else:
            print("No scores available for analysis.")

    def save_to_file(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Grade", "Scores"])
            for student in self.students:
                writer.writerow([student.name, student.student_id, student.grade, student.scores])

    def load_from_file(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    name, student_id, grade, scores = row[0], row[1], int(row[2]), eval(row[3])
                    student = Student(name, student_id, grade, scores)
                    self.add_student(student)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading file: {e}")

def main():
    system = StudentManagementSystem()
    system.load_from_file("students.csv")

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Analyze Scores")
        print("7. Save and Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            student_id = input("Enter student ID: ")
            grade = int(input("Enter grade: "))
            scores = eval(input("Enter scores as a dictionary (e.g., {'Math': 90, 'Science': 85}): "))
            student = Student(name, student_id, grade, scores)
            system.add_student(student)

        elif choice == "2":
            query = input("Enter name or student ID: ")
            student = system.search_student(query)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            updates = eval(input("Enter updates as a dictionary (e.g., {'name': 'new_name', 'grade': 2}): "))
            if system.update_student(student_id, updates):
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            if system.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "5":
            system.display_all_students()

        elif choice == "6":
            system.analyze_scores()

        elif choice == "7":
            system.save_to_file("students.csv")
            print("Data saved. Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
