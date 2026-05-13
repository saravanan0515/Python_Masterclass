# list is a built-in data structure in Python that allows you to store multiple items in a single variable.
#the list is ordered, mutable, and allows duplicate elements. It is defined using square brackets [] and the items in the list are separated by commas.
#we can use multiple data types in a list, including numbers, strings, and even other lists. We can also use indexing to access specific items in the list, and we can use various methods to manipulate the list, such as adding or removing items.
#use in [] to define a list and use comma to separate the items in the list, so the output will be like this [1, 2, 3, 4, 5] because we have defined a list with 5 items and each item is separated by a comma, so the output will be like this [1, 2, 3, 4, 5] because we have defined a list with 5 items and each item is separated by a comma

#sample

playlist =  ["song1", "song2", "song3", "song4", "song5"] # this is a list of songs in a playlist, we can use multiple data types in a list, including numbers, strings, and even other lists, so the output will be like this ['song1', 'song2', 'song3', 'song4', 'song5'] because we have defined a list with 5 items and each item is separated by a comma, so the output will be like this ['song1', 'song2', 'song3', 'song4', 'song5']
fav_food = ["pizza", "burger", "pasta", "ice cream"] # this is a list of favorite foods, we can use multiple data types in a list, including numbers, strings, and even other lists, so the output will be like this ['pizza', 'burger', 'pasta', 'ice cream'] because we have defined a list with 4 items and each item is separated by a comma, so the output will be like this ['pizza', 'burger', 'pasta', 'ice cream']
recent_locations = ["home", "work", "gym", "park"] # this is a list of recent locations, we can use multiple data types in a list, including numbers, strings, and even other lists, so the output will be like this ['home', 'work', 'gym', 'park'] because we have defined a list with 4 items and each item is separated by a comma, so the output will be like this ['home', 'work', 'gym', 'park']
 # we can use this also 
mixed_list = [1, "hello", 3.14, [1, 2, 3], {"name": "John"}] # this is a list that contains multiple data types, including numbers, strings, lists, and dictionaries, so the output will be like this [1, 'hello', 3.14, [1, 2, 3], {'name': 'John'}] because we have defined a list with 5 items and each item is separated by a comma, so the output will be like this [1, 'hello', 3.14, [1, 2, 3], {'name': 'John'}] because we have defined a list with 5 items and each item is separated by a comma
print("playlist:", playlist) # this is used to print the playlist list, so the output will be like this playlist: ['song1', 'song2', 'song3', 'song4', 'song5'] because we have defined a list with 5 items and each item is separated by a comma, so the output will be like this playlist: ['song1', 'song2', 'song3', 'song4', 'song5'] because we have defined a list with 5 items and each item is separated by a comma
print("favorite foods:", fav_food) # this is used to print the fav_food list, so the output will be like this favorite foods: ['pizza', 'burger', 'pasta', 'ice cream'] because we have defined a list with 4 items and each item is separated by a comma, so the output will be like this favorite foods: ['pizza', 'burger', 'pasta', 'ice cream'] because we have defined a list with 4 items and each item is separated by a comma
print("recent locations:", recent_locations) # this is used to print the recent_locations list, so the output will be like this recent locations: ['home', 'work', 'gym', 'park'] because we have defined a list with 4 items and each item is separated by a comma, so the output will be like this recent locations: ['home', 'work', 'gym', 'park'] because we have defined a list with 4 items and each item is separated by a comma
print("mixed list:", mixed_list) # this is used to print the mixed_list list, so the output will be like this mixed list: [1, 'hello', 3.14, [1, 2, 3], {'name': 'John'}] because we have defined a list with 5 items and each item is separated by a comma, so the output will be like this mixed list: [1, 'hello', 3.14, [1, 2, 3], {'name': 'John'}] because we have defined a list with 5 items and each item is separated by a comma

