# Create the following lists using a for loop.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
l=[]
c=1
for i in range(97,123):
    a=chr(i)*c
    l.append(a)
    c=c+1
print(l)
