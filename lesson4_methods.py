class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method tanpa return
    def say_hello(self):
        print(f"Namaku adalah {self.name}")

    # method argument
    def health_up(self, up):
        self.health += up

    # method return
    def get_health(self):
        print("haiiii aku muncul") # print sebelum return akan keluar
        return self.health
        print("yhaa aku tak muncul") # print setelah return tidak akan keluar
        

hero1 = Hero('sniper', 100, 30, 20)
hero2 = Hero('luigi', 1000, 2, 4)

hero1.say_hello()
print(f"Nyawa {hero1.name} lama: {hero1.health}")
hero1.health_up(10)
print(f"Nyawa {hero1.name} baru: {hero1.health}")

print(f"Nyawa saat ini {hero1.get_health()}")