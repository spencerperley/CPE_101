income = int(input("Enter your income: "))

brackets = [(539901,37,162718),(215951,37,49335.5),(170051,32,34647.5),(89076,24,15213.5),(41776,22,4807.5),(10276,12,1027.5),(0,10,0)]

for bracket in brackets:
    if income >= bracket[0]:
        print(f"An income of {income} places you in the {bracket[1]}% income bracket")
        tax = bracket[2] + ((bracket[1]/100)*(income - bracket[0]))
        print(f"The US Federal tax on an income of USD {income} is USD {tax} tax")
        break
        

