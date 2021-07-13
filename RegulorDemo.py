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
    @staticmethod
    def m1():
        super(C,C).m2()
        super(C,C).m3()
        super(C,C).m1(C)
        super(C,C).__init__(C)
C.m1()       
        

       
        
        














