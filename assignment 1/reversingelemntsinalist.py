# You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]
l=[]
r=[]
a=int(input("enter the number of students in the class: ")) 
for i in range(a):
    name=input("enter the name of the students:")
    if(len(name)>15):
        name=name[0:16]
        print(name)
    l.append(name)
    s=name[::-1]
    r.append(s)
print(l)
print(r)