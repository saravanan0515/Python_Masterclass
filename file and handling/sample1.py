feedback = input("enter your feedback:")
# feedback is user input that should save or store in given file 
with open("feedback.txt","a") as log: # log s alice name
    log.write(feedback + "\n")

print("thank you your feedback is saved!!")

#if i give very good in feedback input that save in feedback.txt
# we can give another feedback 
