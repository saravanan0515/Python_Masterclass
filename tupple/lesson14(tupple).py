#tupple is like list but this is immutable\
#use () this for tupple
#use multiple data type

#tupple is faster than list WHEN READ ONLY,bcz we didnt use anything like append and thats like functions

#sample for tupple
trip_summary =("ubergo","chennai","airport",450.00,"completed")
print(trip_summary)

#output is 
#("ubergo","chennai","airport",450.00,"completed")

#access with index 
print(trip_summary[1])

#output chennai 


#LOOPING IN TUPPLE

for  item in trip_summary:
    print(item)

#output
#ubergo
#chennai
#airport
#450.0
#completed


#find len
print(len(trip_summary))
#output=5

#count and index 

print(trip_summary.count("completed")) #ourput = 1 ,if we have 2 completed in tupple ,we get 2 in output
print(trip_summary.index("airport")) #output= 2

