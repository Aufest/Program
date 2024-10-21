n=10000
def dis(a):
    for i in range(2,a//2+1):   
        if a%i==0:
            return 0
    return a

for x in range(2,n):
    a=dis(x)
    if a!=0:
        print(a)
