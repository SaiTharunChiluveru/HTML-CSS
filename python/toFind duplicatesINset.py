a=[1,3,4,5,6,7,2,12,1,21,31,13,14,14,15,6]
s1 =set() #actual set
s2 =set()# duplicates

for i in a:
    if(i not in s1):
        s1.add(i)
    else:
        s2.add(i)
print(s2)        
