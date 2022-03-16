s = input() 
 
s1 = list(set(s.split())) 
s1.sort()

print(len(s1)) 
 
for i in s1: 
  if i.isalpha(): 
    print(i) 
  else: 
    print(i[:-1])