while True:
    a=input("Enter email:")
    x=a.index('@')
    valid=True
    try:
        y=a.index('@',x+1)
        print( "email is not valid")
        valid=False
    except:
        
        valid=False

    if '@'  not in a:
        print( "email is not valid")
        valid=False
    if '.'  not in a:
        print( "email is not valid")
        valid=False
    try:
        z=a.index('.',x+1)
        
        valid=False
    except:
        print( "email is not valid")
        valid=False
        
    if not (isinstance(a[x-1],str) or isinstance(a[x-1],int)):
        print( "email is not valid")
        valid=False
    if not (isinstance(a[x+1],str) or isinstance(a[x+1],int)):
        print( "email is not valid")
        valid=False

    if not isinstance(a[z+1],str):
        print( "email is not valid")
        valid=False

    if(valid==True):
        print ('email is valid')
print(z)        



    
