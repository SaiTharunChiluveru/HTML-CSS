a=[1,2,3,1,4,5,4,5,3,2,1,6,6,7,8,9,8,7,6,5,6,7,8,9,0,0]
op=dict()

for i in a:
    try:
        co=op[i]
    except:
        co=0
    op.update({i:co+1})

print(op)

    
