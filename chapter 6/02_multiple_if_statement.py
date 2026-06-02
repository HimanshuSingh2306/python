# If else
a = int(input("Enter your age: "))


# 1st if statement which is independent two 2nd if statement
if(a%2== 0):
  print("even")
# here 1st if extecuted

#2nd if statement
if(a>=18):
  print("you are eligible for vote")
elif(a<=0):
  print("You are entering an invalid age")
else:
  print("you are not eligible")  
  # here 2nd if executed