#output
#playlist: ['song1', 'song2', 'song3', 'song4', 'song5']
#favorite foods: ['pizza', 'burger', 'pasta', 'ice cream']
#recent locations: ['home', 'work', 'gym', 'park']
#mixed list: [1, 'hello', 3.14, [1, 2, 3], {'name': 'John'}]




#LIST METHODS
#append method is used to add an item to the end of a list. It takes one argument, which is the item to be added, and it modifies the original list by adding the item to the end of the list.

playlist.append("song6") # this is used to add the item "song6" to the end of the playlist list, so the output will be like this ['song1', 'song2', 'song3', 'song4', 'song5', 'song6'] because we have added the item "song6" to the end of the playlist list, so the output will be like this ['song1', 'song2', 'song3', 'song4', 'song5', 'song6'] because we have added the item "song6" to the end of the playlist list
fav_food.append("sushi") # this is used to add the item "sushi" to the end of the fav_food list, so the output will be like this ['pizza', 'burger', 'pasta', 'ice cream', 'sushi'] because we have added the item "sushi" to the end of the fav_food list, so the output will be like this ['pizza', 'burger', 'pasta', 'ice cream', 'sushi'] because we have added the item "sushi" to the end of the fav_food list
print ("updated playlist:", playlist) 
print("updated favorite foods:", fav_food)


#INSERT
# the insert method is used to add an item to a specific position in a list. It takes two arguments: the first argument is the index where the item should be inserted, and the second argument is the item to be inserted. The insert method modifies the original list by adding the item at the specified index and shifting the existing items to the right.

playlist.insert(2, "song7") # this is used to add the item "song7" to the playlist list at index 2, so the output will be like this ['song1', 'song2', 'song7', 'song3', 'song4', 'song5', 'song6'] because we have added the item "song7" to the playlist list at index 2, so the output will be like this ['song1', 'song2', 'song7', 'song3', 'song4', 'song5', 'song6'] because we have added the item "song7" to the playlist list at index 2
fav_food.insert(1, "tacos") # this is used to add the item "

print("updated playlist:", playlist)
print("updated favorite foods:", fav_food)

#output
#updated playlist: ['song1', 'song2', 'song7', 'song3', 'song4', 'song5', 'song6']
#updated favorite foods: ['pizza', 'tacos', 'burger', 'pasta',


#REMOVE METHOD
# the remove method is used to remove the first occurrence of a specified item from a list. It takes one argument, which is the item to be removed, and it modifies the original list by removing the first occurrence of the specified item. If the item is not found in the list, a ValueError will be raised.                        
playlist.remove("song3") # this is used to remove the first occurrence of the item "song3" from the playlist list, so the output will be like this ['song1', 'song2', 'song7', 'song4', 'song5', 'song6'] because we have removed the first occurrence of the item "song3" from the playlist list, so the output will be like this ['song1', 'song2', 'song7', 'song4', 'song5', 'song6'] because we have removed the first occurrence of the item "song3" from the playlist list
fav_food.remove("burger") # this is used to remove the first occurrence of the item "burger" from the fav_food list, so the output will be like this ['pizza', 'tacos', 'pasta', 'ice cream'] because we have removed the first occurrence of the item "burger" from the fav_food list
print("Removed item from playlist:", playlist)
print("Removed item from favorite foods:", fav_food)

#output
#Removed item from playlist: ['song1', 'song2', 'song7', 'song4', 'song5', 'song6']
#Removed item from favorite foods: ['pizza', 'tacos', 'pasta', '



#POP METHOD
# the pop method is used to remove and return an item from a list at a specified index

playlist.pop()
# this is used to remove and return the last item from the playlist list, so the output will be like this song6 because we have removed and returned the last item from the playlist list, so the output will be like this song6 because we have removed and returned the last item from the playlist list
fav_food.pop() # this is used to remove and return the item at index 1 from the fav_food list, so the output will be like this 'tacos' because we have removed and returned the item at index 1 from the fav_food list, so the output will be like this 'tacos' because we have removed and returned the item at index 1 from the fav_food list
print("Popped item from playlist:", playlist)
print("Popped item from favorite foods:", fav_food)

