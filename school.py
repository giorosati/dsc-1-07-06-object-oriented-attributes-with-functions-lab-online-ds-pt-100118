class School():
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, student_name=None, student_grade=None):
        if student_grade in self.roster:
            self.roster[student_grade].append(student_name)
        else:
            self.roster[student_grade] = []
            self.roster[student_grade].append(student_name)

    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        for grade in self.roster:
            self.roster[grade].sort()
        return self.roster
