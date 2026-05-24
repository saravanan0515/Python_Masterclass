#usign a with for avoiding all time to close the file 
with open("notes.txt","r") as file :
    for line in file: # using for loop to read line by line
        print(line.strip()) #using strip to clear any extra space.
        
