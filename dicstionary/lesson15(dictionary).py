#dicstionarysave in key and value 
print("---op for sample 1---")
trip ={
    "trip_id":"UBH947",
    "pickup":"chennai central",
    "drop" : "airport",
    "fare": 430.34,
    "driver":"ravi",
    "status":"completed"
}
#structure of dicstionary
print(trip["driver"])#output is ravi
print(trip["pickup"]) #output is chennai central

#GET METHOD
#use to safe way to use,like if we search with value that must lead to error,but we use get method to avoid ,these show none
print(trip.get("airport"))
 #output is none ,bcz airport is value

print(trip.keys())
#show all the keys in the dicstionarywe use
print(trip.values())
#show the all values 

for key,value in trip.items():
    print(key,":", value)
#output is :
# trip_id : UBH947
#pickup : chennai central
#drop : airport
#fare : 430.34
#driver : ravi
#status : completed

#UPADTE 
trip.update({"car_model":"benz"})
#its will update if the car model key is in dicstionaryelse it will add to the dictionary.
print(trip)
#output is={'trip_id': 'UBH947', 'pickup': 'chennai central', 'drop': 'airport', 'fare': 430.34, 'driver': 'ravi', 'status': 'completed', 'car_model': 'benz'}

trip.update({"car_model":"audi"})
print(trip)
#frist it add the key then if we update again it will update the key
#output is like =={'trip_id': 'UBH947', 'pickup': 'chennai central', 'drop': 'airport', 'fare': 430.34, 'driver': 'ravi', 'status': 'completed', 'car_model': 'benz'}
#{'trip_id': 'UBH947', 'pickup': 'chennai central', 'drop': 'airport', 'fare': 430.34, 'driver': 'ravi', 'status': 'completed', 'car_model': 'audi'}

#it work under the method upsert:mean if key is already in dicstionaryit will update or else it will insert.

#use pop method
trip.pop("status")#remove the last element

#we can use multiple value

trip.update({"pickup":["madurai","cbe","chennai"]})
print(trip)
for k ,v in trip.items():
    print(k,":",v)

#output
#trip_id : UBH947
#pickup : madurai,cbe,chennai
#drop : airport
#fare : 430.34
#driver : ravi
#car_model : audi

print(trip["pickup"][1])#output is = cbe

#using for loop in seprate key 
for location in trip["pickup"]:
    print(location)
#output only show the list of pickup :trip_id : UBH947
#madurai
#cbe
#chennai

#we can store more no of dicstionary in list 
 