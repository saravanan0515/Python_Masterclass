#operators and expressions

amt = 1200
tax = amt * 0.05  #5% tax
total = amt + tax  #addition expression
print("Total amount is:", total)  #print total before discount
if total > 1000:
    discount = total * 0.10 #10% discount
    total -= discount #subtraction expression
print("Total amount after discount is:", total) #print total after discount



#logical expression

age = 20
student = "yes"  #use yes or no and use true or false
if age >= 18 and student == "yes":      #use or and not
    print("You are eligible for the offer.")
else:
    print("You are not eligible for the offer.") 





#input method

x= input("enter the value for x:")
y= input("enter the value for y:")

print(int(x) + int(y))