#NOW WE LEARN CONDITION METHODS 
#LIKE IF CONDITION,ELSE CONDITION,ELIF CONDITION,AND OR NOT CONDITION
#IF CONDITION IS USED TO CHECK IF THE CONDITION IS TRUE OR NOT,IF THE CONDITION IS TRUE THEN IT WILL EXECUTE THE CODE INSIDE THE IF BLOCK OTHERWISE IT WILL NOT EXECUTE THE CODE INSIDE THE IF BLOCK
#ELSE CONDITION IS USED TO EXECUTE THE CODE INSIDE THE ELSE BLOCK IF THE CONDITION IN THE IF BLOCK IS FALSE
#ELIF CONDITION IS USED TO CHECK MULTIPLE CONDITIONS,IF THE CONDITION IN THE IF BLOCK IS FALSE THEN IT WILL CHECK THE CONDITION IN THE ELIF BLOCK AND IF THE CONDITION IN THE ELIF BLOCK IS TRUE THEN IT WILL EXECUTE THE CODE INSIDE THE ELIF BLOCK OTHERWISE IT WILL CHECK THE NEXT ELIF BLOCK OR ELSE BLOCK
#AND CONDITION IS USED TO CHECK IF BOTH THE CONDITIONS ARE TRUE THEN IT WILL EXECUTE THE CODE INSIDE THE AND BLOCK OTHERWISE IT WILL NOT EXECUTE THE CODE INSIDE THE AND BLOCK
#OR CONDITION IS USED TO CHECK IF ANY ONE OF THE CONDITIONS IS TRUE THEN IT WILL EXECUTE THE CODE INSIDE THE OR BLOCK OTHERWISE IT WILL NOT EXECUTE THE CODE INSIDE THE OR BLOCK
#NOT CONDITION IS USED TO CHECK IF THE CONDITION IS FALSE THEN IT WILL EXECUTE THE CODE INSIDE THE NOT BLOCK OTHERWISE IT WILL NOT EXECUTE THE CODE INSIDE THE NOT BLOCK


age = 20
if age >= 18: #this is used to check if the age is greater than or equal to 18 or not, if it is greater than or equal to 18 then it will print the message below otherwise it will not print anything
    print("you are eligible to vote") #output will be like this you are eligible to vote
else :
    print("your not eligible for vote") #output will be like this your not eligible for vote

#another example of if condition
#colors = input("Enter a color: ")
colors = "red"
if colors == "red": #this is used to check if the color entered by the user is red or not, if it is red then it will print the message below otherwise it will not print anything
    print("stop") #output will be like this stop
elif colors == "yellow": #this is used to check if the color entered by the user is yellow or not, if it is yellow then it will print the message below otherwise it will not print anything
    print("wait") #output will be like this wait
elif colors == "green": #this is used to check if the color entered by the user is green or not, if it is green then it will print the message below otherwise it will not print anything
    print("go") #output will be like this go
else:
    print ("invalid color") #output will be like this invalid color if the user enters any color other than red, yellow and green


#nested if condition

age = int(input("enter your age: "))
has_id = input("do you have id? (yes/no): ")
if age >= 18 :
    if has_id == "yes": #this is used
        print("you are eligible for driving license") #output will be like this you are eligible for driving license
    else:
        print("you are not eligible for driving license,link for apply driving license is https://parivahan.gov.in/parivahan/")
else:
    print("u need wait for  get driving license,bcz u are not more than 18 years old")





#not use nested if condition but use and condition to check both the conditions in one line

if age >= 18 and has_id == "yes": #use and condition to check if both the conditions are true or not, if both the conditions are true then it will print the message below otherwise it will not print anything
#if we use or condition then it will check if any one of the conditions is true or not, if any one of the conditions is true then it will print the message below otherwise it will not print anything
    print("you are eligible for driving license")
else:
    print("you are not eligible for driving license,link for apply driving license is https://parivahan.gov.in/parivahan/")




#NOW WE USE in KEYWORD TO CHECK IF THE TARGET WORD IS PRESENT IN THE STRING OR NOT
#NOW BUILT APP TO GIVE OFFER FOR SPEICAL DAY OR SPECIAL ORDER AMOUNT OR SPECIAL MEMBERSHIP

order_amount = int(input("enter your order amount: "))
day = input("enter the day: ")
membership = input("enter your membership status (yes/no): ")
if (order_amount >= 1000 and day in ["sat","sun"]) or membership == "yes": #this is used to check if the order amount is greater than or equal to 1000 and the day is saturday or sunday or the membership status is yes, if any one of the conditions is true then it will print the message below otherwise it will not print anything
    print("you are eligible for special offer") #output will be like this you are eligible for special offer
else:
    print("you are not eligible for special offer") #output will be like this you are not eligible for special offer if the user enters any order amount less than 1000 and the day is not saturday or sunday and the membership status is no


#if  i give order amount 1500 and day is monday and membership status is yes then it will print you are eligible for special offer because the membership status is yes, even though the order amount is greater than 1000 and the day is not saturday or sunday but the membership status is yes so it will print you are eligible for special offer.
