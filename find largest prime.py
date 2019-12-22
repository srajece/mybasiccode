inpt=600851475143

for i in range(2,inpt):
    if inpt%i==0:
        modinpt=inpt/i
        #print(modinpt)
        print(i)
        inpt=modinpt
        if(i>inpt):
            break
    else:
        i=i+1

print(i)

