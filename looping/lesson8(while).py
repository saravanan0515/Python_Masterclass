#different between for and while loop ,while loop is used to execute a block of code repeatedly as long as a certain condition is true, while for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.
#if the password is correct then it will print the message below otherwise it will keep asking for the password until the correct password is entered, this is an example of while loop because we are executing a block of code repeatedly as long as a certain condition is true.

password = "saravanan" 
entered_password = input("enter your password: ") #this is used to take input from the user and store it in the entered_password variable
while entered_password != password: #this is used
    print("incorrect password, please try again") #output will be like this incorrect password, please try again if the user enters the wrong password
    entered_password = input("enter your password: ") #this is used to take input from the user and store it in the entered_password variable again to check if the password is correct or not
#if we come out from the while loop then it means that the user has entered the correct password and then it will print the message below
print("welcome to the system") #output will be like this welcome to the system if the user enters the correct password  


#here,the detailed explanation of our code is like this, we have a variable called password which is used to store the correct password, then we take input from the user and store it in the entered_password variable, then we use a while loop to check if the entered_password is not equal to the password, if it is not equal then it will print the message "incorrect password, please try again" 
# and then it will take input from the user again and store it in the entered_password variable,
#  this process will continue until the user enters the correct password, once the user enters the correct password then it will come out of the while loop and print the message "welcome to the system".