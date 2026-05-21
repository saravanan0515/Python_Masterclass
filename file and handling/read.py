file =  open ("notes.txt","r")
#now we  have that notes.txt so we can read the data in the notes.txt.
content = file.read() # we use content as variable to get the value from the txt file and print it.

print("file content:\n",content)
file.close()

#output
#file content:
# welcome to the file (created)!
#new file created bcz file not exist!!