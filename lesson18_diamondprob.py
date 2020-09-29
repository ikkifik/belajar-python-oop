# Diamond Problem

#       A       jika tidak ada(method) baru mencari di super class utamanya.
#      / \
#     B   C     jika tidak ditemukan(method) akan mulai mencari di parentnya, secara linier
#      \ /
#       D       pemanggilan method akan dimulai dari bawah

class A:
    
    def show(self):
        print("Ini adalah show A")

class B(A):
    
    def show(self):
        print("Ini adalah show B")

class C(A):
    
    def show(self):
        print("Ini adalah show C")

class D(B,C):
    pass

objek = D()
objek.show()
#help(objek)

'''
Method resolution order: (urutan method yang akan dipanggil)
 |      D
 |      B
 |      C
 |      A
'''