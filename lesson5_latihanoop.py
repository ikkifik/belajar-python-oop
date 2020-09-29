# Belajar program oop -> membuat game sederhana

class Hero:
    def __init__(self, name, hp, atk, deff):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.deff = deff
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.atk)
    
    def diserang(self, lawan, atk_lawan):
        print(f"{self.name} diserang {lawan.name}")

        if self.deff <= 0:
            self.deff = 0
            self.hp -= atk_lawan
        elif self.deff >= 0:
            self.deff -= atk_lawan
            if self.deff <= 0:
                self.hp = self.hp + self.deff
                self.deff = 0
        else:
            self.hp = 0

        if self.hp <= 0:
            print("Permainan Berakhir!")
            print(f"{self.name} defeat!")
        else:
            print(f"armor terkini {self.name}: {self.deff}")
            print(f"hp terkini {self.name}: {self.hp}")
        print("-----")

# name, hp, atk, deff
sniper = Hero('sniper', 100, 10, 55)
axe = Hero('axe', 100, 20, 10)

axe.serang(sniper) # input argumen object lain
axe.serang(sniper)
axe.serang(sniper)
axe.serang(sniper)
axe.serang(sniper)
axe.serang(sniper)
axe.serang(sniper)
axe.serang(sniper)
