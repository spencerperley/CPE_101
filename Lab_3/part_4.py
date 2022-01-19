def factorial(num):
    if num == 0:
        return (1)
    else:
        return (factorial(num-1)*num)
    
input = int(input("Enter a number: "))
print (f"The factorial of {input} is {factorial(input)}")