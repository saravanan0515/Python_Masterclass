#we can use readlin instead of read ,we use read for only small data,so use readline for heavy and big data like 10gb.
#read line by line like for 
with open ("file.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if "error" in line:
            print("found error:",line.strip())

#output 
#found error: error: failed to connect to db
#found error: error:null pointer exception occured

#readline used to read certain lines.

#now we see in for loop
with open("file.txt") as d:
    for _ in range(10):  #we used _ its throughaway varibale .we read only in 10 line 
        print(d.readline().strip())


#output only read and print 10 lines
#info: application started
#info:user login completed
#warning:disk sapce low
#error: failed to connect to db
#info:scheduled task started
#error:null pointer exception occured
#info:application shutdown
#info: application started
#info:user login completed
#warning:disk sapce low