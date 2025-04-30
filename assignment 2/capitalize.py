# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.
word=input("enter the word:")
l=list(word)#converting string to list
a=len(l)
for i in range(1,a,2):# range from 1 since first character would remain as it is
    l[i]=l[i].upper()#capitalizing alternate characters
str=''.join(l)#converting list to string syntax
print(str)