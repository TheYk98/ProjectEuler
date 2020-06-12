# num2>num1 !! 
def gcd(num1,num2):
    if num1==0:
        return num2
    return gcd(num2%num1,num1)

# prd of 2 numbers =lcm*gcd
res=10
for i in range(res-1,1,-1):
    res=(res*i)//gcd(i,res)
print(res)

