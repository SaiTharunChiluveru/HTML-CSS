def fun(nums,target):
    li=list()
    for i in range(len(nums)-2):
            x=nums[i]
            for j in range(i+1,len(nums)-1):
                y=nums[j]
                for k in range(j+1,len(nums)):
                    z=nums[k]
                    li.append(x+y+z)
                d=target
                print(li)
                for l in li:
                    if(d>abs(target-l)):
                        d=abs(target-l)
    print(d)


fun([0,2,1,-3],1)
