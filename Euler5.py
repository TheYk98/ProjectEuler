def findAllFactors(num,product,factused):
    for i in range(2,num//2+1):
        if num%i==0:
            if factused[i]==0:
                factused[i]=1
            else:
                product//=i
    return product,factused  

factused={}
for i in range(1,21):
    factused[i]=0
product=1
for number in range(20,1,-1):
    
    if factused[number]==0:
        product*=number
        product,factused=findAllFactors(number,product,factused)
        print(product,factused)
    factused[number]=1

print(product)