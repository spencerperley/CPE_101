list_den = [2, 3, 4, 0, 5, 6, 8] 
list_num = []
results = []
entered = 0
i=0
for num in list_den:
    while True:
        entered = int(input("Enter a number greater than or equal to 10: "))
        
        if entered >= 10:
            break
        else:
            print("Number must be greater than 10")
            
    list_num.append(entered)
    
    results.append((list_num[i]/list_den[i]) if (list_den[i] != 0) else (-1))
    
    i += 1
    
print(results)
