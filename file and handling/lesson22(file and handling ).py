"""mode in file and handling 
r= read only (file must exist)
w= write only (overwrites or creates)
a=append only(adds to end of file)
r+ = read+write(file must m=exist)
w+ = write+read(overwrites or creates)
a+ = append +read(create if not exists)
rb = read binary 
wb = write binary 
ab = append binary 
"""
 #sample
print("--sample 1--")
file = open("notes.txt","w") # we used write mode ,so it will create or overwrite the file
#i dont have notes.txt but if i use w ,that will create the file name as notes.txt.
file.write("welcome to the file (created)!\n")
file.write("new file created bcz file not exist!!\n")
file.close() # must to close the opened file.
# after the execution ,we can see that notes.txt is created