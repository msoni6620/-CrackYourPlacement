# brute force approach
def setZeroes(matrix):
        rw=len(matrix)
        cl=len(matrix[0])
        l=[]
        for i in range(rw):
            l1=[]
            for j in range(cl):
                l1.append(matrix[i][j])
            l.append(l1)
        for i in range(rw):
            for j in range(cl):
                if(matrix[i][j]==0):
                    o=i
                    lp=j

                    for r in range(rw):
                        l[r][lp]=14082003
                    for co in range(cl):
                        l[o][co]=14082003
        for i in range(rw):
            for j in range(cl):
                if(l[i][j]==14082003 or l[i][j]==0):
                    matrix[i][j]=0
        return matrix
# print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

# more optimal approach
def setZeroes1(matrix):
    rw=len(matrix)
    cl=len(matrix[0])
    col=1
    for i in range(rw):
        for j in range(cl):
            if(matrix[i][j]==0):
                matrix[i][0]=0 
                if(j!=0):
                    matrix[0][j]=0
                else:
                    col=0
    for i in range(1,rw):
        for j in range(1,cl):
            if(matrix[i][j]!=0):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0

   
    if(matrix[0][0]==0):
        for i in range(cl):
            matrix[0][i]=0
    if(col==0):
        for i in range(rw):
            matrix[i][0]=0
    return matrix

                    

print(setZeroes1([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
        
        