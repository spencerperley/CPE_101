from math import factorial


from math import exp

def exponentalAproximation(num, sigmaN =100):
    sum = 1
    for i in range(1,sigmaN+1):
        sum+= (num**i)/factorial(i)
        
    return round(sum*100)/100

print(exponentalAproximation(6))
print(exp(6))

#effective to 13 decimals with num = 4