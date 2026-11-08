class Student:

    def __init__(self, name, number, sex, score):
        self.name = name
        self.number = number
        self.sex = sex
        self.score = score
    def __str__(self):
        return f"{self.name},{self.number},{self.sex},{self.score}"

    def is_passed(self):
        return self.score >= 60

    def to_row(self):
        student = [self.name, self.number, self.sex, self.score]
        return student



