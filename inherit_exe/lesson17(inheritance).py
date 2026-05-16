#the inheritance is code reusablity
#making parent and child relations

#sample
print("---output for sample 1---")
class dad:
    def house (self):
        print("Iam from dad class")

class test :
    def factory(self):
        print("im from factory class")

d= dad() #here d is a object that used to call the house method
d.house()

#make a another object for call the another class name as test 
t=test()
t.factory()


#NOW MAKING RELATIONSHIP BTW IN THE DAD AND SO CLASS

#sample
print("----ouptu for sample 2----")
class dad:  #PARENT
    def house (self):
        print("Iam from dad class")
#CHILD 
class son(dad):  #NOW THW SON CLASS IS IN THE RELATION TO DAD CLASS
    def factory(self):
        print("im from factory class")
 #NOW CREATE THE OBJECT FOR SON BUT ITS SHOW BOTH METHODS LIKE HOUSE AND FACTORY 
s=son()
s.house()#THIS IS SINGLE LEVEL INHERITANCE
s.factory()

#ANOTHER SAMPLE
print("---output for sapmle 3--- ")
class app1: #parent
    def v1(self):
        print("orders")
class app1_1(app1):#OVERWRITE THE PARENT CODE
    def v2(self):
        print("refund")
    def v1(self):
        print("cart")
      
a=app1_1()
a.v1() #only take from the overwritted code from the child
a.v2()

