# def factorial(num):
#     if num == 0:
#         return (1)
#     else:
#         return (factorial(num-1)*num)
    
input = int(input("Enter a number: "))
# print (f"The factorial of {input} is {factorial(input)}")

total = 1
for i in range(1,input+1):
    total = total * (i)

print(total)



