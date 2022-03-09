def addOne(lv):
    if lv[len(lv)-1] == 9:
        if len(lv) == 1:
            return [1,0]
        
        else:
            return addOne(lv[:len(lv)-1]) + [0]
        
    else: 
        lv[len(lv)-1] = lv[len(lv)-1] + 1
        
        return lv


a = [9,9]

print(addOne(a))
