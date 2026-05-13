#input method





#wrong method

x= input("enter the value for x:")
y= input("enter the value for y:")

print((x) + (y)) # this WORNG bcz input method always takes the input as string and when we try to add two strings then it will concatenate them instead of adding them as numbers, so we need to convert the input to integer using int() method before adding them.

"""
#output like addding a string ,
enter the x : 4
enter a Y:5
45
"""





#input method

x= input("enter the value for x:")
y= input("enter the value for y:")

print(int(x) + int(y))  # this is the correct method to add two numbers taken as input from the user, 
#we need to convert the input to integer using int() method before adding them, otherwise it will concatenate them as strings.



#another method
# we can also convert the input to integer while taking the input from the user, 
# this is a better method as it will save us from converting the input to integer every time we want to use it as a number. 

x= int(input("enter the value for x:"))  
y= int(input("enter the value for y:"))
print(x+y)