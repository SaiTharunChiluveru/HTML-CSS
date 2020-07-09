


def fundom2(mp):
            if(mp==0):
                return
            li=list(i for i in range(1,mp+1))
            op=list()
            op.append(li[0])
            i=1
            while(sum(op)<mp):
                op.append(li[i])
                i=i+1
            print("for ",mp ,"List is",op)
            
fundom2(2)
fundom2(0)
fundom2(3)
fundom2(5)
fundom2(6)
fundom2(10)
fundom2(11)
fundom2(12)
fundom2(13)
fundom2(14)
fundom2(15)
fundom2(16)
fundom2(17)
fundom2(21)
fundom2(22)
fundom2(23)
fundom2(1036)