#output
#Popped item from playlist: ['song1', 'song2', 'song7', 'song4', 'song5']
#Popped item from favorite foods: ['pizza', 'pasta', 'ice cream']




#REVERSING A LIST
# the reverse method is used to reverse the order of the items in a list. It modifies
playlist.reverse() # this is used to reverse the order of the items in the playlist list, so the output will be like this ['song5', 'song4', 'song7', 'song2', 'song1'] because we have reversed the order of the items in the playlist list, so the output will be like this ['song5', 'song4', 'song7', 'song2', 'song1'] because we have reversed the order of the items in the playlist list
fav_food.reverse() # this is used to reverse the order of the items in the fav_food list, so the output will be like this ['ice cream', 'pasta', 'tacos', 'pizza'] because we have reversed the order of the items in the fav_food list, so the output will be like this ['ice cream', 'pasta', 'tacos', 'pizza'] because we have reversed the order of the items in the fav_food list
print("Reversed playlist:", playlist)                       
print("Reversed favorite foods:", fav_food)

#output
#Reversed playlist: ['song5', 'song4', 'song7', 'song2', 'song1']
#Reversed favorite foods: ['ice cream', 'pasta', 'tacos', 'pizza']  





#COUNT METHOD
# the count method is used to count the number of occurrences of a specified item in a list
print("Count of 'song1' in playlist:", playlist.count("song1"))
print("Count of 'pizza' in favorite foods:", fav_food.count("pizza"))

#output
#Count of 'song1' in playlist: 1        
#Count of 'pizza' in favorite foods: 1




#SLICEING A LIST
# slicing a list is used to create a new list that contains a portion of the original list. It is done using the slice notation, which is written as list[start:stop:step]. The start index is the index of the first item to be included in the new list, the stop index is the index of the first item to be excluded from the new list, and the step is the number of items to skip between each item in the new list.
print("top 2 songs:",playlist[0:2]),#aputyna index zero la irunthu adutha 2
print("last location:",recent_locations[-2:])#-2 na last la irunthu edukum



#LIST ITERATION
print("--song list--")
for song in playlist:
    print("all song:",song)

#output
#all song: song5
#all song: song4
#all song: song7
#all song: song2
#all song: song1
print ("--food list--")
for food in fav_food:
    print(food+ " cooked by saravanan") #we use thet food variable from for loop to add cooked by saravanan

#output
#pasta cooked by saravanan
#tacos cooked by saravanan
#pizza cooked by saravanan




#CHECK IF(USED TO CHECK THE VALUE IN LIST)

if "dosa" in fav_food: # we can use list also like ["pizza", "burger", "pasta", "ice cream"] 
    print("yes dosa is availabale today")
elif "pizza" in fav_food:
    print("u can order pizza today instead of dosa")
else:
    print("dosa not available today")

#output

#dosa not available today


#UPDATE

#REAL WORLD USECASE ,LIKE IN FAV FOOD THERE IS PIZZ IS OVER AND NOT AVAILABLE WE CAN REMOVE OR CHANGE IN THE MIDLLE OF THE CODE

fav_food[0]="shawarma" #we use index value for this so index of the pizz is 0
print("todays special foods:",fav_food)


#output 
#todays special foods: ['shawarma', 'pasta', 'tacos', 'pizza']




#ex for mixed 
mixed = ["sare",20,178]
for m in mixed:
    print(m)

#ourput
#sare
#20
#178


#find the index 
#here we use 2 varibale for the for loop, bcz we have enumerate ,thats give index so we assign it for i and then print location in loaction

for i,location in enumerate(recent_locations):
    print(f"loction {i}: {location}")

#output is 
#loction 0: home
#loction 1: work
#loction 2: gym
#loction 3: park