#This program takes in a positive float and outputs its square root
#Sources:https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#https://realpython.com/python-print/, https://www.w3schools.com/python/ref_string_format.asp ,  https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method


#This is the function that will be run to generate the square root
def squareFun(number, iterations = 500): 
    a = float(number) # this is the number we want to get the square root of
    for i in range(iterations): # The number of iterations
        number = 0.5 * (number + a / number) # This equation was given in the medium article. It is x_(n+1) = 0.5 * (x_n +a / x_n)

    return number

userNum = float(input("please enter a positive number: ")) # This takes in the input from the user and changes it to a float
print("The Square root of", userNum,  "is", squareFun(userNum)) # this prints the squareFun function and enters the number entered by the user into the function to give the result

