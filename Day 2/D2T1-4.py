#Task 1

add = lambda x,y:x+y
print("Enter the number of inputs:")
N=int(input())
num = [0]
for i in range(N):
    temp=int(input())
    num.append(temp)
sum=0
for i in num:
    sum=add(sum,i)
print("sum is: ",sum)



#Task 2
n=int(input("Enter the number of students: "))
name=[]
p=[]
c=[]
m=[]
for i in range(n):
    name.append(input("Enter the name of student: "))
    p.append(input("Enter the physics marks: "))
    c.append(input("Enter the chem marks: "))
    m.append(input("Enter the maths marks: "))

fo = open("foo.csv", "w")
for i in range(n):
    fo.write(name[i]+",")
    fo.write(p[i]+",")
    fo.write(c[i]+",")
    fo.write(m[i]+"\n")
fo.close()



#Task 3
import random
def switch(n):
    if n==1:
        print("Hi Tony!")
    elif n==2:
        print("Hello Steve!")
    elif(n==3):
        print("Greetings Natasha!")
    else:
        print("Hello Stranger!")
switch(random.randint(0,4))




#Task 4

def avengerClass(n,o,cN):
    obj={'name':n,'occup':o,'codeName':cN}
    return obj
y=avengerClass("Natasha","Spy","Black Widow")
print("Name: "+y['name']+"\nOccupation: "+y['occup']+"\nCode Name: "+y['codeName'])
z=avengerClass(input("Name: "),input("\nOccupation: "),input("\nCode Name:"))
print(z)






    
