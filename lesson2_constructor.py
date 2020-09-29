# Belajar init constructor -> magic keyword
class Hero: # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor): # magic keyword
        self.name = inputName # init(initialization) akan dieksekusi pertama kali ketika objek dibuat
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth


hero1 = Hero("sniper", 100, 50, 35)
hero2 = Hero("Lich", 100, 100, 20)
hero3 = Hero("Pudge", 300, 50, 50)

print(hero1.__dict__) # pemanggilan object dengan dictionary
print(hero2.__dict__)
print(hero3.__dict__)

