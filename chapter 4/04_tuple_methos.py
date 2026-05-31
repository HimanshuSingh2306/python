a = (1,32,4,45,False,45, "rohan" , "shivam") # tuple is also immutable as string
print(type(a))
print(a)
no = a.count(45)
print(no)
print(a.index(4))
print(len(a))
A,b,c,d,e,f,g,h = a
print(A,b,c,d,e,f,g,h)