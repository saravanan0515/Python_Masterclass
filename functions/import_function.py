#here we are importing the add function from the testcode module and using it to add two numbers together. The result is then printed to the console.
from testcode import add
result = add(5,5) # we just call and give value for arguments ,but not a add opretion ,bcz the opration is done in the add function which is defined in the testcode module, so we just call the function and pass the arguments to it, and it will return the sum of the two numbers, so the output will be like this 10 because we use return statement to return the sum of a and b when the function is called and we pass 5 and 5 as arguments to the function, so the output will be like this 10 because we use return statement to return the sum of a and b when the function is called and we pass 5 and 5 as arguments to the function
print(result) # if i use print instead of return in testcode module then it will print the sum of a and b when the function is called, but it will not return the value to the caller, its give none in output of our import_function.py 
#what if we need to divide the result like "print(result/2)".only return helps to get the value from modeul and give in present code to implement

#output will be like this 10 
