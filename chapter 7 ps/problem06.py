n = int(input("Enter the num: "))

fact =1
for i in range(1,n+1):
  fact = n*fact
  n = n-1
  i+=1
print(fact)  