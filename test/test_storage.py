import pytest
from models import Student
from storage import CSVStorage

def test_storage_round_trip(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    s1 = CSVStorage()
    stu1 = Student("张三", "20260001", "男", 95)
    stu2 = Student("李四", "20260002", "女", 59)
    students = [stu1,stu2]
    s1.save_stu(students)
    result = s1.load_stu()
    assert result[0].to_row() ==  stu1.to_row()
    assert result[1].to_row() ==  stu2.to_row()
    assert len(result) == 2  

def test_storage_blank(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    s1 = CSVStorage()
    students = []
    s1.save_stu(students)
    result = s1.load_stu()
    assert result ==  []


def test_storage_blank_file(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    s1 = CSVStorage()
    result = s1.load_stu()
    assert result == []

def test_storage_value(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    s1 = CSVStorage()
    stu1 = Student("张三", "20260001", "男", 95)
    stu2 = Student("李四", "20260002", "女", "abc")
    stu3 = Student("王五", "20260003", "男", 59)

    students = [stu1,stu2,stu3]
    s1.save_stu(students)
    result = s1.load_stu()
    assert result[0].to_row() ==  stu1.to_row()
    assert result[1].to_row() ==  stu3.to_row()
    assert len(result) == 2  