def goodDay(name,ending ="thank you"): 
    # yeha jo ending me value de di gyi hai iska matalb ye hai ki yadi ending ko calling argument se value milati hai to vahi print kare nahi to ye default thanks hi print karga
  print("Good morning", name)
  print(ending)
  return"ok"


a = goodDay("Himanshu","thanks") 
goodDay("himanshu")
print(a)