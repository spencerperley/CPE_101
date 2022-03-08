def addM(m1,m2):
    return[[m1[i][j]+m2[i][j] for j in range(0,len(m1[0]))] for i in range(0,len(m1))]

a=[[3,2,1],[1,2,3],[3,2,1]]
b=[[1,2,3],[3,2,1],[1,2,3]]

print(addM(a,b))