# Belajar class variable dan instance variable

class Hero: 
    # Class variable -> variabel static yang terdapat di class itu sendiri
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor): 
        # instance Variable -> variable di bawah ini hanya dimiliki objek hero saja
        self.name = inputName 
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth
        Hero.jumlah += 1
        print(f"Membuat hero dengan nama: {inputName}")


print(Hero.jumlah) # jumlah kosong
hero1 = Hero("sniper", 100, 50, 35)
print(Hero.jumlah) 
hero2 = Hero("Lich", 100, 100, 20)
print(Hero.jumlah) 
hero3 = Hero("Pudge", 300, 50, 50)
print(Hero.jumlah) 



