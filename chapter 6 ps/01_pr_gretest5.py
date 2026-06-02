a = int(input("enter num:"))
b = int(input("enter num:"))
c = int(input("enter num:"))
d = int(input("enter num:"))
e = int(input("enter num:"))

if(a>b):
  if(a>c):
    if(a>d):
      if(a>e):
        print(a)
      else:
        print(e)
    else:
      if(d>e):
        print(d)
      else:
        print(e)
  else:
    if(c>d):
      if(c>e):
        print(c)
      else:
        print(e)
    else:
      if(d>e):
        print(d)
      else:
        print(e)
else:
  if(b>c):
    if(b>d):
      if(b>e):
        print(b)
      else:
        print(e)
    else:
      if(d>e):
        print(d)
      else:
        print(e)
  else:
    if(c>d):
      if(c>e):
        print(c)
      else:
        print(e)
    else:
      if(d>e):
        print(d)
      else:
        print(e)                                               
