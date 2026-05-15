#class and object under the oops concepts
#class is kind of classroom like having many objects like student and table,board,etc..
#if we use def inside the class is know as method ,if outside the class its known as function.
 # ex
"""
class student:
    def say_hello(self): # here using self is rule 
        print("hi,im a student!")
s1=student() #here this is a caller to call the method to execute 
s1.say_hello() #here we call the method using the caller s1
#here this is how python understand s1.say_hello(s1),calling from s1 
"""
#another ex
print("---op for sample 1---")
class student:
    def __init__(self, name, grade):
        self.name =  name
        self.grade = grade

    def display(self):
         print(f"{self.name} is in grade{self.grade}")

#using multiple subject
s1=student(name= "abi",grade= 1)
s2=student(name="aj",grade=2)
s3=student(name="sar",grade=3)

s1.display()
s2.display()
s3.display()

#output is 
#abi is in grade1
#aj is in grade2
#sar is in grade3
