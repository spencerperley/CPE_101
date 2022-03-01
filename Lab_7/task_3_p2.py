from task_3_p1 import *

number = int(input("Enter a number"))
even = "even" if isEven(number) else "odd"
positive = "positive and " if number>=0 else "negative and "

print(positive,even)