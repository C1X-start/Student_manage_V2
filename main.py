from manager import StudentManger
from storage import CSVStorage
from models import Student
def main():
    title()


def title():
    stg = CSVStorage()
    stm = StudentManger()
    students1 = stg.load_stu()
    stm.students = students1        
    while True:
        #当要改变数据类型时一定要警惕数据错误
        try:
            goal = int(
                input(
                "请选择需求\n1.学生信息添加\n2.学生信息删除\n3.修改学生信息\n4.退出程序\n"
                )
            )  # 输入的是字符串类型 要转换
        except ValueError:
            print("请输入正确数字")
            continue

        match goal:
            case 1:
                name = input("请输入姓名")
                number = input("请输入学号")
                sex = input("请输入性别")
                while True:
                    try:
                        score = int(input("请输入成绩"))
                        break
                    except ValueError:
                        print("请输入正确数字")
                        continue
                new_student = Student(name,number,sex,score)
                result = stm.add_student(new_student)
                if result:
                    print("已添加完毕")
                    stg.save_stu(stm.students)
                else:
                    print("添加失败，学号可能重复或信息不符合格式要求")
                
            case 2:
                number = input("请输入需要删除的学生学号")
                result = stm.del_student(number)
                if result:
                    print("学生信息已被删除")
                    stg.save_stu(stm.students)
                else:
                    print("可能未找到该学生，删除失败")
                
            case 3:
                number = input("输入需要修改的学生学号\n")
                while True:
                    try:
                        choice = int(input("1.修改姓名\n2.修改学号\n3.修改性别\n4.修改成绩\n"))
                        break
                    except ValueError:
                        print("请输入正确数字")
                        continue
                if choice == 4:
                    while True:
                        try:
                            new_value = int(input("请输入成绩"))
                            break
                        except ValueError:
                            print("请输入正确数字")
                            continue
                else:
                    new_value = input("输入新的值")
                result = stm.change_student(number,choice,new_value)
                if result:
                    print("已修改成功")
                    stg.save_stu(stm.students)
                else:
                    print("修改失败")         
            case 4:
                print("====关闭程序====")
                break
            case _:
                print("输入错误，请重新输入\n")






if __name__ == "__main__":
    main()