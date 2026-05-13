#the function is a block of code that performs a specific task. It is reusable and can be called multiple times in a program. Functions help to break down complex problems into smaller, manageable pieces, making the code more organized and easier to read.
#the function is like we first  built code and the reuse it whenever we want to use it, so that we dont have to write the same code again and again, we can just call the function and it will execute the code inside the function, this is how functions help us to write reusable code and make our code more organized and easier to read.
#like the upper() is also a function that is used to convert a string to uppercase, we can use this function whenever we want to convert a string to uppercase without having to write the code for converting a string to uppercase again and again, we can just call the upper() function and it will convert the string to uppercase for us, this is how functions help us to write reusable code and make our code more organized and easier to read.
#defining a function is using def keyword followed by the function name and parentheses, and then a colon. The code block inside the function is indented.
#def greet(): # this is used to define a function called greet, the def keyword is used to define a function, and the parentheses are used to indicate that this is a function, and the colon is used to indicate the start of the code block inside the function
#after def is the function name which is greet in this case, we can choose any name for the function but it should be meaningful and should indicate what the function does, so that it will be easier to understand the code when we read it later, and also it will be easier to remember the function name when we want to call the function later in the code
#calling the function is using the function name followed by parentheses, and then a colon. The code block inside the function is executed when the function is called.

def great():
    print("hello world") # this is used to print the message "hello world" when the function is called, so the output will be like this hello world because we use print function to print the message "hello world" when the function is called
great() # this is used to call the function great, when we call the function great it will execute the code inside the function and print the message "hello world", so the output will be like this hello world because we use print function to print the message "hello world" when the function is called


#function with arugments

def greet(name): # this is used to define a function called greet that takes one argument called name, the argument is a variable that is used to pass information
    print(f"hello {name},welcome to the world of python") 
# this is used to print the message "hello {name}, welcome to the world of python" when the function is called, the {name} is a placeholder for the argument that we pass to the function when we call it, so when we call the function and pass an argument
greet("saravanan") # if i didnt give anything in the arugement then it will print hello , welcome to the world of python because the name variable will be empty, but if i give saravanan in the argument then it will print hello saravanan, welcome to the world of python because the name variable will be replaced with the value that we pass in the argument when we call the function, so the output will be like this hello saravanan, welcome to the world of python because we use print function to print the message "hello {name}, welcome to the world of python" when the function is called and we pass "saravanan" as an argument to the function


#output will be like this hello saravanan, welcome to the world of python because we use print function to print the message "hello {name}, welcome to the world of python" when the function is called and we pass "saravanan" as an argument to the function



#another example of function with arguments

def add(a,b): # this is used to define a function called add that takes two arguments called a and b, the arguments are variables that are used to pass information
    print(a+b) # this is used to print the sum of a and b when the function is called, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function
add(5,3) # if the arugumens(5,3) are not given then it will print 0 because the a and b variables will be empty, but if we give 5 and 3 as arguments then it will print 8 because the a variable will be replaced with 5 and the b variable will be replaced with 3 when we call the function and pass 5 and 3 as arguments to the function, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function
#if i give only value for a and not for b then it will give an error because the b variable will be empty and we cannot add an empty variable to a variable, so we need to give values for both a and b when we call the function and pass arguments to the function, so that it will print the sum of a and b when the function is called, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function, so the output will be like this 8 because we use print function to print the sum of a and b when the function is called and we pass 5 and 3 as arguments to the function
#output will be like this 8






#NOW WE SEE *args , its mean accept any argument ,like in previous code we only use a and b ,but if we use *argv then it will accept any number of arguments and store them in a tuple, so that we can use those arguments later in the code, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function


def add(*args):
    total = 0 # this is used to store the sum of all the arguments that we pass to the function when we call it, so that we can use that value later in the code, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function
    for num in args: #mean we asssign the num to args ,we used for loop so frst it take one value and plus with another value then next loop for another and plus with it it store in total variable
        total += num # this is used to add each argument to the total variable, so that we can get the sum of all the arguments that we pass to the function when we call it, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function
         #0 += 1 then total will be 1
         #1 += 2 then total will be 3
            #3 += 3 then total will be 6
                #6 += 4 then total will be 10
                    #10 += 5 then total will be 15
    return total # this is used to return the sum of all the arguments to the caller, so that we can use that value later in the code, so the output will be like this 15 because we use return statement to return the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function, so the output will be like this 15 because we use return statement to return the sum of all the arguments when the function is called and we pass 5, 3 and 7 as arguments to the function
print(add(1,2,3,4,5)) # if we give 1,2,3,4 and 5 as arguments then it will print 15 because the total variable will be updated with the sum of all the arguments that we pass to the function when we call it, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 1,2,3,4 and 5 as arguments to the function, so the output will be like this 15 because we use print function to print the sum of all the arguments when the function is called and we pass 1,2,3,4 and 5 as arguments to the function
#here frst the total will be 0 then all the 1,2,3,4,5 i n args and it will run in loop one by one and frst 1 will assign to total and + 2 then it goes to next value in loop



#NEXT LESSON IS kwargs, its mean accept any keyword argument, like in previous code we only use a and b as arguments, but if we use **kwargs then it will accept any number of keyword arguments and store them in a dictionary, so that we can use those keyword arguments later in the code, so the output will be like this {'name': 'saravanan', 'age': 25} because we use print function to print the dicstionaryof all the keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function, 
# so the output will be like this {'name': 'saravanan', 'age': 25} because we use print function to print the dicstionaryof all the keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function
 #example of kwargs

def create_profile(**kwargs):
    print("---user profile--")
    for key ,value in kwargs.items(): # this is used to iterate through the dicstionaryof keyword arguments and print each key and value, so that we can see the profile of the user that we create with the keyword arguments that we pass to the function when we call it, so the output will be like this {'name': 'saravanan', 'age': 25} because we use print function to print the dicstionaryof all the keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function, so the output will be like this {'name': 'saravanan', 'age': 25} because we use print function to print the dicstionaryof all the keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function
        #mean 2 loop name key and value ,then assign frst one is key then second one is value .
        print(f"{key}: {value}") # this is used to print each key and value in the dicstionaryof keyword arguments, so that we can see the profile of the user that we create with the keyword arguments that we pass to the function when we call it, so the output will be like this name: saravanan age: 25 because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function, so the output will be like this name: saravanan age: 25 because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan' and age=25 as keyword arguments to the function
create_profile(name="saravanan", age=25 ,job="developer") # if we give name='saravanan', age=25 and job='developer' as keyword arguments then it will print the profile of the user that we create with the keyword arguments that we pass to the function when we call it, so the output will be like this name: saravanan age: 25 job: developer because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan', age=25 and job='developer' as keyword arguments to the function, so the output will be like this name: saravanan age: 25 job: developer because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan', age=25 and job='developer' as keyword arguments to the function
#call create_profile function and pass name='saravanan', age=25 and job='developer' as keyword arguments
#output will be like this name: saravanan age: 25 job: developer because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan', age=25 and job='developer' as keyword arguments to the function, so the output will be like this name: saravanan age: 25 job: developer because we use print function to print each key and value in the dicstionaryof keyword arguments when the function is called and we pass name='saravanan', age=25 and job='developer' as keyword arguments to the function
