# Belajar inheritance -> Pewarisan

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligence(Hero):
    pass

class Hero_strength(Hero):
    pass

lina = Hero('lina', 100)
print(lina.name)

windranger = Hero_intelligence('windranger', 80)
print(windranger.name)

bloodseeker = Hero_strength('bloodseeker', 200) 
print(bloodseeker.name)