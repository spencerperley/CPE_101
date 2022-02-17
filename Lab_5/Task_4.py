from math import factorial


from math import exp

def exponentalAproximation(num, sigmaN =100):
    sum = 1
    for i in range(1,sigmaN+1):
        sum+= (num**i)/factorial(i)
        
    return sum

print(exponentalAproximation(4))
print(exp(4))

#effective to 13 decimals with num = 4