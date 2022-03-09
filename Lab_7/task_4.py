def linear_Search_uniq(ls,key): # this sufieces what the example tells us to do 
    return [value for value in ls if not(value == key)]

def lSu(ls,key):
    return list(set(ls))



def ss(ls):
    for i in range(1,len(ls)):
        key = ls[i-1]
        comparator = ls[i]
        for j in range(i,len(ls)):
            comparator = ls[j] if ls[j] <= comparator else comparator
            
            
        if key > comparator:
            ls[ls.index(comparator)] = key
            ls[i-1] = comparator
            
