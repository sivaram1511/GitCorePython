class P:
    def __init__(self):
        print("parent class constructor")
    def m1(self):
        print("parent class M1 method")
    @classmethod
    def m2(cls):
        print("parent cls m2 clas method")
    @staticmethod
    def m3():
        print("parent class static method")
class C(P):
    @classmethod
    def m1(cls):
        super().m2()
        super().m3()
        super(C,cls).m1(cls)
        super(C,cls).__init__(cls)
C.m1()       
        

       
        
        














