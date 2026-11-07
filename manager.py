from models import Student


class StudentManger:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        for stu in self.students:
            # stundents列表里面储存的学生数据不是列表，而是对象，不能用列表的方式索引
            if stu.number == student.number:
                # return 会直接结束语句
                return False
        self.students.append(student)
        return True

    def search_student(self, number):
        for stu in self.students:
            if stu.number == number:
                # 这里返回的是一个对象，直接打印是无效的，必须通过调用来显示
                return stu
        return None

    def del_student(self, number):
        result = self.search_student(number)
        if result is not None:
            self.students.remove(result)
            return True
        return False

    def change_stu_name(self, number):
        pass

    def change_stu_number(self, number):
        pass

    def change_stu_sex(self, number):
        pass

    def change_stu_score(self, number, new_score):
        result = self.search_student(number)
        if result is not None and 0 <= new_score <= 100:
            # result 就是原来列表中的那个对象，直接更改就行，不需要再次保存
            result.score = new_score
            return True
        return False


stu1 = Student("张三", "20260001", "男", 95)
stu2 = Student("李四", "20260001", "女", 59)
manager = StudentManger()
manager.add_student(stu1)
result3 = manager.change_stu_score("20260001", 99)
print(result3)

# manager.add_student(stu2)
# result = manager.search_student("20260001")
# if result is not None:
#     print(result.to_row())
# result2 = manager.del_student("20260001")
# print(result2)
# print(len(manager.students))
