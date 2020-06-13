prevres=0
for i in range(2,101):
    for j in range(1,i):
        prevres=prevres+(i*j)
print(prevres*2)