# Method Resolution Order -> Multiple inheritance
# Urutan method yang terjadi apabila terdapat 2 method dengan nama yang sama di class yang berbeda

class A:

    def show(self):
        print("Ini show A")
    
class B:

    def show(self):
        print("Ini show B")

class C(A,B):
    pass

objek = C()
objek.show()


'''
Urutan method yang terjadi adalah:
C
A
B
menurut pembuatan objek "class C(A,B)"
'''