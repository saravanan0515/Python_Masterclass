# LOOPING 
#in for loop we cant give the condition like while loop, we can only give the sequence to iterate over, but in while loop we can give the condition to execute the block of code repeatedly as long as the condition is true.
#FOR LOOP  ,for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.
#SYNTAX for variable in sequence:
#    #code to execute for each item in the sequence

name = ["saravanan","maluventhi","saran"]
for i in name: #this is used to iterate over the list of names and print each name in the list, the variable i is used to store the current item in the list during each iteration of the loop
    print(i.capitalize()) #output will be like this saravanan maluventhi saran each name will be printed in a new line because we use print function to print each name in the list

#here the i is used to store the current item in the list during each iteration of the loop, so in the first iteration i will be "saravanan", in the second iteration i will be "maluventhi" and in the third iteration i will be "saran" and then it will print each name in the list.