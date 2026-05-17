#there is three method like public,private ,protected.
#normal variable is pubic
#if _ come before the variable is protected
#if __ come before the variable is private
class parent:
    def __init__(self):
        self.public_var = "iam a public"
        self._protected_var = "im protected"
        self.__private_var = "im private"
    
    def access_from_same_class(self):
        print("inside parent class:")
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        print("private:",self.__private_var)

class child(parent):
    def access_from_subclass(self):
        print("inside child class (subclass):")
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        #HERE WE USE THE TRY AN EXCEPTION TO HANDLE THE ERROR
        #BECAUSE PRIVATE VAR DOESNT ACCESS IN THE SUBCLASS
        #SO WE KNOW IF WE ACCESS THATS MAKE A ERROR.
        try:
            print("private:",self.__private_var)
        except AttributeError:
            print("private :cannot access(attributeerror)")
 
 
 
 
 #we can access private var from any class with  one method
#use  try:
            #print("private:",self._parent__private_var)
#                                 see here we used parent class so it not goes exception output.

        try:
            print("private:",self._parent__private_var)
        except AttributeError:
            print("private :cannot access(attributeerror)")





class stranger : #no connection between parent and child class.
    def access_from_other_class(self, obj):
        print("inside stranger  class (unrelated):")
        print("public:",obj.public_var)
        print("protected:",obj._protected_var) #not recommand
        #HERE WE USE THE TRY AN EXCEPTION TO HANDLE THE ERROR
        #BECAUSE PRIVATE VAR DOESNT ACCESS IN THE SUBCLASS
        #SO WE KNOW IF WE ACCESS THATS MAKE A ERROR.
        try:
            print("private:",obj.__private_var)
        except AttributeError:
            print("private :cannot access(attributeerror)")
       
        

p=parent()
c=child()
s=stranger()

print("\n access from same class")
p.access_from_same_class()

#output is :
# access from same class
#inside parent class:
#public: iam a public
#protected: im protected
#private: im private



print("\n access from child class")
c.access_from_subclass()

 #access from child class
#inside child class (subclass):
#public: iam a public
#protected: im protected
#private :cannot access(attributeerror)
#private: im private



print("\n access from stranger  class")
s.access_from_other_class(p) #acces the parent from the stranger by p.

#access from stranger  class
#inside stranger  class (unrelated):
#public: iam a public
#protected: im protected
#private :cannot access(attributeerror)