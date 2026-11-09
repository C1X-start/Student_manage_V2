from models import Student
import re

class StudentManger:

    def __init__(self):
        self.students = []

    def number_verify(self,number):
        result = re.search(r"^[1-9][0-9]{7}$",number)
        if result:
            return True
        return False

    def add_student(self, student):
        for stu in self.students:
            # stundents列表里面储存的学生数据不是列表，而是对象，不能用列表的方式索引
            if stu.number == student.number:
                # return 会直接结束语句
                return False
        if self.number_verify(student.number):
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

    def change_student(self,number,choice,new_value):
        match choice:
            case 1:
                self.change_stu_name(number,new_value)
            case 2:
                self.change_stu_number(number,new_value)
            case 3:
                self.change_stu_sex(number,new_value)
            case 4:
                self.change_stu_score(number,new_value)



        
    def change_stu_name(self, number,new_name):
        result = self.search_student(number)
        if result is not None and new_name is not None :
            result.name = new_name
            return True
        return False

    def change_stu_number(self, number,new_number):
        result = self.search_student(number)
        result2 = self.search_student(new_number)
        if result is not None  and result2 is None and self.number_verify(new_number):
            result.number = new_number
            return True
        return False

    def change_stu_sex(self, number,new_sex):
        result = self.search_student(number)
        if result is not None and new_sex in ("男","女") :
            result.sex = new_sex
            return True
        return False

    def change_stu_score(self, number, new_score):
        result = self.search_student(number)
        if result is not None and 0 <= new_score <= 100:
            # result 就是原来列表中的那个对象，直接更改就行，不需要再次保存
            result.score = new_score
            return True
        return False




