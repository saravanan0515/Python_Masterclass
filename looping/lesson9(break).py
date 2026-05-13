#break statement is used to exit a loop prematurely when a certain condition is met. It can be used in both for and while loops. When the break statement is encountered, the loop is immediately terminated, and the program continues with the next statement after the loop.

#break in for loop

for i in range (10): # here we used range function to generate a sequence of numbers from 0 to 9 and then we used for loop to iterate over the sequence of numbers and print each number in the sequence
    if i == 5: # this is used to check if the current number in the sequence is equal to 5, if it is equal then it will break the loop and exit the loop
        break # this is used to exit the loop when the current number in the sequence is equal to 5
    print(i) # this is used to print each number in the sequence until it reaches 5, once it reaches 5 then it will break the loop and exit the loop
    #we out from if and print in for loop, so it will print the numbers from 0 to 4 and then it will break the loop when it reaches 5 and exit the loop, so the output will be like this 0 1 2 3 4 each number will be printed in a new line because we use print function to print each number in the sequence

#same exapmle 

id = [1,2,3,4,8,6,7,8,5,9,10] # this is a list of numbers from 1 to 10 but the number 5 is in the middle of the list
for i in id: # this is used to iterate over the list of numbers and print each number in the list, the variable i is used to store the current item in the list during each iteration of the loop
    if i == 5: # this is used to check if the current number in the list is equal to 5, if it is equal then it will break the loop and exit the loop
        break # this is used to exit the loop when the current number in the list is equal to 5
    print(i) # this is used to print each number in the list until it reaches 5, once it reaches 5 then it will break the loop and exit the loop, so the output will be like this 1 2 3 4 8 6 7 8 each number will be printed in a new line because we use print function to print each number in the list


#exa,ple for while loop
count = 0 # count is a variable to store the count of numbers from 0 to 9
while count < 10: # this is used to execute a block of code repeatedly as long as the count is less than 10
    if count == 5: # this is used to check if the count is equal to 5, if it is equal then it will break the loop and exit the loop
        break # this is used to exit the loop when the count is equal to 5
    print(count) # this is used to print the count until it reaches 5, once it reaches 5 then it will break the loop and exit the loop, so the output will be like this 0 1 2 3 4 each number will be printed in a new line because we use print function to print each number in the sequence
    count += 1# this is used to increment the count by 1 in each iteration of the loop, so that it will eventually reach 10 and exit the loop