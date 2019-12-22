while True:
    
    count=0
    a=input("enter the string")
    b=input("Enter the string to find in a")
    for i in a:
        if (b==i):
            count=count+1
    print(count)
