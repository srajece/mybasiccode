x=0
a=0
b=0
for i in range (100,1000):
    for j in range(100,1000):
        opt=i*j
        c=str(opt)
        y=c[::-1]
        w=int(y)
        if ( opt==w ):
            if(x<opt):
                a=i
                b=j
                x=opt
print(a,b,x)
                
                
         


