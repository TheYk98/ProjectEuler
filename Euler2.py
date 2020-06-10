limit=4*(10**6)
prev=1
curr=2
sum=2
while curr<=limit:
    curr=prev+curr
    prev=curr-prev
    if curr%2==0:
        sum+=curr

print(sum)