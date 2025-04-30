"""Find Digits:
You are given a number N, you need to print the number of positions where digits exactly
divides N.
Input format
The first line contains T (number of test cases followed by T lines each containing N).
Constraints
1 <= T <= 15
0 <= N <= 1010
Output Format
For each test case print the number of positions in N where digits in that number exactly
divides the number N in separate line.
Input
2
12
13
Output
2
1
Explanation

Test case 1:
2 digits in the number 12 divides the number exactly.
Test case 2:
Only 1 digit in the number 13 divides the number exactly.
"""
def digitextraction(n):
    numbers=str(n)
    digits=[int(i) for i in numbers if i!=0]
    return digits
l=[]
T=int(input("enter the number of test cases from 1<=T<=15: "))
for i in range(0,T):
    a=int(input("enter the number from 0<=N<=1010: "))
    l.append(a)
print(l)
for i in range(0,T):
    c=0
    d=digitextraction(l[i])
    N=int(l[i])
    for j in d:
        if N % j== 0:
            c+=1
    print(f"the number of digits dividing {N} in {N} is/are {c}")

        

