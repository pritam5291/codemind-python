x,y=map(int,input().split())
for i in range(1,y+1):
    if(x%i==0 and y%i==0):
        gcd=i
lcm=(x*y)//gcd
print(lcm)
