class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Name(Student):
    def getName(self):
        return f"{self.name}"
    def getAge(self):
        return f"{self.age}"
    def getGender(self):
        return f"{self.gender}"
s1 = Name("John", 24, "Male")
s2 = Name("Mathew", 24, "Female")
s3 = Name("Jason", 24, "Male")
print(s1.getName())
print(s2.getName())
print(s3.getAge())
print(s1.getGender())
