class A:

    def method_A(self):
        print("ini adalah method A")

class B:

    def method_B(self):
        print("ini adalah method B")

class C(A,B):

    def __init__(self):
        pass

objek = C()

objek.method_A()
objek.method_B()