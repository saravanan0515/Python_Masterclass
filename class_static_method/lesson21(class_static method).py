# sample one
print("-- op for sample 1--")
class myclass:
    def instance_method(self):
        print("called instance method")
    
    @classmethod
    def class_method(cls):# we need to give cls for this classmethod
        print("called clas method")
    

    @staticmethod
    def static_method():
        print("called static method")
    
#creatting obj for class
obj=myclass()
obj.instance_method()
#but in class method we dont need obj
myclass.class_method()
myclass.static_method()

 
#sample 2
print("----sample2----")

class employee:
    company= "openAi" #class level data

    @classmethod
    def change_company(cls,new_name): #here new company name should store in new_name
        cls.company = new_name #accessing class variable 

    
    @staticmethod
    def try_change_company(new_name):
        company = new_name #ITS LOCAK LEVEL VARIABLE SO WE DOESNT OVERWRITNG THE CLASS VARIBALE .


#call both methods
employee.change_company("google")
print("after classmethod:",employee.company)
employee.try_change_company("meta")
print("after static method :",employee.company)

