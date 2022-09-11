#it just normal e calculator of my basic add multiply,divide,minus, cse110 

# ask user for calculation to be performed
operation = input("Would you like to add/subtract/multiply/divide? ").lower( )
# ask for numbers, alert order matters for subtracting and dividing
if operation == "subtract" or operation == "divide":
    print( "You chose {}.".format(operation) )
    print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
# setup try/except for mathematical operation
try:
    num1, num2 = float(num1), float(num2)#  perform operation and print result
    if operation == "add":
        result = num1 + num2
        print( "{} + {} = {}".format(num1,num2,result))
    elif operation == "subtract":
        result = num1 - num2
        print( "{} - {} = {}".format(num1, num2, result) )
    elif operation == "multiply":
        result = num1 * num2
        print( "{} * {} = {}".format(num1, num2, result) )
    elif operation == "divide":
        result = num1 / num2
        print( "{} / {} = {}".format(num1, num2, result) )
    else:
 # else will be hit if they didn't chose an option correctly
        print("Sorry, but '{}' is not an option.".format(operation) )
except:

    print("Error: Improper numbers used. Please try again.")
