def isloggedin(func):
    def check():
        login =True
        print("checking")
        if login == True:
            print(func)
            func()
        else:
            print("login failed")
    print('hai')
    return check

@isloggedin
def ordinary():
    print ("i am ordinary")

@isloggedin
def show_profile():
    print("Myprofile")

ordinary()
show_profile()
'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())
'''
