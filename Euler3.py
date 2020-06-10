sieve=[2,3]
maxfactor=0
i=4
number=600851475143
while i<=number:
    Prime=True
    if i%2==0:
        i+=1
        continue
    for pf in sieve:
        if i%pf==0:
            Prime=False
    if Prime:
        sieve.append(i)
        if number%i==0:
            while number%i==0:
                number//=i
            maxfactor=i
    i+=1
print(maxfactor)
        
        



