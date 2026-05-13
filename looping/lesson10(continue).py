# the continue statement is used to skip the current iteration of a loop and move on to the next iteration. It can be used in both for and while loops. When the continue statement is encountered, the rest of the code inside the loop for that iteration is skipped, and the loop continues with the next iteration.

#continue in for loop
n=[1,2,-2,4,5,-1,7,8,-9,10] # this is a list of numbers from 1 to 10 but it also contains some negative numbers, we will use continue statement to skip the negative numbers and print only the positive numbers in the list
for num in n :
    if num < 0: # this is used to check if the current number in the list is less than 0, if it is less than 0 then it will skip the rest of the code inside the loop for that iteration and move on to the next iteration
        continue # this is used to skip the current iteration of the loop when the current number in the list is less than 0
    print(num) # this is used to print each number in the list until it reaches a negative number, once it reaches a negative number then it will skip that iteration and move on to the next iteration, so the output will be like this 1 2 4 5 7 8 10 each number will be printed in a new line because we use print function to print each number in the list
# here we skip the negative numbers in the list and print only the positive numbers in the list, so the output will be like this 1 2 4 5 7 8 10 each number will be printed in a new line because we use print function to print each number in the list


#Example for while loop
count = 0 # this is a variable to store the count of numbers from 0 to 9
while count < 10: # this is used to execute a block of code repeatedly as long as the count is less than 10
    count += 1 # this is used to increment the count by 1 in each iteration of the loop, so that it will eventually reach 10 and exit the loop
    if count % 2 == 0: # this is used to check if the count is even or not, if it is even then it will skip the rest of the code inside the loop for that iteration and move on to the next iteration
        continue # this is used to skip the current iteration of the loop when the count is even
    print(count) # this is used to print each number in the sequence until it reaches an even number, once it reaches an even number then it will skip that iteration and move on to the next iteration, so the output will be like this 1 3 5 7 9 each number will be printed in a new line because we use print function to print each number in the sequence



#PASS statement is used as a placeholder for code that is not yet implemented. It allows you to write code that is syntactically correct but does not do anything. When the pass statement is encountered, it does nothing and the program continues with the next statement after the pass statement.

num= [1,2,3,4,5]
for i in num:
    pass # this is used as a placeholder for code that is not yet implemented, it does nothing and the program continues with the next statement after the pass statement, so the output will be nothing because we are not doing anything in the loop
