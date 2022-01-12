
from datetime import datetime

currentYear = datetime.now().year

greeting = "Hello"

name = input("Enter name of partner:")

birthYear = int(input("what year were you born"))

print(f"{name} is {currentYear - birthYear} in the current year {currentYear}")

 