class Login(object):
    
    def __init__(self,name,pwd):
        self.username=name
        self.password = pwd

    def authenticate(self):
        if self.username == "vel" and self.password == "admin":
            print("success")
        else:
            print("login failed")

class Student(Login):
    def __init__(self,username,password,marks,std):
        self.marks=marks
        self.std=std

    def show_marks(self):
        print (self.marks)
        return self
    def show_std(self):
        print (self.std)
    

stud=Student("vel","admin",[10,20,30], 10)
stud.show_marks()
stud.show_std()

stud1=Student("vel","admin",[10,20,30], 10).show_marks()
stud1.show_std()

stud=Student("vel","admin",[10,20,30], 10).show_marks()
stud.show_std()
