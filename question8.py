def maximum(numOne, numTwo):
    if numOne>numTwo:
        return numOne;
    else:
        return numTwo;

numOne = float(input("Enter your first number:  "))
numTwo = float(input("Enter your second number:  "))
print("You entered: {} {} " .format(numOne,numTwo))

print("The larger of the two numbers is: {} " .format(maximum(numOne,numTwo)))
