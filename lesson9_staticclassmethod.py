# Belajar static method dan class method -> decorator
# enkapsulasi untuk Class 

class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1
    
    # method ini hanya berlaku untuk objek
    def getJumlah1(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek, tapi berlaku untuk class
    def getJumlah2():
        return Hero.__jumlah

    # method static (decorator), nempel ke object dan class
    @staticmethod
    def getJumlah3():
        return Hero.__jumlah

    @classmethod
    def getJumlah4(cls):  
        return cls.__jumlah 


sniper = Hero("sniper")
# print(Hero.__jumlah) tidak bisa diakses
# print(Hero.getJumlah2()) tidak bisa diakses
print(Hero.getJumlah2())

rikimaru = Hero("rikimaru") 
print(rikimaru.getJumlah3())

mirana = Hero("mirana") 
print(Hero.getJumlah4())
print(mirana.getJumlah4())