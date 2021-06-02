#input n = 2
#output 1
def countDer(n):
    if (n == 1): return 0
    if (n == 2): return 1
    return (n - 1) * (countDer(n- 1)+countDer(n-2))

#drivers code
n = 3
print("count dearangement is ", countDer(n))

# time complexity O(n)
# space complexity O(n)
