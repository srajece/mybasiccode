count=0

for i in range(212300000,10000000000000000):
    count=0
    for j in range(1,21):
        if (i%j==0):
            
            count+=1
    if count==20:
        print(i)
        break
            
        
    
