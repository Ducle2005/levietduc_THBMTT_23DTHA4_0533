from student import Student

class StudentManager:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self, name, gender, major, gpa):
        student = Student(self.next_id, name, gender, major, gpa)
        self.students.append(student)
        self.next_id += 1
        return student

    def update_student(self, student_id, name, gender, major, gpa):
        for s in self.students:
            if s.id == student_id:
                s.name = name
                s.gender = gender
                s.major = major
                s.gpa = gpa
                s.rank = s.calculate_rank()
                return True
        return False

    def delete_student(self, student_id):
        for i, s in enumerate(self.students):
            if s.id == student_id:
                del self.students[i]
                return True
        return False

    def search_by_name(self, name):
        results = []
        for s in self.students:
            if name.lower() in s.name.lower():
                results.append(s)
        return results

    def sort_by_gpa(self):
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def sort_by_major(self):
        self.students.sort(key=lambda x: x.major.lower())

    def get_all_students(self):
        return self.students
