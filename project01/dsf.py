'''
snake = 0
water =-1
gun =1

'''
import random

computer = random.choice([0,-1,1])



youstr = input("choose : ")
str = {"s":0, "w":-1,"g":1}
revstr = {0:"sanke", -1:"water",1 :"gun"}
you = str[youstr]

print(f"you choose  {revstr[you]} \n  computer choose {revstr[computer]}")
if(computer == you):
  print("Match draw")
else:
  if(computer == 0 and you == 1):
    print("You win!")

  elif(computer == 0 and you == -1):
    print("You loss!")
      
  elif(computer == 1 and you == -1):
    print("You win!")

  elif(computer == 1 and you == 0):
    print("You loss!")

  elif(computer == -1 and you == 1):
    print("You loss!")

  elif(computer == -1 and you == 0):
    print("You win!")
