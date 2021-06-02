# Fanny is given a string along with the string which contains 
# single character x. She has to remove the character x from the
#  given string. Help her write a function to remove all occurrences of x 
# character from the given string.

# Input Specification:

# input1: input string s 

# input2: String containing any character x

# Output Specification:

# String without the occurrence of character x

# Example 1:

# input1: welcome to mettl 

# input2: l



# Output: wecome to mett
def removechar(s,c) :
    counts = s.count(c)
    s=list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = ''.join(s)
    print(s)

# drivers code
if __name__ == '__main__':
    s="welcome to mettle"
    removechar(s,'l')

#time complexity O(n) where n is length of string
# space complexity O(1)