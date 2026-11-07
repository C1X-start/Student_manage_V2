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
        student = [self.name, self.number, self.sex, f"{self.score}"]
        return student


stu1 = Student("张三", "20260001", "男", 95)
stu2 = Student("李四", "20260002", "女", 59)
# print(stu1.name)
# print(stu1.score)
# print(stu1.is_passed())
# print(stu1.to_row())
