class avgmark(object):
    def __init__(self,totalmark):
        self.test_totalmark=totalmark

        
    def get_avg(self):
        print(self.test_totalmark)
        self.avg = 80
        
        


class student_database(avgmark):
    def __init__(self,name,roll_no,ind_mark):
        self.test_name=name
        self.test_roll_no=roll_no
        self.test_ind_mark=ind_mark
        super(student_database,self).__init__(ind_mark)


Std_1=student_database(name="arun",roll_no="1234",ind_mark=[23,33,32,41])
print(Std_1.test_totalmark)
Std_1.get_avg()
print(Std_1.avg)


    
    
