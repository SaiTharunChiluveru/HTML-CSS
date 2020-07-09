s="HELLO mama my name is THARUN how are yoyu IAm fine"
di=dict()

for i in s:
    x=0
    x=di.get(i)
    if(x==None):
        x=0

    x=x+1
    di.update({i:x})
print(di)


