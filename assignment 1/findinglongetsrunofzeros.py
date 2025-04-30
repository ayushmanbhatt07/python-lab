# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
import random
l=[]
for i in range(101):
    a=random.randint(0,1)
    l.append(a)
print(l)
max_run=0
current_run=0
for i in l:
    if(i==0):
        current_run+=1
        if(current_run>max_run):
            max_run=current_run
    else:
        current_run=0
    
print(max_run)