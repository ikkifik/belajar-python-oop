# Belajar enkapsulasi

'''
- Buat semua variable 'private'
- untuk mengambil data gunakan getter 
- untuk men-set data gunakan setter
'''

class Hero:
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
    
    # getter
    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def diserang(self, atk):
        self.__hp -= atk


# awal game
earth_shaker = Hero("earth shaker", 100, 50)


# game berjalan
print(earth_shaker.getName())
print(earth_shaker.getHp())
earth_shaker.diserang(5)
print(earth_shaker.getHp())
