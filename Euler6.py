res=0
n=100
for i in range(2,n+1):
    for j in range(1,i):
        res+=(i*j)
print(res*2)

#Optimized Solution
Sum_of_n_Terms =n*(n+1)//2
Sum_of_n_sq_terms=n*(n+1)*(2*n+1)//6
res=Sum_of_n_Terms**2-Sum_of_n_sq_terms
print(res)