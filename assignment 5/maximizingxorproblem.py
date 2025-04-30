# 1. Maximizing XOR
# Given two integers: L and R, Find the maximal values of A xor B given, L <= A <= B <= R
# Input Format:
# The input contains two lines, L is present in the first line. R in the second line.
# Constraints
# 1 <= L <= R <= 103
# Output Format:
# The maximal value as mentioned in the problem statement.
# Sample Input #00:
# 1
# 10
# Sample Output #00:
# 15
# Sample Input #01:
# 10
# 15
# Sample Output #01:
# 7
# Explanation
# In the second sample let’s say L=10, R=15, then all pairs which comply to above condition are
# 10 xor 10 = 0
# 10 xor 11 = 1
# 10 xor 12 = 6
# 10 xor 13 = 7
# 10 xor 14 = 4
# 10 xor 15 = 5
# 11 xor 11 = 0
# 11 xor 12 = 7
# 11 xor 13 = 6
# 11 xor 14 = 5
# 11 xor 15 = 4
# 12 xor 12 = 0
# 12 xor 13 = 1
# 12 xor 14 = 2
# 12 xor 15 = 3
# 13 xor 13 = 0
# 13 xor 14 = 3
# 13 xor 15 = 2
# 14 xor 14 = 0
# 14 xor 15 = 1
# 15 xor 15 = 0
# Here two pairs (10,13) and (11,12) have maximum xor value 7 and this is the answer.
def digittobinary(n):
    b=bin(n)
    b=b[2:]
    return b
def returnxor(a,b):
    l1=list(a)
    l2=list(b)
    l3=[]
    for i in range(len(l1)):
        m=int(l1[i])
        n=int(l2[i])
        c=m^n
        l3.append(c)
    x=str(l3)
    return x
print("enter the two numbers")
L=int(input("enter the starting number less than 1000: "))
R=int(input("enter the ending number less than 1000: "))
l=[ch for ch in range(L,(R+1))]
print(l)
b=[]
for i in l:
    a=(digittobinary(i))
    b.append(a)
print(b)
for i in range(len(b)):
    x=returnxor(b[i],b[i+1]) # x is a string
    print(x)
