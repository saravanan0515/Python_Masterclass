import csv 
#bcz we use camma datas
with  open("inputfile.csv","r") as file:
    reader = csv.DictReader(file)
    #we used dictreader bzc we dont have a database ,we we converting inputfile.csv as dicstionary , so that take first line as header,
    for row in reader:
        print(row["age"])
        #it take only age row

    

#WE CAN USE ANOTHER METHOD IN ARRAY
'''
with  open("inputfile.csv","r") as file:
    lines = file.readlines()
    for line in lines[1:]: # we use [1:] mean skip the header
        columns = line.strip().split(",") # we used split to mention data in speration of camma,
        #columns[0],columns[1],columns[2]
        print("age:",columns[2]) # age column
        print("name:",columns[1])
'''