"""
types of exceptions

ZerDivisionError = divifing a number by zero 10/0
ValueError= invalid vlaue for a function(e.g int("abc"))  int ("hello")
TypeError=wrong data type used in operation "abc"+10
IndexError = accessing out of range list index my_list[10]
Keyerror = accessing a non-existing key in dictionaryy my_dict["not found"]
AttributeError =accessing a  non-existing attribute of an object none.upper()
FileNotFoundError =file not found when opening open("abc.txt")
ImportError= trying to import a missing module import notamodule
NameError =using a varibale that was never defined  print(xzy)
SyntaxError = writing invalid python code if true print("hi")
IndentationError -incorrect indentation
RuntimeError = generic error not falling into other categories rare cases
StopIteration= raised by next() when iterator is exhausted in loop and generators
MemoryError = program run out of memory working with huge data
RecursionError =too many recursive calls A fumction calls itself endlessly

"""

#WE CAN USE SIMPLY EXCEPTION TO HANDLE ANY EXCEPTIONS

#sample 1
print("---sample1---")
try:# if we didnt use try ,then if we give 0 for no of items ,that lead to error
    number_of_items = int(input("how many items:"))
    total_price= 200*number_of_items
    average_price=total_price / number_of_items
    print("average price:",average_price)
except Exception: # else we give ZeroDivideError 
    print("you cannot order 0 items,plz buy more than 0")

#FINALLY - IT ALWAYS EXECUTE
finally:
    print("it always execute even exception occur")
print("next block")

#output
#---sample1---
#how many items:2
#average price: 200.0
#next block

#---sample1---
#how many items:0
#you cannot order 0 items,plz buy more than 0
#next block

#WE CAN USE MORE THAN 2 EXCEPT