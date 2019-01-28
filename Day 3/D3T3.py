class Student:
    def __init__(self,name,rollno):
        self.name= name
        self.rollno=rollno
        self.marks=0
        self.age=0

    def Display(self):
        print('Name: ',self.name,'\tRollno: ',self.rollno, '\nMarks: ',self.marks,'\tAge: ',self.age)

    def getMarks(self,marks):
        self.marks=marks

    def getAge(self,age):
        self.age=age


s1=Student('Aditi',21)
marks=input('Enter the marks: ')
s1.getMarks(int(marks))
age=input('Enter the age: ')
s1.getAge(int(age))
s1.Display()
