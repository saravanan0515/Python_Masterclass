#let we use string methods

driver_name = "sAravanan" #its is a string variable and we can use string methods on it
#we used mix of lower and upper case letters to show the use of string methods
print(driver_name.lower()) #this will convert all the letters to lower case
print(driver_name.upper()) #this will convert all the letters to upper case
print(driver_name.capitalize()) #this will convert the first letter to upper case and the rest to lower case
print(driver_name.title()) #this will convert the first letter of each word to upper case and the rest to lower case


mobile="9983456789"
masked=mobile[:2] + "******" + mobile[-2:] #this is used to mask the mobile number and show only the first 2 and last 2 digits
print("Driver Number:", masked) #output will be like this Driver Number: 99******89
print("driver name:",driver_name.title()) #output will be like this Driver Name: Saravanan


song = "let iT be"
airtist = "saravanan"
formatted= f"{song.title()} by {airtist.title()}" #this is used to format the string and show the song name and artist name in title case

print(formatted) #output will be like this Let It Be by Saravanan







#here we show how to use string method in pickup app like change the loction after the booking is done
location =  "cbe"
fixed_location = location.replace("cbe","madurai") #this is used to replace the location with the new location after the booking is done
print("pickup location:",fixed_location) #output will be like this pickup location: madurai




message  = "your rapido otp is :12sfc2.please do not share it with anyone"
otp = message.split(":")[1].split(".")[0].strip()#this is used to extract the otp from the message by splitting the message and getting the otp from it
#mean frist we split the message by ":" and before the ":" is index 0 and after the ":" is index 1,in index 1 we have the otp and the rest of the message,
# then we split the otp by "." and before the "." is index 0 and after the "." is index 1, so we get the otp from index 0 and store it in the otp variable
#the sprip() method is used to remove any extra spaces from the otp variable
print("your otp is:",otp) #output will be like this your otp is: 12sfc2




#DELIMITERS
#delimiter is know as the character that is used to separate the values in a string, in this case we use ":" and "." as delimiters to split the message and extract the otp from it.


#NEXT WE USE IF CONDITION TO FIND THE TARGET WORD IN THE STRING

message = "use rapido2e44 to get off on your first ride "
if "rapido2e44 " in message: #this is used to check if the target word is present in the message or not, if it is present then it will print the message below otherwise it will not print anything
    print("your discount code appilied for your first ride") #output will be like this you have a discount code for your first ride 


#NOW USE FIND TO FIND THE INDEX OF THE TARGET WORD IN THE STRING

feedback =  "the driver was very good and the ride was comfortable"
print("position is:",feedback.find("good")) #this is used to find the index of the target word in the string, if the target word is present in the string then it will return the index of the first occurrence of the target word, otherwise it will return -1



 #now we find the initital letter of word given
name = "saravanan maluventhi" #i used 2 words to show the use of split method to get the first letter of each word
initials = "".join([word[0].upper() for word in name.split()]) # we used join method to join the first letter of each word in the name variable .
#we used for loop,and frist we use word[0] to get the first letter of each word and then use for loop for word in name.split() to split the name variable into words and get the first letter of each word, then we use upper method to convert the first letter to upper case and then we use join method to join the first letter of each word in the name variable and store it in the initials variable.
#and we used upper method to convert the first letter to upper case 
#and we used split method to split the name variable into words and get the first letter of each word
#if i didnt give join method the output will be like this ['S', 'M'] because we used list comprehension to get the first letter of each word and store it in a list, but if we use join method then it will join the first letter of each word and give the output as SM
print("initials:",initials) #output will be like this initials: SM




#NOW WE USE STRIP METHOD TO REMOVE THE EXTRA SPACES FROM THE STRING

dirty_name = "     sar   " #this is used to show the use of strip method to remove the extra spaces from the string
cleaned = dirty_name.strip() #this is used to remove the extra spaces from the string and store it in the cleaned variable
print("cleaned name:",cleaned) #output will be like this cleaned name: sar

#if we didnt use strip method the output will be like this cleaned name:      sar   because we have extra spaces in the dirty_name variable, but if we use strip method then it will remove the extra spaces and give the output as cleaned name: sar




#NOW WE LEN TO COUNT THE LENGTH OF THE STRING

word1 = "the trip was good and the driver was friendly"
count_words = len(word1.split()) #this is used to count the number of words in the string by splitting the string into words and counting the number of words in the list
print ("no of words :",count_words) #output will be like this no of words : 8 because we have 8 words in the string variable word1
count_frequent= word1.count("the") #this is used to count the number of occurrences of the target word in the string, if the target word is present in the string then it will return the number of occurrences of the target word, otherwise it will return 0
print("count of the word 'the':",count_frequent) #output will be like this count of the word 'the': 3 because the target word "the" is present 3 times in the string variable word1