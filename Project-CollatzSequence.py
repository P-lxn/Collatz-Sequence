#define a function named collatz with 1 parameter with the value number
def collatz(number):
    
    #determining if the (number) is odd or even
    #printing (number) with the correct operations for O or E
    #returning the final value of (number) back to the function
    #return is put last as it ends the exectution of the function call
    if number % 2 == 0:
    #even numbers
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
    #odd numbers
        print(3 * number + 1)
        return 3 * number + 1

#variable (result) is assigned to a value where users input an integer value
result = int(input("enter a number: "))

#while loop when the variable (result) is not equal to 1, keeps running. 
while result != 1:

    #(result) variable assigned and calls upon the collatz function
    #(result) parameters (number) is now equal to (result) 
    result = collatz(result)

    #if statement where the function will break, once the result is equal to 1. 
    if result == 1:
        break

