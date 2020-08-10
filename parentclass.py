class Parent():
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_all_info(self):
        print(self.fname,' ',self.lname,' age is ',self.age)


    def change_l_name(self,lname):
        self.lname = lname
        print('lname changed to',lname)



p1 = Parent('abhishek','saklani',24)
p1.get_all_info()
p1.change_l_name('sharma')
p1.get_all_info()