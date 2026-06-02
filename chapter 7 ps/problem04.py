num = int(input("Enter the num"))

for i in range(2,num//2):
  if(num%i)==0:
    print("This is not prime")
    break
else:

    print("this is prime number")  