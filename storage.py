import csv
from pathlib import Path
from models import Student

class CSVStorage:

    def __init__(self,file_path="data/student.csv"):
        self.file_path = file_path



    def load_stu(self):
        stundents = [] 
        try:
            with open(self.file_path,"r",encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 4:
                        print(f"发现错误数据{row}请及时修改")
                        continue
                    try:
                        stu = Student(row[0],row[1],row[2],int(row[3]))
                        stundents.append(stu)
                    except ValueError:
                        print(f"发现错误成绩数据{row}，已跳过")
                return stundents
        except FileNotFoundError:
            return []
       

    def save_stu(self,students):
        Path(self.file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            for stu in students:
                writer.writerow(stu.to_row())

