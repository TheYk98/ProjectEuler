def isPalindrome(num):
    safe=num
    revNum=0
    while num>0:
        revNum=revNum*10+num%10
        num//=10
    return safe==revNum

def largestPalindrome(num1,num2):
    maxNum=0
    for i in range(num1,100,-1):
        for j in range(num2,100,-1):
            res=i*j
            #if str(res) == str(res)[::-1]:# (alternatively)
            if isPalindrome(res):
                if maxNum<res:
                    maxNum=res
    return maxNum
print(largestPalindrome(1000,1000))
