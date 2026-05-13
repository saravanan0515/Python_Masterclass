#variables
#have  local,enclosing and global scope and also built in scope

delivery_partner="swiggy"  # this is a global variable and can be accessed anywhere in the code

def hotel(): # this is a function and it has its own local scope
    item ="pizza"  # this is a local variable and can only be accessed within the hotel function

    def ordernow(): # this is a nested function and it has its own local scope
        quantity=2  # this is a local variable and can only be accessed within the ordernow function
        print(f"ordering {quantity}-{item} using {delivery_partner}")
    ordernow()  # this is used to call the ordernow function and execute the code inside it
hotel()  # this is used to call the hotel function and execute the code inside it