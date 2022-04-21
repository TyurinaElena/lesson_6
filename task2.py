import configparser
import pickle
import os
import argparse

print(os.getcwd())

class Student:
    def __init__(self, lastname, name, age, group):
        self.lastname = lastname
        self.name = name
        self.age = age
        self.group = group
    def __str__(self):
        return f"Студент {self.lastname} {self.name}, {self.age} лет, группа {self.group}"

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help="Путь к файлу настроек")

args = parser.parse_args()

if os.path.exists(args.path):
    config = configparser.ConfigParser()
    config.read(args.path, encoding="UTF-8")
    st1 = Student(config["Student1"]["lastname"],
                  config["Student1"]["name"],
                  config["Student1"]["age"],
                  config["Student1"]["group"])
    st2 = Student(config["Student2"]["lastname"],
                  config["Student2"]["name"],
                  config["Student2"]["age"],
                  config["Student2"]["group"])
    st3 = Student(config["Student3"]["lastname"],
                  config["Student3"]["name"],
                  config["Student3"]["age"],
                  config["Student3"]["group"])
    pickled_st1 = pickle.dumps(st1)
    pickled_st2 = pickle.dumps(st2)
    pickled_st3 = pickle.dumps(st3)
    with open("students.txt", "wb") as f:
        f.write(pickled_st1)
    with open("students.txt", "ab") as f:
        f.write(pickled_st2)
        f.write(pickled_st3)
else:
    print("Такого файла нет")


