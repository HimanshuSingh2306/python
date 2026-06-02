'''
snake = 1
water = 0
gun  =-1
'''
import random
computer = random.choice([0,1,-1])


youstr = (input("choose: "))
print("")

str = {"s":1,"w":0,"g":-1}
revstr = {1:"snake",0:"water",-1:"gun"}
you = str[youstr]

print(f"you choose  {revstr[you]} \n computer choose {revstr[computer]}")
if(computer == you):
  print("Draw")
else:
  if(computer == 1 and you == 0):
    print("you lose")

  elif(computer == 1 and you == -1):
    print("you win")

  elif(computer == 0 and you == 1):
    print("you win")

  elif(computer == 0 and you == -1):
    print("you lose")

  elif(computer == -1 and you == 1):
    print("you lose")

  elif(computer == -1 and you == 0):
    print("you win")
      