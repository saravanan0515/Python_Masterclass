

count=5 #here we us ethis count outside the while so its a global variable and we can use it inside the while loop, if we declare the count variable inside the while loop then it will be a local variable and we cannot use it outside the while loop, so we need to declare the count variable outside the while loop to make it a global variable and use it inside the while loop.
while count > 0:
    print (f"countdown : {count}") # this is used to print the count variable in each iteration of the loop, the output will be like this countdown : 5 countdown : 4 countdown : 3 countdown : 2 countdown : 1 each count will be printed in a new line because we use print function to print each count in the loop
    count -= 1 # this is used to decrement the count variable by 1 in each iteration of the loop, so that it will eventually reach 0 and exit the loop, if we dont decrement the count variable then it will be an infinite loop because the count variable will always be greater than 0 and the loop will never exit, so we need to decrement the count variable by 1 in each iteration of the loop to make it eventually reach 0 and exit the loop
    #mean frist intragtion count is 5 then it will print countdown : 5 and then it will decrement the count variable by 1 and then it will be 4 and then it will print countdown : 4 and then it will decrement the count variable by 1 and then it will be 3 and then it will print countdown : 3 and then it will decrement the count variable by 1 and then it will be 2 and then it will print countdown : 2 and then it will decrement the count variable by 1 and then it will be 1 and then it will print countdown : 1 and then it will decrement the count variable by 1 and then it will be 0 and then the loop will exit because the count variable is no longer greater than 0, so the output will be like this countdown : 5 countdown : 4 countdown : 3 countdown : 2 countdown : 1 each count will be printed in a new line because we use print function to print each count in the loop
print("blast off") # this is used to print blast off after the loop has exited, so the output will be like this blast off because we use print function to print blast off after the loop has exited



# if we use true in while loop then it will be an infinite loop because the condition will always be true and the loop will never exit, so we need to use a condition that will eventually become false to make the loop exit, for example we can use count > 0 as the condition in the while loop and then decrement the count variable by 1 in each iteration of the loop to make it eventually reach 0 and exit the loop, so the output will be like this countdown : 5 countdown : 4 countdown : 3 countdown : 2 countdown : 1 each count will be printed in a new line because we use print function to print each count in the loop and then blast off because we use print function to print blast off after the loop has exited



#cart methods

items =[]
while True:
    item= input("enter the item to add to the cart (or 'done' to finish): ") # this is used to take input from the user to add items to the cart, the user can enter items one by one and then when they are done they can enter 'done' to finish adding items to the cart
    if item.lower() == 'done': # this is used to check if the user has entered 'done' to finish adding items to the cart, if they have entered 'done' then it will break the loop and exit the loop
        break # this is used to exit the loop when the user has entered 'done' to finish adding items to the cart
    items.append(item) # this is used to add the item entered by the user to the items list, so that we can keep track of the items added to the cart, the append method is used to add an item to the end of the list, so each item entered by the user will be added to the end of the items list, so that we can keep track of all the items added to the cart
print("items in the cart:", items) # this is used to print the message "items in the cart:" before printing the items in the cart, so that the user knows that the items being printed are the items in the cart
