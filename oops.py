


# class Laptop:

#     def __init__(self,name,processor):
#         self.name = name
#         self.processor = processor

#     def printOutput(self):
#         print("My Laptop name is :",self.name,"and the processor is :",self.processor)

#     # def config(self):
#     #     print("PAVILION","i7","516GB")

# laptop1 = Laptop("Pavilion","i7")
# laptop2 = Laptop("hp","i7")

# laptop1.printOutput()
# laptop2.printOutput()

# # laptop1.config()
# # laptop2.config()

# # print(laptop1)
# # print(laptop2)


# class Person:

#     def __init__(self,name,rollNo):
#         self.name = name
#         self.rollNo = rollNo

#     def printOutput(self):
#         print("My name is :",self.name,"and roll no is :",self.rollNo)

# person1 = Person("Ram","33")
# person2 = Person("Mehroj","55")

# person1.printOutput()
# person2.printOutput()
# print(id(person1))
# print(id(person2))

# class Person:
#     def __init__(self):
#         self.name = "Sriram"
#         self.age = 18

#     def updateName(self,name):
#         self.name = name

#     def compareAge(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False

# person1 = Person()
# person2 = Person()

# if person1.compareAge(person2):
#     print("They are of same age")
# else:
#     print("They are of different age")
# # person1.updateName("Ram")

# print(person1.name, person1.age)
# print(person2.name, person2.age)





# class Car:

#     wheels = 4

#     def __init__(self,brand,mil):
#         self.brand = brand
#         self.mil = mil

# car1 = Car("Range rover",15)
# car2 = Car("BMW",12)

# Car.wheels = 3

# print(car1.brand,car1.mil,car1.wheels)
# print(car2.brand,car2.mil,car2.wheels)


class Student:

    numberofSubjects = 5

    def __init__(self,marks1,marks2,marks3):
         self.web = marks1
         self.python = marks2
         self.math = marks3

    # def averageCalc(self):
    #     print((self.web+self.python+self.math)/3)

    # def getMarks(self):
    #     return self.math   #ACCESSORS

    # def setMarks(self,marks):
    #     self.math = marks   #MUTATORS        

    @classmethod
    def classMethodExample(cls):
        return cls.numberofSubjects

    @staticmethod
    def saticMethodExample():
        print("This is an example of static method")

student1 = Student(5,4,3)
student2 = Student(7,8,9)
student3 = Student(1,6,9)

print(Student.classMethodExample())
Student.saticMethodExample()

# print(student1.averageCalc)
# print(student2.averageCalc)
# print(student3.averageCalc)