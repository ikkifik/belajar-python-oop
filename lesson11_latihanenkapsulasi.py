class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandard = health
        self.__attPowerStandard = attPower
        self.__armorStandard = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandard * self.__level
        self.__attPower = self.__attPowerStandard * self.__level
        self.__armor = self.__armorStandard * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name} ({self.__level}): \n\thealth = {self.__health}/{self.__healthMax}\n\tattack = {self.__attPower}\n\tarmor = {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp

        if (self.__exp >= 100):
            print(self.__name, 'level up!')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandard * self.__level
            self.__attPower = self.__attPowerStandard * self.__level
            self.__armor = self.__armorStandard * self.__level
    
    def attack(self, enemy):
        self.gainExp = 50


slardar = Hero("slardar", 100, 5, 10) 
tidehunter = Hero("tidehunter", 100, 4, 12)

slardar.attack(tidehunter)
slardar.attack(tidehunter)
print(slardar.info)
