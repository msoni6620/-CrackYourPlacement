class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        c=len(matrix[0])
        r=len(matrix)
        l=[]
        for i in range(r):
            l1=[]
            for j in range(c-1,-1,-1):
                l1.append(matrix[j][i])
            l.append(l1)
        for i in range(r):
            for j in range(c):
                matrix[i][j]=l[i][j]

        
        