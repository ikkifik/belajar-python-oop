class Hero: # template
    pass

hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

# deklarasi attribute class
hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero1.health = 200

hero3.name = "lich"
hero1.health = 120

# test- output class
print(hero1)
print(hero1.__dict__) 
print(hero1.name) # pemanggilan attribute nama dari object hero1 