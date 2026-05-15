from DADCODE import dad
from grandfather import grandfather
#HERE HYBRID METHOD IS USED LIKE WE USED MULTILEVEL AND MULTIPLE INHERITANCE IN SAME CODE.
print("IN THIS CODE WE HAVE MULTILEVEL AND MULTIPLE INHERITANCE IN SAME CODE AND KNOW AS HYBRID")
#HERE  THIS IS FOLDER NAME INHERIT AND FILE NAME DADCODE AND WE IMPORT THE DAD CLASS
print("--multi level  AND MULTIPLE inheritance--")
#HERE WE USE BOTH DAD AND GRANDFATHER CLASS FOR SON 1 ,THIS IS THE MULTIPLE INHERITANCE.
class son(dad,grandfather):#we can acess the father and grandfather class by relation 
    def factory(self):

        print("white")
    def house(self):
        print("yellow")
        #we are change the dad house color from the son code using the import and inheritance
    def car(self):
        print("red car")
        #dow here son 2 only relation with the dad only he didnt use the grandfather properties.
class son2(dad):#HERE WE CREATED 2 CHILD CLASS FRO DAD BUT HER ETHE QUESTION IS ,CREATING THE OBJECT FOR WHICH ???
    def market(self):
        print("fish market")
    
g=son2()
g.house() #he can use the house but he didnt use the son 1 properties
g.market()#he only acess the market and house from the parent dad class
s= son()  
s.factory()
s.house()
s.car()

