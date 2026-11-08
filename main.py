from manager import StudentManger
from storage import CSVStorage

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
                stm.add_student(students1)
            case 2:
                stm.del_student()
            case 3:
                stm.change_stu_name()         
            case 4:
                print("====关闭程序====")
                break
            case _:
                print("输入错误，请重新输入\n")






if __name__ == "__main__":
    main()