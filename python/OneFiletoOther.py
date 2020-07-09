with open("text1.txt","r") as f1:
    f2=open("text2.txt","a+")
    f1_lines=f1.readlines()
    f2.writelines(f1_lines)
    f2.close()

    
