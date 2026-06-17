class Student:
    def __init__(self, student_id, name, gender, major, gpa):
        self.id = student_id
        self.name = name
        self.gender = gender
        self.major = major
        self.gpa = gpa
        self.rank = self.calculate_rank()

    def calculate_rank(self):
        if self.gpa >= 8.0:
            return "Giỏi"
        elif self.gpa >= 6.5:
            return "Khá"
        elif self.gpa >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
