import random
#function that generates a list of random length with random numbers inside (can be duplicates!)
def rand_list():
  a = []
  n = random.randint(1,100)
  [a.append(random.randint(0,100)) for i in range(0, n)]
  return a
a = rand_list()
print(a)

#method 1: sets (1LOC)
b= list(set(a))

print(b)

#method 2: loop and list (3LOC)
c=[]
for i in a:
  if i not in c:  
    c.append(i)
    
print(c)

# if correct, b and c have to have the same length
print(len(a), len (b), len(c))