l=[]
k=0
import random
while(k==0):
        l.clear()
        for i in range(6):
                l.append(random.randint(0,9))
        for i in range(6):
                if(l[i]==3):
                        k=k+1
print(l)


   


    





