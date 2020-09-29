# Belajar setter dan getter -> python ver

class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = f"name {self.__name} : \n\thealth: {self.__health}"
    
    # decorator property -> mengubah sebuah method menjadi seperti variable
    @property
    def info(self):
        return f"name {self.name} : \n\thealth: {self.__health}"

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input    
    
    @armor.deleter
    def armor(self):
        print('Armor di delete')
        self.__armor = None

sniper = Hero('sniper', 100, 10)

print("-- Mengubah info --")
print(sniper.info) # pemanggilan seperti variable/property
sniper.name = "dahyun" 
print(sniper.info)

print("\n-- Getter dan setter untuk __armor --")
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print("\n-- Delete __armor --")
del sniper.armor
print(sniper.__dict__)






