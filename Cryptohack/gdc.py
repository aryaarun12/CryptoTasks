a=66528
b=52920
while 1:
    r=a%b
    if not r:
        break
    a=b
    b=r
print('GCD is:', b)
