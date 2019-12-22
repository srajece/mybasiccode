a=int(input("Enter the number:"))
b=int(input("Enter the number of click:"))
count=0
disp={2:['c','a','b'],3:['f','d','e'],4:['i','g','h'],5:['l','j','k'],6:['o','m','n'],7:['s','p','q','r'],8:['v','t','u'],9:['z','w','x','y']}

if(a==7 or a==9):
    chs=disp[a]
    opt=chs[b%4]
    print(opt)
    
else:
    chs=disp[a]
    opt=chs[b%3]
    print(opt)

