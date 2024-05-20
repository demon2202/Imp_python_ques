   x=[[1,2,3],[4,6,1],[2,8,6]]
   result=[[0,0,0],[0,0,0],[0,0,0]]
   for i in range (0,3):
        for j in range(0,3):
              result[i][j]=x[j][i]
   for k in result:
      print(k)
