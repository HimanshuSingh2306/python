def greatest():
  a = int(input("Enter the num: "))
  b = int(input("Enter the num: "))
  c = int(input("Enter the num: "))
  if(a>b):
    if(a>c):
      print(a)
    else:
      print(c)
  else:
    if(b>c):
      print(b)
    else:
      print(c)        

greatest()

