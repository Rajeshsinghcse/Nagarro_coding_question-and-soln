# another method to reduce spaces
def countDer(n) :
    if n == 1 or n == 2 :
        return n-1;
    a = 0
    b = 1

    for i in range(3, n+1): 
        cur = (i-1)*(a+b)
        a = b
        b = cur
    return b
n = 4
print("count of Dearrangement is ", countDer(n))

#time complexity O(n)
#space complexity O(1)