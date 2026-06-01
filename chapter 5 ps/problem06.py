s = {}
name1 = input("Enter the name")
lang1= input("enter the language")

name2 = input("Enter the name")
lang2= input("enter the language")

name3 = input("Enter the name")
lang3= input("enter the language")

name4 = input("Enter the name")
lang4= input("enter the language")

s.update( {name1: lang1,name2:lang2,name3:lang3,name4: lang4})
print(dict(s))