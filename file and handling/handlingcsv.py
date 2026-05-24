with open("inputfile.csv","r") as infile, open("outputfile.csv","w") as outfile:
#here we created inputfile.csv but not outputfile.csv ,so we read a data from inputfile.csv and write to the outputfile.csv.
#using for loop and for variable is line for infile,so read line by line and write the line in outfile(outputfile.csv).
    for line in infile:
        print(line.strip())
        outfile.write(line)

"""
output
id,name,age
1,john,25
2,alice,30
3,bob,22
"""