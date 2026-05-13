#system arguments - sysargv  used to get the input before the code run
#creating the email with use of only full name
import sys

if len(sys.argv) == 2: #this is used to check the length of the command line arguments, if its 2 then it will execute the code below otherwise it will print the message and exit the program
    print ("Please provide your full name and last name as command line arguments.")
    sys.exit()  #this is used to exit the program if the length of the command line arguments is not 2

full_name = sys.argv[1]  # what is this 1 mean=> its index value of output screen after the py command like systemargv.py is 0 and sar is 1 
last_name = sys.argv[2]  # if we want to take last name as input then we can use this and also change the email format below
#format
email = full_name.lower().replace(" ", ".") + last_name.lower().replace(" ", ".") + "@gmail.com"

 
#output

print("\n ---your new profile----")
print("full name:",full_name + " " + last_name)
print("generated email:",email)



"""
#output

PS E:\design\learn py> py systemargv.py sar

 ---your new profile----
full name: sar
generated email: sar@gmail.com
"""




#another example of sysargv and best method to take input from command line

#and this is used to take full name as input from command line and print it in one line

full_name = sys.argv[1:] # this is used to get all the command line arguments after the first one and store it in a list

 #if we print this then it will print the list of command line arguments,but in seprate line,if we want to join all the command line arguments in one line then we can use the join method

full_name = " ".join(sys.argv[1:]) # this is used to join all the command line arguments in one line and store it in the full_name variable

#output :if i give sar m cbe as input then it will print sar m cbe as output


print("Full name:", full_name)


#the output email is look like sar.m.cbe@gmail.com ,
# bcz we use replace method to replace the space with dot
# and also we use lower method to convert the full name to lower case and then we add the last name and then we add the @gmail.com to generate the email address.
