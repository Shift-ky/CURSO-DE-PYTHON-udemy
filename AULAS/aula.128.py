#s1 = set()  #set vazio 
#s1 = set('Robson', 1,2,3) #set com valores



#l1 = (1,2,2,3,3,4,4,5,5,6,6)

#s1 = set(l1)
#l2 = list(s1)
#print(l2)

### add, update, clear, discart

#s1 = set()
#s1.add(('Robson'))
#s1.add(123)
#s1.add(125)
#s1.add(127)
#s1.clear()
#s1.discard(1)
#s1.discard(123)
#s1.discard(125)

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s3
print(s3)
s3 = s1 ^ s2
print(s3)
 