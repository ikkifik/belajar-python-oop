# Belajar overriding 
class Hero: 
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print("Show Info di class Hero")
        print(f"{self.name} health : {self.health}")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    def showInfo(self):
        print("Show info di subclass Hero_Intelligent")
        print(f"{self.name} : \n\tTipe: Intelligent \n\thealth: {self.health}")


class Hero_strenght(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_intelligent('lina')
axe = Hero_strenght('axe')

#lina.showInfo()
axe.showInfo()