s = set()
# 1==1.0 -> true 
# so the lengh of this set is 2
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))