class Login:
    def authenticate(self,name,pwd):
        self.username=name
        self.password=pwd
        if self.username=='vel' and self.passowrd == 'admin':
            print('Login Success')
        else:
            print('Login Failed')

ad=Login.authenticate('vel','admin','h')

    
