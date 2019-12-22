class Login(object):
    def authenticate(self,name,pwd):
        self.username=name
        self.password = pwd
        if self.username == "vel" and self.password == "admin":
            
            print("success")
            return True
        else:
            
            print("login failed")
            return False
            

class Student(Login):
    def __init__(self,username,password,marks,std):
        self.marks=marks
        self.std=std
        login_status=super(Student,self).authenticate(username,password)
        if login_status:
            self.show_marks()
            self.show_std()

    def show_marks(self):
        print (self.marks)
        
    def show_std(self):
        print (self.std)


    def set_average(self):
        avg=sum(self.marks)/len(self.marks)
        self.average_marks=avg

    @property #cannot change average value"""
    def average(self):
        return self.average_marks

stud=Student("vel","admin", [1,2,3,4,5],8)
stud.set_average()
print (stud.average)
