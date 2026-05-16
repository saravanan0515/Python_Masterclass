#hiding the essiontial data
#this method used to make the class complusory to implement ,
#exmaple if manager give 3 empty method to implement but we implement only 2 mean it give  error to implement the missed method.
 # ex
from abc import ABC, abstractmethod
print("--op for sample 1--")
#manager assigns
class featurePlan(ABC):
    @abstractmethod
    def login(self):
        pass # empty method and passthrough method

    @abstractmethod
    def logout(self):
        pass

    #this both are abstracted methods,if i give without @abstractmethod ,this mean normal method.
    def checkout(self):
        pass
#developer implements
# making inherit with child class
class webap(featurePlan):
    def login(self):
        print("web app login done")
    def logout(self):
        print("webapp logout done")
    #if we didnt implement the logout method ,lead to error to compile without implement the logout abstractmethod.
    #but we can compile without implement this without implement the normal method like checkout.
s=webap()
s.login()
s.logout()

#output is 
#--op for sample 1--
#web app login done
#webapp logout done

#what if did implement logout
#output:TypeError: Can't instantiate abstract class webap without an implementation for abstract method 'logout.
    