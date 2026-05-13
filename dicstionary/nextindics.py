#we can store more no of dicstionary in list 
trips = [
    {"trip_id":"UBGF23" , "pickup_up": "chennai", "drop":"airport","fare":235},
    {"trip_id":"UBGF44" , "pickup_up": "t-nagar", "drop":"valechery","fare":233},
    {"trip_id":"UBG455" , "pickup_up": "tambaram", "drop":"central","fare":244}
]

for trip in trips:
    print(trip["trip_id"])
#only show the all trip_id in trips 


#another metjod without using list,but we need to manually define the value 
#like assigning for certain user
trips = {
   "UBGF23": {"trip_id":"UBGF23" , "pickup_up": "chennai", "drop":"airport","fare":235},
   "UBGF44": {"trip_id":"UBGF44" , "pickup_up": "t-nagar", "drop":"valechery","fare":233},
   "UBG455": {"trip_id":"UBG455" , "pickup_up": "tambaram", "drop":"central","fare":244}
}

print("UBGF23 fare ",trips["UBGF23"]["fare"])
#output is UBGF23 fare  235

for trip_id ,details in trips.items():
    print(trip_id)
    print(details["pickup_up"],"->",details["drop"])

#output is 
#UBGF23
#chennai -> airport
#UBGF44
#t-nagar -> valechery
#UBG455
#tambaram -> central
