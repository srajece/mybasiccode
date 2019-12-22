import re
f=open('raj.txt','r')
for line in f:
    
    
        
    for word in line.split():
        if re.findall('offset=',word):
            x=word
            
            
            a=float(word[word.index('=')+1:])
            a=str(a-50.5)
            x='offset='+a
            
            neww=open('raj2.txt','a')
            neww.write(x)
            neww.write(' ')
            
        else:
            neww=open('raj2.txt','a')
            neww.write(word)
            neww.write(' ')
    neww=open('raj2.txt','a')
    neww.write("\n")
        

                
f.close()
neww.close()
                
            
            
        



        



