# 🎓 Student Management System V2

一个基于 Python 面向对象编程（OOP）开发的命令行学生信息管理系统，支持学生信息的增删改查，并通过 CSV 文件实现数据持久化。

本项目是 Python 学习阶段的实践项目，主要用于巩固面向对象编程、模块化设计、文件操作、异常处理及自动化测试等知识。

## ✨ 功能介绍

- **添加学生**：录入学生姓名、学号、性别和成绩。
    
- **删除学生**：根据学号查找并删除指定学生。
    
- **修改学生**：支持修改学生姓名、学号、性别和成绩。
    
- **查询学生**：根据学号查找学生信息。
    
- **数据持久化**：通过 CSV 文件保存学生信息，程序重新启动后可以恢复数据。
    
- **异常处理**：处理文件不存在、数据格式错误及用户输入错误等情况。
    
- **数据校验**：对学号、成绩等信息进行基本格式校验。
    

## 🏗️ 项目结构

```
Student_manage_V2/
│
├── main.py              # 主程序入口，负责用户交互
├── manager.py           # 学生信息管理与业务逻辑
├── models.py            # Student 学生模型
├── storage.py           # CSV 数据读写
│
├── data/
│   └── student.csv      # 学生数据文件
│
└── test/
    └── test_storage.py  # CSV 存储模块测试
```

## 🧩 模块设计

项目采用模块化设计，将数据模型、业务逻辑、数据存储和用户交互分离。

|模块|主要职责|
|---|---|
|models.py|定义 Student 类，封装学生属性及数据转换方法|
|manager.py|定义 StudentManager 类，负责学生信息的管理与修改|
|storage.py|定义 CSVStorage 类，负责 CSV 文件的读取与保存|
|main.py|创建对象、处理用户输入、调用业务功能并反馈结果|

**核心设计思路：**

- Student 负责描述学生对象。
    
- StudentManager 负责管理内存中的学生数据。
    
- CSVStorage 负责数据持久化，不直接参与学生业务逻辑。
    
- Main 负责协调各模块，避免业务逻辑与用户交互混杂。
    

通过这种设计，学生信息管理与数据存储相互独立，便于后续维护和扩展。

## 🛠️ 技术栈

- Python 3.10+
    
- 面向对象编程（OOP）
    
- CSV 文件读写
    
- 正则表达式（re）
    
- 异常处理（try-except）
    
- pytest 自动化测试
    
- Git / GitHub 版本管理
    

## 🚀 运行项目

**1. 克隆仓库**

```
git clone https://github.com/C1X-start/Student_manage_V2.git
```

**2. 进入项目目录**

```
cd Student_manage_V2
```

**3. 运行程序**

```
python main.py
```

## 🧪 自动化测试

项目使用 pytest 对 CSV 存储模块进行测试。

运行测试：

```
python -m pytest -v
```

目前测试覆盖的场景包括：

- 正常数据的保存与读取（Round Trip）
    
- 空列表的保存与读取
    
- CSV 文件不存在时的处理
    
- CSV 数据格式异常时的处理
    

## 📚 学习收获

通过本项目，实践并巩固了以下知识：

1. **面向对象编程**：类、对象、实例属性、实例方法及魔法方法。
    
2. **模块化设计**：通过多个 Python 文件划分职责，使用 import 实现模块协作。
    
3. **数据持久化**：使用 CSV 模块实现结构化数据的读取与写入。
    
4. **异常处理**：使用 try-except 处理常见运行时错误。
    
5. **数据校验**：使用条件判断和正则表达式验证用户输入。
    
6. **自动化测试**：使用 pytest、assert 和 monkeypatch 测试程序功能。
    
7. **版本管理**：使用 Git 和 GitHub 管理项目代码。
    

## 🔮 后续改进方向

- 优化用户交互界面。
    
- 完善数据校验和异常处理。
    
- 增加学生信息展示、排序和统计功能。
    
- 探索使用 SQLite 数据库替代 CSV 文件。
    
- 进一步完善单元测试覆盖率。
    

---

**Author:** C1X-start

**Project:** Student Management System V2

**Purpose:** Python OOP & Software Development Practice