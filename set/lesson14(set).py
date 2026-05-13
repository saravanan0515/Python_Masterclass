# the set 
# the set is unordered
#unlike list 
#its doesnt have index value
#set eliminate the dupilicate

#a={1,2,3}
#we can change the list into set like using a=set{[1,2,3]}


uber_cities = ["chn","bng","mad","mad"]
unique_cities=set(uber_cities)
print(unique_cities)

#set remove the dupiliacte mad and output is like "bng,chn,mad"

#union method 
uber_cities1= {"chn","bng","mad","mad"}
uber_cities2= {"bng","kar","up","delhi"}
print("union of cite 1,2:",uber_cities1.union(uber_cities2))

#output  {'up', 'kar', 'chn', 'bng', 'delhi', 'mad'}

#intersection

print("the intersection of 1,2:",uber_cities1.intersection(uber_cities2))
#output is only comman:the intersection of 1,2: {'bng'}

#difference 
print("the diffrence is :",uber_cities1.difference(uber_cities2))

#output  is =the diffrence is : {'mad', 'chn'}

#interchange 
print("the diffrence is :",uber_cities2.difference(uber_cities1))

#output for interchange:the diffrence is : {'up', 'kar', 'delhi'}

#add item
uber_cities1.add("karur")
#add in any place
print(uber_cities1)
#assign in any place ,the output is :{'karur', 'bng', 'mad', 'chn'}

#remove 
uber_cities1.remove("mad")
print("after removed madurai:",uber_cities1)

#output
#after removed madurai: {'chn', 'karur', 'bng'}

#discard ,is used to check if our value is in the item set,like if we want to remove 8 from set but we  dont know 8 is in the set 
#its like deleting process but its check and remove ,if there is not value match to the given value ,then its not execute 
my_set= {1,2,3}
print(my_set)
#output =1,2,3
my_set.discard(8)
print(my_set)
#but its give the sane output ,bcz 8 is not in the set
 