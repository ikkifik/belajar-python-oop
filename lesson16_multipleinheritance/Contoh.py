class Team:
    
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TipeHero:
    
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team, TipeHero):
    
    def __init__(self, name, health):
        self.name = name
        self.health = health

bambang = Hero("Bambang", 100)
print(bambang.name)

bambang.setTeam('Radiance')
bambang.setTipe('Melee')

bambang.showTeam()
bambang.showTipe()

