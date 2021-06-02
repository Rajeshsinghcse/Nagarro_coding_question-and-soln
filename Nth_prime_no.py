input1 = int(input())
n = 1
c = 0
while (c<input1):
    n+=1
    for i in range(2,n+1):
        if(n%i==0):
            break
        if(i==n):
            c+=1
print(n)