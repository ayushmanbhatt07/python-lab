# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.
l=['inches','yards','miles','millimeters','centimeters','meters','kilometers']
l1=[1,2,3,4,5,6,7]
l2=[12,0.333333,0.0001893939,304.8,30.48,0.3048,0.0003048]
a=float(input("enter the value in feet: "))
for i,j in zip(l1,l):
    print(i,":",j)
ch=int(input("enter your choice: "))
length=a*l2[(ch-1)]
print(length)